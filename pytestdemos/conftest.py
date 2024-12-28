import pytest


@pytest.fixture(scope="class")
def test_fixturesdemo():
    print("I'm first")
    yield
    print("I'm last")


@pytest.fixture()
def dataload():
    print("this is dataload")
    return ["Shivamani", "Konam", "Shivasuriyakonam@gmail.com"]


@pytest.fixture(params=[("chrome", "firefox"), "safari", "edge"])
def crossbrowser(request):
    return request.param
