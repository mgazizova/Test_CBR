from BaseApp import BasePage
from selenium.webdriver.common.by import By


class AboutWarningPageLocators:
    LOCATOR_CURRENT_LOCAL = (By.CSS_SELECTOR, "li.selected")
    LOCATOR_WARNING_CONTENT = (By.ID, "content")
    LOCATOR_NOT_CURRENT_LOCAL = (By.CSS_SELECTOR, "ul.langs li:not(.selected)")


class AboutWarningPage(BasePage):
    def change_local(self):
        return self.find_element(AboutWarningPageLocators.LOCATOR_NOT_CURRENT_LOCAL).click()

    def get_warning_text(self):
        return self.find_element(AboutWarningPageLocators.LOCATOR_WARNING_CONTENT).text
