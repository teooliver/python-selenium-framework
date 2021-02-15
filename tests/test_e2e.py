import pytest

from pageobjects.Blog import BlogPage
from pageobjects.ContactPage import ContactPage
from pageobjects.HomePage import HomePage
from pageobjects.Navbar import Navbar
from pageobjects.ServicesPage import ServicesPage
from testdata.ContactFormData import ContactFormData
from utilities.BaseClass import BaseClass
from testdata.BlogPageData import BlogPageData
import time


class TestOne(BaseClass):

    # def test_e2e(self):
    #     homepage = HomePage(self.driver)
    #     blogpage = BlogPage(self.driver)
    #
    #
    #     self.driver.get("https://www.rixxo.com/")
    #
    #     assert homepage.get_page_title() == "Rixxo | B2B ECommerce & Marketing Experts"
    #     assert homepage.get_current_url() == "https://www.rixxo.com/"
    #     homepage.confirm_eu_cookie().click()
    #     title = homepage.get_heading_title().text
    #     assert "rixxo" in title
    #     time.sleep(2)
    #
    #     self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    #     time.sleep(2)
    #
    #     self.driver.get("https://www.rixxo.com/clients/")
    #     assert self.driver.current_url == "https://www.rixxo.com/clients/"
    #
    #     self.driver.get("https://www.rixxo.com/services/")
    #     assert self.driver.current_url == "https://www.rixxo.com/services/"
    #     services_menu = self.driver.find_element_by_id("mega-menu-item-19456")
    #     print(services_menu.text)
    #     self.action.move_to_element(services_menu).pause(5).perform()
    #     # time.sleep(30)
    #
    #     # Email label not working on firefox and safari (/blog)
    #     self.driver.get("https://www.rixxo.com/blog/")
    #     assert self.driver.current_url == "https://www.rixxo.com/blog/"
    #
    #     blogpage.get_email_input().send_keys("test@test.com")
    #     time.sleep(4)
    #     self.driver.get("https://www.rixxo.com/about/")
    #     assert self.driver.current_url == "https://www.rixxo.com/about/"
    #
    #     # input labels dont work on firefox
    #     self.driver.get("https://www.rixxo.com/contact/")
    #     assert self.driver.current_url == "https://www.rixxo.com/contact/"
    #
    #     title = self.driver.find_element_by_css_selector("h1.heading-title span").text
    #     assert "Contact" in title
    #
    #     self.driver.back()
    #     assert self.driver.current_url == "https://www.rixxo.com/about/"
    #     # driver.minimize_window()
    #     self.driver.refresh()
    #
    #

    def test_subscribe_blog(self, get_data):
        log = self.get_logger()
        self.driver.get("https://www.rixxo.com/blog/")
        blogpage = BlogPage(self.driver)
        assert self.get_current_url() == "https://www.rixxo.com/blog/"
        log.warning("using email: " + get_data["email"])
        blogpage.get_email_input().send_keys(get_data["email"])

        time.sleep(2)
        blogpage.click_subscribe_btn().click()
        # implement implicit wait()
        assert blogpage.get_subscribe_error()
        time.sleep(6)

    def test_contact_page(self):
        self.driver.get("https://www.rixxo.com/contact/")
        contactpage = ContactPage(self.driver)
        title = contactpage.get_heading_title().text
        assert "Contact" in title

    def test_services_page_contact(self, get_contact_form_data):
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
        else:
            # assert errors messages are present
            pass

        time.sleep(3)

    @pytest.fixture(params=BlogPageData.test_blog_page_data)
    def get_data(self, request):
        return request.param

    @pytest.fixture(params=ContactFormData.test_contact_form_data)
    def get_contact_form_data(self, request):
        return request.param

