import calculator as calc
import pytest


def test_operation_with_empty_operator():
    #input
    a=1
    b=6
    operator = ""

#     process
    result = calc.calculate(a,b,operator)

#     output
    assert result is None


def test_sum_two_numbers_success():

    # input
    value1 = 2
    value2 = 3
    operator = "+"

    # process
    result = calc.calculate(value1,value2,operator)

    # assert (Check if True/False, raises exception when False and Passes when True)
    assert result is 5

def test_divide_by_zero():
    # input
    a=4
    b=0
    operator = '/'

    # process and assert
    # General Exception also works
    # with pytest.raises(Exception):
    with pytest.raises(ZeroDivisionError):
        calc.calculate(a,b,operator)

