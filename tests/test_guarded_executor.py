import importlib.util,json,sys
from pathlib import Path
import pytest
from conftest import CREATOR,OUTSIDER,set_sender

def load_executor(g):
    spec=importlib.util.spec_from_file_location("guarded_executor_test",Path("contracts/guarded_executor.py"));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m.GuardedScopeExecutor(CREATOR)

def test_only_bound_guard_can_execute_and_receipt_is_single_use(runtime):
    _,_,g,_,_=runtime;e=load_executor(g);recipient="0x"+"b"*40;action=json.dumps({"nonce":1,"chain_id":61997,"target":"0x"+"a"*40,"recipient":recipient,"amount":1200})
    digest="sha256:"+"a"*64;receipt="sha256:"+"b"*64
    set_sender(g,OUTSIDER)
    with pytest.raises(ValueError,match="ONLY_SCOPE_SENTINEL"):e.execute_authorized(1,2,digest,action,receipt)
    set_sender(g,CREATOR);assert e.execute_authorized(1,2,digest,action,receipt)=="EXECUTED"
    assert e.get_execution(1)["status"]=="EXECUTED" and e.get_info()["execution_count"]==1
    assert e.get_allocation(recipient)==1200 and e.get_info()["total_authorized"]==1200
    with pytest.raises(ValueError,match="AUTHORIZATION_REPLAY"):e.execute_authorized(1,2,digest,action,receipt)

def test_executor_rejects_malformed_authorization(runtime):
    _,_,g,_,_=runtime;e=load_executor(g);set_sender(g,CREATOR)
    with pytest.raises(ValueError,match="INVALID_MANIFEST_DIGEST"):e.execute_authorized(1,2,"bad","{}","sha256:"+"b"*64)
