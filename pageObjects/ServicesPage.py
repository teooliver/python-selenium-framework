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

    def get_heading_title(self):
        return self.driver.find_element(*ServicesPage.heading_title)

    def get_contact_form(self):
        pass

    def scroll_to_contact_form(self):
        self.driver.execute_script("document.getElementById('contact').scrollIntoView();")

    def fill_contact_form(self):
        pass

    def submit_contact_form(self):
        print("click click click")
        return self.driver.find_element(*ServicesPage.submit_contact_form_button).click()

