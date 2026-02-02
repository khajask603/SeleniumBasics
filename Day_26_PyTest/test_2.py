import pytest

class TestClass:

    @pytest.fixture()                   #->its Called Decoratore and testng its called annotation
    def setup(self):
        print("-------LaunchingBrowser---------")
        yield               #Before it All statment will execute before everytest after these all the staments will end after testcases
        print("---------Closing Browser--------")

    def test_Login(self, setup):
        print("These is the the Login test ")

    def test_Search(self,setup):
        print("These is the the Search test ")

    def test_AdvanceSearch(self, setup):
        print("These is the the Advance Search test ")
