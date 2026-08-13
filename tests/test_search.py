from idlelib import query
import pytest
import allure
from playwright.sync_api import expect
from conftest import load_search_test_data


@pytest.mark.parametrize("td", load_search_test_data(selected_ids=["python_books", "game_of_thrones"]), ids = lambda td: td.id)
def test_filters(home, results, td):
    allure.dynamic.title(f"Поиск книги {query}")
    home.accept_cookies()
    home.search(td.query, True)
    results.apply_ru_filter()
    expect(results.ru_chip).to_be_visible()


@pytest.mark.parametrize("td", load_search_test_data(selected_ids=["harlan_ellison", "stephen_king"]), ids = lambda td: td.id)
def test_results_count(home, results, td):
    allure.dynamic.title(td.description)
    home.accept_cookies()
    home.search(td.query, True)
    expect(results.results_title).to_contain_text(td.query, timeout=8000)
    expect(results.books).to_have_count(td.expected_count, timeout=8000)
