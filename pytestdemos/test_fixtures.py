import pytest

from pytestdemos.BaseClass import BaseClass


@pytest.mark.usefixtures("dataload")
class Test(BaseClass):

    def test_demo(self):
        print("I will be executed in btw setup and teardown functions")

    def test_scddemo(self, dataload):
        log = self.getlogger()
        log.info(dataload[2])
        log.info(dataload[0])
