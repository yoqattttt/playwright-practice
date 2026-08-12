import pytest
from playwright.sync_api import expect

from conftest import load_search_test_data


@pytest.mark.parametrize("td", load_search_test_data(ids=["python_books", "game_of_thrones"]))
def test_filters(home, results, td):
    home.accept_cookies()
    home.search(td.query, True)
    results.apply_ru_filter()
    expect(results.ru_chip).to_be_visible()


@pytest.mark.parametrize("td", load_search_test_data(ids=["harlan_ellison", "stephen_king"]))
def test_results_count(home, results, td):
    home.accept_cookies()
    home.search(td.query, True)
    expect(results.results_title).to_contain_text(td.query)
    expect(results.books).to_have_count(td.expected_count, timeout=7000)

