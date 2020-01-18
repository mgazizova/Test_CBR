from BaseApp import BasePage
from selenium.webdriver.common.by import By
from ReceptionPage import ReceptionPage


class CBRLocators:
    LOCATOR_INTERNET_RECEPTION = (By.LINK_TEXT, "Интернет-приемная")


class CBRPage(BasePage):
    def go_to_reception(self):
        self.find_element(CBRLocators.LOCATOR_INTERNET_RECEPTION).click()
        return ReceptionPage(self.driver)

