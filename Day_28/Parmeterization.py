import pytest

class Test_Class:

    @pytest.mark.parametrize('num1,num2',[(1,1),(7,5),(10,10),(9,8)])
    def test_Cal(self,num1,num2):
        assert num1==num2