import pytest

class Test_Class:

    @pytest.mark.dependency()
    def test_openApp(self):
        # if ---OPEN TEST CASE FAILED i dont wanr to continue and skip
        assert True

    @pytest.mark.dependency(depends=['Test_Class::test_openApp'])
    def test_login(self):
        assert True

    @pytest.mark.dependency(depends=['Test_Class::test_login'])
    def test_Search(self):
        assert False

    @pytest.mark.dependency(depends=['Test_Class::test_login', 'Test_Class3::test_Search'])
    def test_AdvanceSearch(self):
        assert True

    @pytest.mark.dependency(depends=['Test_Class::test_login'])
    def test_logOut(self):
        assert True
