import pytest

def square(n):
    return n ** 2

def cube(n):
    return n ** 3

def fifth_power(n):
    return n ** 5

#Testing the functions
def test_square():
    assert square(2) == 4, "Test failed: 2 squared should be 4"
    assert square(-3) == 9, "Test failed: -3 squared should be 9"
    assert square(0) == 0, "Test failed: 0 squared should be 0"
    
def test_cube():
    assert cube(2) == 8, "Test failed: 2 cubed should be 8"
    assert cube(-3) == -27, "Test failed: -3 cubed should be -27"
    assert cube(0) == 0, "Test failed: 0 cubed should be 0"
    
def test_fifth_power():
    assert fifth_power(2) == 32, "Test failed: 2 to the fifth power should be 32"
    assert fifth_power(-3) == -243, "Test failed: -3 to the fifth power should be -243"
    assert fifth_power(0) == 0, "Test failed: 0 to the fifth power should be 0"
    
#Test for invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("a")
    with pytest.raises(TypeError):
        cube("b")
    with pytest.raises(TypeError):
        fifth_power("c")