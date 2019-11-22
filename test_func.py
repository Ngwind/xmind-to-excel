from utils import get_config

def test_get_config():
    assert get_config("default_prefix") == ""
    assert get_config("default_execType") == "手工"
    assert get_config("default_testType") == "WEB测试"
