from selenium.webdriver.common.by import By


class ServicesPage:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element_by_css_selector("h1.heading-title span")
    heading_title = (By.CSS_SELECTOR, "h1.heading-title span")

    first_name_input = (By.ID, "firstname-d7d5d815-6d59-4668-9b17-7857a77a743e")
    last_name_input = (By.ID, "lastname-d7d5d815-6d59-4668-9b17-7857a77a743e")
    email_input = (By.ID, "email-d7d5d815-6d59-4668-9b17-7857a77a743e")
    phone_number_input = (By.ID, "phone-d7d5d815-6d59-4668-9b17-7857a77a743e")
    website_url_input = (By.ID, "website-d7d5d815-6d59-4668-9b17-7857a77a743e")
    message_input = (By.ID, "message-d7d5d815-6d59-4668-9b17-7857a77a743e")
    submit_contact_form_button = (By.CSS_SELECTOR, "[data-reactid='.hbspt-forms-0.5.1.0']")

    # Error labels:
    email_error_label = (By.XPATH, "//label[contains(text(),'Email must be formatted correctly.')]")
    phone_number_size_error_label = (By.XPATH, "//label[contains(text(),'Please enter a phone number')]")
    phone_number_format_error_label = (By.XPATH, "//label[contains(text(),'Must contain only numbers, +()-. and x.')]")
    complete_all_required_fields_error_message = (By.XPATH, "//label[contains(text(),'Please complete all required fields.')]")
    # error messages to assert against:
    # - email_error_message = "Email must be formatted correctly".
    # - phone_number_size_validation_message = "Please enter a phone number that's at least 7 numbers long".
    # - phone_number_format_validation_message = "Must contain only numbers, +()-. and x".
    # require_field_error_message = "Please complete this required field."
    # complete_all_required_fields_error_message = "Please complete all required fields."
    # change_email_address_error_message = "Please change your email address to continue."
    # enter_business_email_error_message = /"Please enter your business email address."/i

    def get_heading_title(self):
        return self.driver.find_element(*ServicesPage.heading_title)

    def get_contact_form(self):
        pass

    def scroll_to_contact_form(self):
        self.driver.execute_script("document.getElementById('contact').scrollIntoView();")

    def get_first_name_input(self):
        return self.driver.find_element(*ServicesPage.first_name_input)

    def get_last_name_input(self):
        return self.driver.find_element(*ServicesPage.last_name_input)

    def get_email_input(self):
        return self.driver.find_element(*ServicesPage.email_input)

    def get_phone_number_input(self):
        return self.driver.find_element(*ServicesPage.phone_number_input)

    def get_website_url_input(self):
        return self.driver.find_element(*ServicesPage.website_url_input)

    def get_message_input(self):
        return self.driver.find_element(*ServicesPage.message_input)

    def submit_contact_form(self):
        return self.driver.find_element(*ServicesPage.submit_contact_form_button).click()

    # Get error labels

    def get_email_error_label(self):
        return self.driver.find_element(*ServicesPage.email_error_label)

    def get_phone_number_size_error_label(self):
        return self.driver.find_element(*ServicesPage.phone_number_size_error_label)

    def get_phone_number_format_error_label(self):
        return self.driver.find_element(*ServicesPage.phone_number_format_error_label)

    def get_complete_all_required_fields_error_message(self):
        return self.driver.find_element(*ServicesPage.complete_all_required_fields_error_message)