import pytest

from employee import Employee

@pytest.fixture
def employee():
    """An Employee object that will be available to all test functions."""
    employee = Employee('eric', 'matthes', 65_000)
    return employee

def test_give_default_raise(employee):
    """Test that a default raise works correctly."""
    employee.give_raise()
    assert employee.salary == 70_000

def test_give_custom_raise(employee):
    """Test that a custom raise works correctly."""
    employee.give_raise(10000)
    assert employee.salary == 75_000
