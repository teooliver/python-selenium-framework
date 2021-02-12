import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verify_link_presence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(By.LINK_TEXT, text)
        )

    def get_page_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url
