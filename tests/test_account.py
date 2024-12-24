import pytest
import random
from tests.test_login import TestLogin
from pages.page_account import AccountPage
from pages.constants import *

@pytest.mark.usefixtures("driver")
class TestAccount(TestLogin):
    random_month = random.choice(constant_months)
    random_day = str(random.randint(1, 30))
    random_year = str(random.randint(1970, 1995))

    @pytest.mark.account
    def test_edit_account(self, driver):
        self.test_valid_login(driver)
        AccountPage(driver).go_to_account_page() \
               .change_dob(self.random_month, self.random_day, self.random_year) \
               .assert_dob_is_changed(self.random_month, self.random_day, self.random_year)
        