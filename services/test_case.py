import pytest

from KDT_MODULE.services.excuter import Excuter


class Test_Case:
    @pytest.mark.parametrize("rs", Excuter().runner("chrome"))
    def test(self, rs):
        print(f"{rs['tc'].title}: {rs['result']}")
        if False in rs["result"]:
            result = False
        else:
            result = True
        assert result is True


if __name__ == '__main__':
    pytest.main(["-vs", "./test_case.py::Test_Case"])

