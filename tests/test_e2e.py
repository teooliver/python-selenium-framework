import pytest
import time

from pageobjects.Blog import BlogPage
from pageobjects.ContactPage import ContactPage
from pageobjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from testdata.BlogPageData import BlogPageData


class EndToEnd(BaseClass):

    @pytest.mark.skip(reason="not need anymore")
    def test_e2e(self):
        homepage = HomePage(self.driver)
        blogpage = BlogPage(self.driver)


        self.driver.get("https://www.rixxo.com/")

        assert homepage.get_page_title() == "Rixxo | B2B ECommerce & Marketing Experts"
        assert homepage.get_current_url() == "https://www.rixxo.com/"
        homepage.confirm_eu_cookie().click()
        title = homepage.get_heading_title().text
        assert "rixxo" in title
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)

        self.driver.get("https://www.rixxo.com/clients/")
        assert self.driver.current_url == "https://www.rixxo.com/clients/"

        self.driver.get("https://www.rixxo.com/services/")
        assert self.driver.current_url == "https://www.rixxo.com/services/"
        services_menu = self.driver.find_element_by_id("mega-menu-item-19456")
        print(services_menu.text)
        self.action.move_to_element(services_menu).pause(5).perform()
        # time.sleep(30)

        # Email label not working on firefox and safari (/blog)
        self.driver.get("https://www.rixxo.com/blog/")
        assert self.driver.current_url == "https://www.rixxo.com/blog/"

        blogpage.get_email_input().send_keys("test@test.com")
        time.sleep(4)
        self.driver.get("https://www.rixxo.com/about/")
        assert self.driver.current_url == "https://www.rixxo.com/about/"

        # input labels dont work on firefox
        self.driver.get("https://www.rixxo.com/contact/")
        assert self.driver.current_url == "https://www.rixxo.com/contact/"

        title = self.driver.find_element_by_css_selector("h1.heading-title span").text
        assert "Contact" in title

        self.driver.back()
        assert self.driver.current_url == "https://www.rixxo.com/about/"
        # driver.minimize_window()
        self.driver.refresh()



    def test_subscribe_blog(self, get_data):
        log = self.get_logger()
        # self.driver.set_window_size(480, 320)
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

    @pytest.fixture(params=BlogPageData.test_blog_page_data)
    def get_data(self, request):
        return request.param
