import importlib.util,json,sys,types
from pathlib import Path
import pytest

CREATOR="0x1111111111111111111111111111111111111111";REVIEWER="0x2222222222222222222222222222222222222222";OUTSIDER="0x3333333333333333333333333333333333333333"
BASE="Fund the open-source wallet security audit with 1000 units sent to the named audit collective after delivery of the final report. The collective may only perform the scoped wallet audit."
REVISED="Fund the open-source wallet security audit with 1200 units sent to the named audit collective after delivery of the final report. The increase covers an added mobile-wallet review."
HIDDEN="Fund the ecosystem security program with 1200 units sent to a new recipient. The recipient may spend the allocation on any security-related activity it selects."
SUMMARY="Discloses the increase from 1000 to 1200 units and the added mobile-wallet review scope."
MANIFEST=[{"target":"0x"+"a"*40,"selector":"0x12345678","value":0,"asset":"NATIVE","recipient":"0x"+"b"*40,"amount":1000}]
MANIFEST2=[{**MANIFEST[0],"amount":1200}]

class TreeMap(dict):
    @classmethod
    def __class_getitem__(cls,_):return cls
class U256(int):pass
class ContractBase:pass
class Write:
    def __call__(self,fn):return fn
class Public:write=Write();view=staticmethod(lambda fn:fn)
class Nondet:
    def __init__(self):
        self.answer={"decision":"FULLY_DISCLOSED","material_changes":["EXECUTION_ACTION","PURPOSE"],"summary_complete":True,"semantic_scope_expanded":False};self.prompts=[]
    def exec_prompt(self,prompt,**_):self.prompts.append(prompt);return self.answer
class Eq:
    def __init__(self):self.forced=None
    def prompt_comparative(self,fn,*_,**__):return self.forced if self.forced is not None else fn()

@pytest.fixture
def runtime(monkeypatch):
    n=Nondet();eq=Eq();g=types.ModuleType("genlayer");g.__all__=["gl","u256","TreeMap","typing"]
    g.gl=g;g.Contract=ContractBase;g.public=Public();g.nondet=n;g.eq_principle=eq;g.message=types.SimpleNamespace(sender_address=CREATOR);g.message_raw={"datetime":"2026-10-06T00:00:00+00:00"};g.u256=U256;g.TreeMap=TreeMap;g.typing=types.SimpleNamespace(Any=object)
    monkeypatch.setitem(sys.modules,"genlayer",g);spec=importlib.util.spec_from_file_location("scope_sentinel_test",Path("contracts/scope_sentinel.py"));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m,m.ScopeSentinel(),g,n,eq

def set_sender(g,a):g.message.sender_address=a
def create(c):return c.create_proposal("Wallet audit mandate",BASE,json.dumps(MANIFEST))
def proposed(c,g,text=REVISED,summary=SUMMARY,manifest=MANIFEST2):
    create(c);p=c.get_proposal(1);r=c.get_revision(1);set_sender(g,REVIEWER)
    return c.propose_revision(1,1,r["text_digest"],text,summary,json.dumps(manifest),p["revision"])
