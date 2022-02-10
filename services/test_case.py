import pytest

from KDT_Selenium_Python.services.excuter import Excuter

a = Excuter().runner("chrome")

print(len(a))
class Test_Case:
    @pytest.mark.parametrize("rs", a)
    def test(self, rs):
        print(f"{rs['tc'].title}: {rs['result']}")
        if False in rs["result"]:
            result = False
        else:
            result = True
        assert result is True

if __name__ == '__main__':
    pytest.main(["-vs", "./test_case.py::Test_Case", "--alluredir=../temps/"])

