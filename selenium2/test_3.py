from testpage import OperationsHelper
import logging
import yaml
import time
from emailReport import send_email

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
    send_email()

def test_step2(browser):
    logging.info("Test2 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["pass"])
    testpage.click_login_button()
    assert testpage.get_title_text() == "Blog"
    send_email()

def test_step3(browser):
    logging.info("Test3 starting")
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
    send_email()

# тест по проверке механики работы формы Contact Us

def test_step4(browser):
    logging.info("Test4 starting")
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
    send_email()

# Тест с использованием DDT проверяет наличие поста
# с определенным заголовком в списке постов
# пользователя, для этого выполняется get запрос по адресу
def test_step5(browser, user_title_list):
    logging.info("Test5 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["pass"])
    testpage.click_login_button()
    time.sleep(testdata["sleep_time"])
    assert testpage.get_user_title_text() in user_title_list
    logging.info("Test5 ended")
    send_email()

# Добавить в задание с REST API ещё один тест, в котором создаётся новый пост,
# а потом проверяется его наличие на сервере по полю «описание».
def test_step6(browser, user_description_list):
    logging.info("Test3 starting")
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
    testpage.enter_description(testdata["descr"])
    testpage.click_save_post_button()
    descrList = user_description_list
    time.sleep(testdata["sleep_time"])
    assert testdata["descr"] in descrList
    send_email()