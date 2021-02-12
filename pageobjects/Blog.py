from selenium.webdriver.common.by import By


class BlogPage:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element_by_id("hs-eu-confirmation-button").click()
    eu_confirmation_button = (By.ID, "hs-eu-confirmation-button")
    # self.driver.find_element_by_css_selector("h1.heading-title span")
    heading_title = (By.XPATH, "//span[contains(text(),'Sign up for B2B eCommerce Tips & News')]")
    email_input = (By.NAME, "email")
    subscribe_button = (By.CSS_SELECTOR, "div.actions > input.hs-button.primary.large")
    subscribe_error = (By.XPATH, "//label[contains(text(),'Please change your email address to continue.')]")



    def get_email_input(self):
        return self.driver.find_element(*BlogPage.email_input)

    def click_subscribe_btn(self):
        return self.driver.find_element(*BlogPage.subscribe_button)

    def get_subscribe_error(self):
        return self.driver.find_element(*BlogPage.subscribe_error)