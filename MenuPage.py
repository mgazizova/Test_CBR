from BaseApp import BasePage
from AboutWarningPage import AboutWarningPage
from selenium.webdriver.common.by import By


class MenuPageLocator:
    LOCATOR_ABOUT = (By.CSS_SELECTOR, "li.for_branch_11377")
    LOCATOR_ABOUT_WARNING = (By.CSS_SELECTOR, "li[data-catalogid='11380'")


class MenuPage(BasePage):
    def select_about(self):
        return self.find_element(MenuPageLocator.LOCATOR_ABOUT).click()

    def select_about_warning(self):
        self.select_about()
        self.find_element(MenuPageLocator.LOCATOR_ABOUT_WARNING).click()
        return AboutWarningPage(self.driver)


