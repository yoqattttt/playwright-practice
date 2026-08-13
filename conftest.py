from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, Iterable
import pytest
import json
import allure

data_dir = Path(__file__).parent / "test_data"

@dataclass
class SearchTestData:
    id: str
    query: str
    expected_count: str
    description: str

def load_search_test_data(selected_ids: Optional[Iterable[str]] = None):

    with open(data_dir / "search_data.json", encoding="utf-8") as f:
        raw_data = json.load(f)["search_input"]

    if selected_ids is not None:

        raw_data = [item for item in raw_data if item["id"] in selected_ids]

    return [
        SearchTestData(
            id=item["id"],
            query=item["query"],
            expected_count=item["expected_results_count"],
            description=item["description"]
        )
        for item in raw_data
    ]


@pytest.fixture(autouse=True)
def open_litres(page: Page):
    page.goto("https://www.litres.ru/")

@pytest.fixture
def home(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture
def results(page: Page) -> SearchResultsPage:
    return SearchResultsPage(page)

@pytest.fixture(autouse=True)
def screen_on_fail(page, request):
    yield

    if request.node.rep_call.failed:
        screenshot = page.screenshot(full_page=True)
        allure.attach(
            screenshot,
            name="Screenshot on failure",
            attachment_type=allure.attachment_type.PNG
        )