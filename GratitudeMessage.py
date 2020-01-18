from BaseApp import BasePage
from MenuPage import MenuPage
from selenium.webdriver.common.by import By


class GratitudeMessageLocators:
    LOCATOR_MESSAGE_AREA = (By.ID, "MessageBody")
    LOCATOR_AGREEMENT_FLAG = (By.ID, "_agreementFlag")
    LOCATOR_CHECKED_AGREEMENT_FLAG = (By.CSS_SELECTOR, "input.valid[id = '_agreementFlag']")
    LOCATOR_BURGER_BUTTON = (By.CSS_SELECTOR, "span.burger")


class GratitudeMessagePage(BasePage):
    def enter_message(self, message):
        message_area = self.find_element(GratitudeMessageLocators.LOCATOR_MESSAGE_AREA)
        message_area.click()
        message_area.send_keys(message)
        return message_area

    def check_agreement_flag(self):
        agreement_flag = self.find_element(GratitudeMessageLocators.LOCATOR_AGREEMENT_FLAG)
        if not agreement_flag.is_selected():
            agreement_flag.click()
            checked_agreement = self.find_element(GratitudeMessageLocators.LOCATOR_CHECKED_AGREEMENT_FLAG)
        return checked_agreement

    def open_menu(self):
        self.find_element(GratitudeMessageLocators.LOCATOR_BURGER_BUTTON).click()
        return MenuPage(self.driver)
