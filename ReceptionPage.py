from BaseApp import BasePage
from GratitudeMessage import GratitudeMessagePage
from selenium.webdriver.common.by import By


class ReceptionLocators:
    LOCATOR_GRATITUDE = (By.CSS_SELECTOR, "a[href$='messageType=Gratitude']")


class ReceptionPage(BasePage):
    def write_gratitude(self):
        self.find_element(ReceptionLocators.LOCATOR_GRATITUDE).click()
        return GratitudeMessagePage(self.driver)