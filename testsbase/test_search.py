from playwright.sync_api import Page, expect

def test_main_actions(page: Page):

# как вариант  close = page.get_by_role("button", name="Принять")
#              if close.is_visible():
#                  close.click()
    page.locator("button:has-text('Принять')").click()

    page.get_by_test_id("search__input").fill("python")
    page.keyboard.press("Enter")


    expect(page.get_by_text("Результаты поиска «python»")).to_be_visible(timeout=20000)
    page.locator("xpath=//*[@aria-description='Книги, которые можно читать без ограничений с активной Литрес: Подпиской']").dblclick()
    page.locator("xpath=//*[@aria-description='Книги, которые можно взять по Литрес: Абонементу']").click()

# баг: page.locator("xpath=//*[@id='languages-ru']").click(force=True)
    page.check("label[for='languages-ru']")

    page.screenshot(path="screenshots/Swither.png")
    page.pause()


def test_waiting(page: Page):
    page.get_by_placeholder("Искать на Литрес").fill("Фридрих Ницше")
    page.get_by_test_id("search__button").click()

    expect(page.get_by_text("Результаты поиска «Фридрих Ницше»")).to_be_visible(timeout=8000)
    expect(page).to_have_title("Результаты поиска по книгам: «Фридрих Ницше»")

# либо __(timeout=10000)
#   result=page.locator("text=Результаты поиска «Фридрих Ницше»")
#   result.wait_for(timeout=10000)

    books = page.get_by_test_id("art__wrapper")
    expect(books).to_have_count(24, timeout=7000)

