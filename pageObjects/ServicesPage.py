from selenium.webdriver.common.by import By


class ServicesPage:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element_by_css_selector("h1.heading-title span")
    heading_title = (By.CSS_SELECTOR, "h1.heading-title span")

    # first_name_input =
    # last_name_input =
    # email_input =
    # phone_number_input =
    # website_url_input =
    # message_input =
    # submit_contact_form_button =

    def get_heading_title(self):
        return self.driver.find_element(*ServicesPage.heading_title)

    def get_contact_form(self):
        pass

    def scroll_to_contact_form(self):
        pass

    def fill_contact_form(self):
        pass

    def submit_contact_form(self):
        pass
