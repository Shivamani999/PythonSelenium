import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_Second(test_fixturesdemo):
    print("Hello Shiva")


@pytest.mark.skip
def test_assert():
    v = "hello"
    assert v is "hi", "This is not matching with v i.e., " + v


def test_browser(crossbrowser):
    print(crossbrowser)