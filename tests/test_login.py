import pytest
from pages.page_login import LoginPage
from pages.constants import *

@pytest.mark.usefixtures("driver")
class TestLogin:

    @pytest.mark.login
    def test_valid_login(self, driver):
        LoginPage(driver).go_to_login_page() \
            .login(constant_valid_user['email'], constant_valid_user['password']) \
            .assert_is_logged_in()

    @pytest.mark.login
    def test_invalid_login(self, driver):
        LoginPage(driver).go_to_login_page() \
            .login(constant_invalid_user['email'], constant_invalid_user['password']) \
            .assert_is_login_failed()
