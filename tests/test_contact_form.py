import time
import pytest
from utilities.BaseClass import BaseClass
from pageobjects.ServicesPage import ServicesPage
from testdata.ContactFormData import ContactFormData


class ContactForm(BaseClass):
    def test_services_page_contact_form(self, get_contact_form_data):
        log = self.get_logger()
        self.driver.get("https://www.rixxo.com/services/")
        servicespage = ServicesPage(self.driver)
        servicespage.scroll_to_contact_form()
        time.sleep(2)

        log.info("Data: " + get_contact_form_data["type"])
        servicespage.get_first_name_input().send_keys(get_contact_form_data["first_name"])
        servicespage.get_last_name_input().send_keys(get_contact_form_data["last_name"])
        servicespage.get_email_input().send_keys(get_contact_form_data["email"])
        servicespage.get_phone_number_input().send_keys(get_contact_form_data["phone_number"])
        servicespage.get_website_url_input().send_keys(get_contact_form_data["website_url"])
        servicespage.get_message_input().send_keys(get_contact_form_data["message"])

        servicespage.submit_contact_form()
        time.sleep(2)

        if get_contact_form_data["type"] == "good":
            # assert successs message present
            pass
        if get_contact_form_data["type"] == "empty":
            assert servicespage.get_complete_all_required_fields_error_message().is_displayed()

        if get_contact_form_data["type"] == "bad":
            # assert errors messages are visible/displayed
            assert servicespage.get_email_error_label().is_displayed()
            assert servicespage.get_phone_number_format_error_label().is_displayed()
            assert servicespage.get_phone_number_size_error_label().is_displayed()
        time.sleep(3)

    @pytest.fixture(params=ContactFormData.test_contact_form_data)
    def get_contact_form_data(self, request):
        return request.param
