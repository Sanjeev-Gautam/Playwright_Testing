import pytest
from pages.login_page import LoginPage
from util.data_reader import read_csv

data = read_csv('resource/Data.csv')


@pytest.mark.parametrize("data", data)
def test_login_with_valid_credentials(page, data):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(data["username"], data["password"])