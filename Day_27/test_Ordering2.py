import pytest


class Test_Class2:

    @pytest.mark.run(order=3)
    def test_MethodC(self):
        print("Running method C3.. ")

    @pytest.mark.run(order=4)
    def test_MethodD(self):
        print("Running method D4.. ")

    @pytest.mark.run(order=1)
    def test_MethodA(self):
        print("Running method A1.. ")

    @pytest.mark.run(order=5)
    def test_MethodF(self):
        print("Running method F5.. ")

    @pytest.mark.run(order=2)
    def test_MethodB(self):
        print("Running method B2.. ")
