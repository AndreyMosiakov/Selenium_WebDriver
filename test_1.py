import yaml
from module import Site
import time


with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

# site = Site(testdata["address"])


def test_step1(site, log_xpath, pass_xpath, btn_xpath, result_code_xpath):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys("test")
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys("test")
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    err_label = site.find_element("xpath", result_code_xpath)
    assert err_label.text == "401"


def test_step2(site, log_xpath, pass_xpath, btn_xpath,result_auth):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys(testdata ["login"])
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys(testdata ["pass"])
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    auth_label = site.find_element("xpath", result_auth)
    assert auth_label.text == "Blog"



def test_step3(site, log_xpath, pass_xpath, btn_xpath, btncp_xpath, title_post_xpath, btn_save_xpath, result_new_post):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys(testdata ["login"])
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys(testdata["pass"])
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    btncp = site.find_element("xpath", btncp_xpath)
    btncp.click()
    time.sleep(testdata["sleep_time"])
    input3 = site.find_element("xpath", title_post_xpath)
    input3.send_keys(testdata["new_post"])
    time.sleep(testdata["sleep_time"])
    btn_save = site.find_element("xpath", btn_save_xpath)
    btn_save.click()
    time.sleep(testdata["sleep_time"])
    new_post_label = site.find_element("xpath", result_new_post)
    assert new_post_label.text == (testdata["new_post"])







# login > div.submit.svelte-uwkxn9 > button > span


# css_selector = "span.mdc-text-field__ripple"
# print(site.get_element_property("css", css_selector, "height"))
#
# xpath_selector = '//*[@id="login"]/div[3]/button/div'
# print(site.get_element_property("xpath", xpath_selector, "color"))
