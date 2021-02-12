import time
from pageobjects.Navbar import Navbar
from utilities.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC


class TestNavbar(BaseClass):
    def test_navigation_tabs(self):
        self.driver.get("https://www.rixxo.com")
        navbar = Navbar(self.driver)

        # work
        navbar.click_work_tab()
        time.sleep(3)
        assert self.get_current_url() == "https://www.rixxo.com/work"
        assert self.get_page_title() == "Our Work | Want To Learn More? 0117 2077504"

        # clients
        navbar.click_clients_tab()
        time.sleep(3)
        assert self.get_current_url() == "https://www.rixxo.com/clients/"
        assert self.get_page_title() == "Our Clients | Like What You See? What To Join In?"

        # services
        self.action.move_to_element(navbar.get_services_tab()).pause(8).click().perform()
        time.sleep(3)
        assert self.get_current_url() == "https://www.rixxo.com/services/"
        assert self.get_page_title() == "B2B ECommerce & Marketing Services For Strategic Growth"

        # blog
        navbar.click_blog_tab()
        time.sleep(3)
        assert self.get_current_url() == "https://www.rixxo.com/blog/"
        assert self.get_page_title() == "Blog | Rixxo | B2B Magento Marketing Specialists"

        # about
        navbar.click_about_us_tab()
        time.sleep(3)
        assert self.get_current_url() == "https://www.rixxo.com/about/"
        assert self.get_page_title() == "About Rixxo | We Are An Agency Redefining Audience Engagement"

        # contact
        navbar.click_contact_tab()
        time.sleep(3)
        assert self.get_current_url() == "https://www.rixxo.com/contact/"
        assert self.get_page_title() == "Contact Rixxo | An Agency Redefining Audience Engagement"

    # tab tests
    def test_work_tab(self):
        self.driver.get("https://www.rixxo.com")
        navbar = Navbar(self.driver)
        navbar.click_work_tab()
        time.sleep(3)
        assert self.get_current_url() == "https://www.rixxo.com/work"
        assert self.get_page_title() == "Our Work | Want To Learn More? 0117 2077504"

    def test_clients_tab(self):
        self.driver.get("https://www.rixxo.com")
        navbar = Navbar(self.driver)
        navbar.click_clients_tab()
        time.sleep(3)
        assert self.get_current_url() == "https://www.rixxo.com/clients/"
        assert self.get_page_title() == "Our Clients | Like What You See? What To Join In?"

    def test_services_tab(self):
        self.driver.get("https://www.rixxo.com")
        navbar = Navbar(self.driver)
        self.action.move_to_element(navbar.get_services_tab()).pause(6).click().perform()
        time.sleep(3)
        assert self.get_current_url() == "https://www.rixxo.com/services/"
        assert self.get_page_title() == "B2B ECommerce & Marketing Services For Strategic Growth"

    def test_services_tab_hover(self):
        self.driver.get("https://www.rixxo.com")
        navbar = Navbar(self.driver)
        self.action.move_to_element(navbar.get_services_tab()).pause(5).perform()
        navbar.get_services_submenu()
        assert (EC.visibility_of(navbar.get_services_submenu()))

    def test_blog_tab(self):
        self.driver.get("https://www.rixxo.com")
        navbar = Navbar(self.driver)
        navbar.click_blog_tab()
        time.sleep(3)
        assert self.get_current_url() == "https://www.rixxo.com/blog/"
        assert self.get_page_title() == "Blog | Rixxo | B2B Magento Marketing Specialists"

    def test_about_us_tab(self):
        self.driver.get("https://www.rixxo.com")
        navbar = Navbar(self.driver)
        navbar.click_about_us_tab()
        time.sleep(3)
        assert self.get_current_url() == "https://www.rixxo.com/about/"
        assert self.get_page_title() == "About Rixxo | We Are An Agency Redefining Audience Engagement"

    def test_contact_tab(self):
        # contact
        self.driver.get("https://www.rixxo.com")
        navbar = Navbar(self.driver)
        navbar.click_contact_tab()
        time.sleep(3)
        assert self.get_current_url() == "https://www.rixxo.com/contact/"
        assert self.get_page_title() == "Contact Rixxo | An Agency Redefining Audience Engagement"
