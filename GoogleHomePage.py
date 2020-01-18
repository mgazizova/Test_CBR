from BaseApp import BasePage
from GoogleSearchResultPage import GoogleSearchResultPage
from selenium.webdriver.common.by import By


class GoogleHomeLocators:
    LOCATOR_GOOGLE_SEARCH_FIELD = (By.CSS_SELECTOR, "input.gLFyf")
    LOCATOR_GOOGLE_SEARCH_BUTTON = (By.CSS_SELECTOR, "input.gNO89b")


class GoogleHomePage(BasePage):
    def enter_word(self, word):
        search_field = self.find_element(GoogleHomeLocators.LOCATOR_GOOGLE_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        search_button = self.find_element(GoogleHomeLocators.LOCATOR_GOOGLE_SEARCH_BUTTON)
        return search_button.click()

    def search(self):
        self.click_on_the_search_button()
        return GoogleSearchResultPage(self.driver)

