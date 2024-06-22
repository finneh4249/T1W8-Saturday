def test_success_code():
    assert 10 / 2 == 5 # Test will pass
    
def test_fail_code():
    assert 10 / 2 == 0 # Test will fail
    
def test_exception():
    if True:
        raise ValueError("You got a value error!!")