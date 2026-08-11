from playwright.sync_api import Page
import pytest

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


@pytest.fixture(autouse=True)
def open_litres(page: Page):
    page.goto("https://www.litres.ru/")

@pytest.fixture
def home(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture
def results(page: Page) -> SearchResultsPage:
    return SearchResultsPage(page)