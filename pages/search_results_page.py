from playwright.sync_api import Locator
from pages.base_page import BasePage

class SearchResultsPage(BasePage):

    # Локаторы

    @property
    def results_title(self) -> Locator:

        return self.page.get_by_text("Результаты поиска")

    @property
    def books(self) -> Locator:

        return self.page.get_by_test_id("art__wrapper")

    @property
    def ru_filter(self) -> Locator:

        return self.page.locator("label[for='languages-ru']")

    @property
    def ru_chip(self) -> Locator:

        return self.page.locator("[data-testid='chip-content']:has-text('Русский')")

    # Действия

    def apply_ru_filter(self) -> None:
        self.ru_filter.check()