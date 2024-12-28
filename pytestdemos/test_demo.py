# Any pytest file should be starting or ending with 'test_' or '_test'
# function names should be starting with test
# Any code should be wrapped in function
# Method names should be more meaningfull and usefull
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstassert():
    print("pytest started")


@pytest.mark.xfail
def test_secondassert():
    a = 4
    b = 6
    assert a+2 == b, "Not Matching"
