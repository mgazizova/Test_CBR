from BaseApp import BasePage
from CBR import CBRPage
from selenium.webdriver.common.by import By


class GoogleSearchResultLocators:
    LOCATOR_CBR_SITE = (By.CSS_SELECTOR, "a[href ^= 'http://www.cbr.ru']")


class GoogleSearchResultPage(BasePage):
    def select_cbr_site(self):
        self.find_element(GoogleSearchResultLocators.LOCATOR_CBR_SITE).click()
        return CBRPage(self.driver)
