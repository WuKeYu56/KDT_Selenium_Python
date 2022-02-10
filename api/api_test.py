import pytest

from KDT_Selenium_Python.api.do_request import DoRequests
from KDT_Selenium_Python.api.parseXls import ParseXls


class TestCase:
    def setup(self):
        pass

    @pytest.mark.parametrize("tc", ParseXls("./data/case3.xls").prepare_tc())
    def test1(self, tc):
        act = DoRequests().get_act(tc["precondition"], tc["method"], tc["url"], tc["param"], tc["accept_type"])
        expect = tc["expect"]
        if tc["accept_type"] == "json":
            assert act.get(expect[0]) == expect[1]
        if tc["accept_type"] == "text":
            assert expect in act


if __name__ == '__main__':
    pytest.main(["-vs", "./api_test.py::TestCase::test1", "--alluredir=./temps/"])