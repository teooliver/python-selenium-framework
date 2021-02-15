import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    @staticmethod
    def get_logger():
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def get_page_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def verify_link_presence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(By.LINK_TEXT, text)
        )

