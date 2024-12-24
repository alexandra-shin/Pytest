import pytest
from pages.page_search import SearchPage
from pages.constants import *

@pytest.mark.usefixtures("driver")
class TestSearch:

    @pytest.mark.search
    def test_valid_search(self, driver):
        SearchPage(driver).go_to_search_page() \
            .search(constant_valid_id) \
            .assert_item_found()

    @pytest.mark.search
    def test_invalid_search(self, driver):  
        SearchPage(driver).go_to_search_page() \
            .search(constant_invalid_id) \
            .assert_item_not_found()
