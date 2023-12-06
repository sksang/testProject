import pytest

@pytest.mark.parametrize("a", [1,2,3,4,5])
def test_a1(a):
    print(a)
    assert a > 0
    
def test_a2():
    print("In test_a2")
    assert 1 == 1