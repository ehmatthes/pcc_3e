from employee import Employee

def test_give_default_raise():
    """Test that a default raise works correctly."""
    employee = Employee('eric', 'matthes', 65_000)
    employee.give_raise()
    assert employee.salary == 70_000

def test_give_custom_raise():
    """Test that a custom raise works correctly."""
    employee = Employee('eric', 'matthes', 65_000)
    employee.give_raise(10000)
    assert employee.salary == 75_000
