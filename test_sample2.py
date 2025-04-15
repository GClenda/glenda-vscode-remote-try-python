# test_sample.py

# Import the function to test
from your_module import add  # Replace 'your_module' with the actual module name

def test_add():
    # Test cases for the 'add' function
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-5, -5) == -10
