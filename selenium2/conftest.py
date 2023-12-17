import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from emailReport import send_email
import requests

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


#     browser = testdata["browser"]


@pytest.fixture(scope="session")
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


#   send_email()
@pytest.fixture()
def user_title_list():
    result = requests.post(url=testdata["url"], data={"username": testdata["login"], "password": testdata["pass"]})
    token = (result.json()["token"])
    res_get = requests.get(url=testdata["url_post"], headers={"X-Auth-Token": token}, params=testdata["owner"])
    title_list = [item["title"] for item in res_get.json()["data"]]
    return title_list

@pytest.fixture()
def user_description_list():
    result = requests.post(url=testdata["url"], data={"username": testdata["login"], "password": testdata["pass"]})
    token = (result.json()["token"])
    res_get = requests.get(url=testdata["url_post"], headers={"X-Auth-Token": token}, params=testdata["owner"])
    description_list = [item["description"] for item in res_get.json()["data"]]
    return description_list
