from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, Iterable
import pytest
import json

data_dir = Path(__file__).parent / "test_data"

@dataclass
class SearchTestData:
    id: str
    query: str
    expected_count: str

def load_search_test_data(ids: Optional[Iterable[str]] = None):

    with open(data_dir / "search_data.json", encoding="utf-8") as f:
        raw_data = json.load(f)["search_input"]

    if ids is not None:

        raw_data = [item for item in raw_data if item["id"] in ids]

    return [
        SearchTestData(
            id=item["id"],
            query=item["query"],
            expected_count=item["expected_results_count"],
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