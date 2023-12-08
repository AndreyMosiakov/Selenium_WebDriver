from testpage import OperationsHelper
import logging
import yaml
import time

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info("Test starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step2(browser):
    logging.info("Test starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["pass"])
    testpage.click_login_button()
    assert testpage.get_title_text() == "Blog"


def test_step3(browser):
    logging.info("Test starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["pass"])
    testpage.click_login_button()
    time.sleep(testdata["sleep_time"])
    testpage.click_create_post_button()
    time.sleep(testdata["sleep_time"])
    testpage.create_new_post(testdata["new_post"])
    time.sleep(testdata["sleep_time"])
    testpage.click_save_post_button()
    time.sleep(testdata["sleep_time"])
    assert testpage.get_title_text() == (testdata["new_post"])


# тест по проверке механики работы формы Contact Us

def test_step4(browser):
    logging.info("Test starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["pass"])
    testpage.click_login_button()
    time.sleep(testdata["sleep_time"])
    testpage.click_contact_button()
    testpage.enter_name(testdata["login"])
    testpage.enter_email(testdata["email"])
    testpage.click_contact_us_button()
    time.sleep(testdata["sleep_time"])
    assert testpage.is_alert() == "Form successfully submitted"
