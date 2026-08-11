from playwright.sync_api import Page, expect
from urllib.parse import quote_plus

def test_main_actions(page, home, results):

    page.locator("button:has-text('Принять')").click()

    query = "python"
    home.search(query, True)
    expect(page).to_have_url(f"https://www.litres.ru/search/?q={query}")

    results.apply_ru_filter()
    expect(results.ru_chip).to_be_visible()

    page.screenshot(path="screenshots/Swither.png")


def test_waiting(page, home, results):

    page.locator("button:has-text('Принять')").click()

    query = "Фридрих Ницше"
    home.search(query, True)
    expect(page).to_have_url(f"https://www.litres.ru/search/?q={quote_plus(query)}")

    expect(results.results_title).to_contain_text(query)
    expect(results.books).to_have_count(24, timeout=7000)

