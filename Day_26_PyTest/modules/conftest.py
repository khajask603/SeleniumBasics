import pytest

@pytest.fixture()
def setaup():
    print("++++++++++++LaunchingBrowser++++++++++++++")
    yield
    print("+++++++++++++Closing Browser++++++++++++++")