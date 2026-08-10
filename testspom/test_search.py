from playwright.sync_api import Page, expect

def test_main_actions(page, home):

    page.locator("button:has-text('Принять')").click()

    query = "python"
    home.search(query, True)

    expect(page.get_by_text("Результаты поиска «python»")).to_be_visible(timeout=20000)
    page.locator("xpath=//*[@aria-description='Книги, которые можно читать без ограничений с активной Литрес: Подпиской']").dblclick()
    page.locator("xpath=//*[@aria-description='Книги, которые можно взять по Литрес: Абонементу']").click()

    page.check("label[for='languages-ru']")

    page.screenshot(path="screenshots/Swither.png")
    page.pause()


def test_waiting(page, home):

    query = "Фридрих Ницше"
    home.search(query)

    expect(page.get_by_text("Результаты поиска «Фридрих Ницше»")).to_be_visible(timeout=8000)
    expect(page).to_have_title("Результаты поиска по книгам: «Фридрих Ницше»")

    books = page.get_by_test_id("art__wrapper")
    expect(books).to_have_count(24, timeout=7000)

