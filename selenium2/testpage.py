from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send{word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element{locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get test from {element_name}")
            return None
        logging.debug(f"We find {text} in field {element_name}")
        return text

    # ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="pass form")

    def enter_description(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_DESCRIPTION_FIELD"], word,
                                   description="description form")

    def create_new_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_NEW_POST_FIELD"], word, description="new post form")

    def enter_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_NAME_FIELD"], word, description="name form")

    def enter_email(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_EMAIL_FIELD"], word, description="email form")

    # CLICK
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login")

    def click_create_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_POST_BTN"], description="create new post")

    def click_save_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_POST_BTN"], description="save new post")

    def click_contact_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description="Click contact button")

    def click_contact_us_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_US_BTN"], description="Click Contact US button")

    # GET
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERR_FIELD"], description="error field")

    def get_title_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_TITLE_FIELD"], description="title field")

    def get_profile_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_USER_PROFILE_NAME"],
                                          description="user profile name")

    def get_user_title_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_USER_TITLE_FIELD"],
                                          description="user title text")

    def get_user_description_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_DESCRIPTION_FIELD"],
                                          description="user description text")