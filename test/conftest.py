import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture
def driver():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window()
    yield browser
    browser.quit()
