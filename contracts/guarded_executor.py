# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *
import hashlib,json,re

ADDRESS=re.compile(r"^0x[0-9a-f]{40}$")
def canon(v):return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=True)
def addr(v):
    s=str(v).lower()
    if not s.startswith("0x"):
        try:s="0x"+format(int(v),"040x")
        except Exception:pass
    return s
def require(ok,msg):
    if not ok:raise gl.vm.UserError(msg)

class GuardedScopeExecutor(gl.Contract):
    guard:str
    execution_count:u256
    receipts:TreeMap[str,str]
    executions:TreeMap[u256,str]
    allocations:TreeMap[str,str]
    total_authorized:u256
    def __init__(self,guard:str):
        value=addr(guard);require(ADDRESS.fullmatch(value) is not None and value!="0x"+"0"*40,"INVALID_GUARD")
        self.guard=value;self.execution_count=u256(0);self.receipts=TreeMap[str,str]();self.executions=TreeMap[u256,str]();self.allocations=TreeMap[str,str]();self.total_authorized=u256(0)
    @gl.public.write
    def execute_authorized(self,proposal_id:u256,revision_id:u256,manifest_digest:str,action_json:str,authorization_receipt:str)->str:
        require(addr(gl.message.sender_address)==self.guard,"ONLY_SCOPE_SENTINEL")
        require(re.fullmatch(r"sha256:[0-9a-f]{64}",manifest_digest) is not None,"INVALID_MANIFEST_DIGEST")
        require(re.fullmatch(r"sha256:[0-9a-f]{64}",authorization_receipt) is not None,"INVALID_RECEIPT")
        require(authorization_receipt not in self.receipts,"AUTHORIZATION_REPLAY")
        try:action=json.loads(action_json)
        except Exception:raise gl.vm.UserError("INVALID_ACTION")
        require(type(action) is dict and int(action.get("nonce",0))>0 and int(action.get("chain_id",0))>0,"INVALID_ACTION")
        recipient=str(action.get("recipient","")).lower();amount=int(action.get("amount",-1))
        require(ADDRESS.fullmatch(recipient) is not None and recipient!="0x"+"0"*40 and amount>=0,"INVALID_EFFECT")
        eid=u256(int(self.execution_count)+1);self.execution_count=eid
        record={"id":int(eid),"proposal_id":int(proposal_id),"revision_id":int(revision_id),"manifest_digest":manifest_digest,"authorization_receipt":authorization_receipt,"action":action,"status":"EXECUTED"}
        self.executions[eid]=canon(record);self.receipts[authorization_receipt]=canon({"execution_id":int(eid),"digest":"sha256:"+hashlib.sha256(action_json.encode()).hexdigest()})
        previous=int(self.allocations[recipient]) if recipient in self.allocations else 0;self.allocations[recipient]=str(previous+amount);self.total_authorized=u256(int(self.total_authorized)+amount)
        return "EXECUTED"
    @gl.public.view
    def get_execution(self,execution_id:u256)->dict:
        if int(execution_id)<1 or int(execution_id)>int(self.execution_count):return {}
        return json.loads(self.executions[execution_id])
    @gl.public.view
    def get_allocation(self,recipient:str)->int:
        key=addr(recipient);return int(self.allocations[key]) if key in self.allocations else 0
    @gl.public.view
    def get_info(self)->dict:return {"name":"GuardedScopeExecutor","guard":self.guard,"execution_count":int(self.execution_count),"total_authorized":int(self.total_authorized)}

Contract=GuardedScopeExecutor
