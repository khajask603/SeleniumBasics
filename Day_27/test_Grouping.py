import pytest

class Test_Class4:

    @pytest.mark.sanity
    def test_login_By_Email(self):
        print("These is Login By Email...")
        assert 1 == 1

    @pytest.mark.sanity
    def test_login_By_Facebook(self):
        print("These is Login By FaceBook..")
        assert 1 == 1

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_By_Twitter(self):
        print("These is Login By Twitter...")
        assert 1 == 1

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Signup_By_Email(self):
        print("These is SignUp By EmailTest.....")
        assert True == True

    @pytest.mark.regression
    def test_SignUp_By_FaceBook(self):
        print("These is SignUp By FaceBookTest.....")
        assert True == True

    @pytest.mark.regression
    def test_SignUp_By_Twitter(self):
        print("These is SignUp By TwitterTest.....")
        assert True == True
