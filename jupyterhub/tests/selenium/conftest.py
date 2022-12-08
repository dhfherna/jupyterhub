import pytest
from selenium import webdriver


@pytest.fixture()
def browser(cleanup_after):
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.close()
    driver.quit()
