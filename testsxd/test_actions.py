from playwright.sync_api import Page, expect

def test_main_actions(page: Page):

# как вариант  close = page.get_by_role("button", name="Принять")
#              if close.is_visible():
#                  accept.click()
    page.locator("button:has-text('Принять')").click()

    page.get_by_test_id("search__input").fill("python")
    page.keyboard.press("Enter")


    expect(page.get_by_text("Результаты поиска «python»")).to_be_visible(timeout=25000)
    page.locator("xpath=//*[@aria-description='Книги, которые можно читать без ограничений с активной Литрес: Подпиской']").dblclick()
    page.locator("xpath=//*[@aria-description='Книги, которые можно взять по Литрес: Абонементу']").click()

# баг: page.locator("xpath=//*[@id='languages-ru']").click(force=True)
    page.check("label[for='languages-ru']")

    page.screenshot(path="screenshots/Swither.png")
    page.pause()

