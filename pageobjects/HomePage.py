from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element_by_id("hs-eu-confirmation-button").click()
    eu_confirmation_button = (By.ID, "hs-eu-confirmation-button")
    # self.driver.find_element_by_css_selector("h1.heading-title span")
    heading_title = (By.CSS_SELECTOR, "h1.heading-title span")

    def confirm_eu_cookie(self):
        return self.driver.find_element(*HomePage.eu_confirmation_button)

    def get_heading_title(self):
        return self.driver.find_element(*HomePage.heading_title)