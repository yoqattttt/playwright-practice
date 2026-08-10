from playwright.sync_api import Page
import pytest

from pages.home_page import HomePage


@pytest.fixture(autouse=True)
def open_litres(page: Page):
    page.goto("https://www.litres.ru/")

@pytest.fixture
def home(page: Page) -> HomePage:
    return HomePage(page)