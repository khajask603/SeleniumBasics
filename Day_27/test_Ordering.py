import pytest


class Test_Class2:

    @pytest.mark.third
    def test_MethodC(self):
        print("Running method C.. ")

    @pytest.mark.fourth
    def test_MethodD(self):
        print("Running method D.. ")

    @pytest.mark.first
    def test_MethodA(self):
        print("Running method A.. ")

    @pytest.mark.fifth
    def test_MethodF(self):
        print("Running method F.. ")

    @pytest.mark.second
    def test_MethodB(self):
        print("Running method B.. ")
