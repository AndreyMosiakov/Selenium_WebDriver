from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_TITLE_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CREATE_POST_BTN = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_NEW_POST_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_SAVE_POST_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button/span""")
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")

class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        err_field = self.find_element(TestSearchLocators.LOCATOR_ERR_FIELD, time=3)
        text = err_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERR_FIELD[1]}")
        return text

    def get_title_text(self):
        title_field = self.find_element(TestSearchLocators.LOCATOR_TITLE_FIELD, time=3)
        text = title_field.text
        logging.info(f"We find text {text} in title field {TestSearchLocators.LOCATOR_TITLE_FIELD[1]}")
        return text

    def click_create_post_button(self):
        logging.info("Click create post button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()

    def create_new_post(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_NEW_POST_FIELD[1]}")
        new_post_field = self.find_element(TestSearchLocators.LOCATOR_NEW_POST_FIELD)
        new_post_field.send_keys(word)

    def click_save_post_button(self):
        logging.info("Click save new post button")
        self.find_element(TestSearchLocators.LOCATOR_SAVE_POST_BTN).click()

    def click_contact_button(self):
        logging.info("Click contact button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()


    def enter_name(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_NAME_FIELD[1]}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_NAME_FIELD)
        name_field.send_keys(word)

    def enter_email(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_EMAIL_FIELD[1]}")
        email_field = self.find_element(TestSearchLocators.LOCATOR_EMAIL_FIELD)
        email_field.send_keys(word)

    def click_contact_us_button(self):
        logging.info("Click Contact US button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()


