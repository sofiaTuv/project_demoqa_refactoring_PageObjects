import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://demoqa.com'
    yield
    browser.quit()