from selenium.webdriver.common.by import By


class ContactPage:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element_by_id("hs-eu-confirmation-button").click()

    # self.driver.find_element_by_css_selector("h1.heading-title span")
    heading_title = (By.CSS_SELECTOR, "h1.heading-title")


    def get_heading_title(self):
        return self.driver.find_element(*ContactPage.heading_title)
