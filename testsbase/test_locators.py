from playwright.sync_api import Page, expect
import pytest

def test_locator_role(page: Page):

    page.get_by_role("link", name="Летние истории на любой вкус").click()
    expect(page).to_have_title("Летние истории на любой вкус – подборка книг – Литрес")

    page.get_by_role("button", name="Найти").click()
    expect(page.get_by_text("татьяна устинова")).to_be_visible()


def test_locator_placeholder(page: Page):


    page.get_by_placeholder("Искать на Литрес").fill("Иммануил Кант")
    page.keyboard.press("Enter")
    expect(page.get_by_text("Результаты поиска «Иммануил Кант»")).to_be_visible()


def test_locator_datatestid(page: Page):


    page.get_by_test_id("basketTabIcon").click()
    expect(page.get_by_text("Книга в подарок")).to_be_visible()


def test_locator_alttext(page: Page):


    page.get_by_alt_text("Логотип Литрес").click()
    expect(page).to_have_url("https://www.litres.ru/")


def test_locator_xpath(page: Page):

    expect(page.locator("xpath=//a[@title='YouTube']")).to_be_visible()







