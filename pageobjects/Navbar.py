from selenium.webdriver.common.by import By


class Navbar:

    def __init__(self, driver):
        self.driver = driver

    work_tab = (By.XPATH, "//a[contains(text(),'Work')]")
    clients_tab = (By.XPATH, "//a[contains(text(),'Clients')]")
    services_tab = (By.CSS_SELECTOR, ".mega-menu-grid.mega-menu-item-19456:nth-child(3) > a.mega-menu-link")
    blog_tab = (By.XPATH, "//a[contains(text(),'Blog')]")
    about_tab = (By.XPATH, "//a[contains(text(),'About')]")
    contact_tab = (By.XPATH, "//a[contains(text(),'Contact')]")
    services_sub_menu = (By.CSS_SELECTOR, ".mega-sub-menu")
    open_nav_button = (By.CSS_SELECTOR, ".pp-advanced-menu-mobile-toggle.hamburger")
    close_nav_button = (By.CSS_SELECTOR, ".pp-menu-close-btn")
    mobile_menu_div = (By.CSS_SELECTOR, ".pp-off-canvas-menu.pp-menu-right")

    def hover_services_tab(self):
        pass

    def click_work_tab(self):
        return self.driver.find_element(*Navbar.work_tab).click()

    def click_clients_tab(self):
        return self.driver.find_element(*Navbar.clients_tab).click()

    def get_services_tab(self):
        return self.driver.find_element(*Navbar.services_tab)

    def click_blog_tab(self):
        return self.driver.find_element(*Navbar.blog_tab).click()

    def click_about_us_tab(self):
        return self.driver.find_element(*Navbar.about_tab).click()

    def click_contact_tab(self):
        return self.driver.find_element(*Navbar.contact_tab).click()

    def get_services_submenu(self):
        return self.driver.find_element(*Navbar.services_sub_menu)

    def click_open_nav_button(self):
        return self.driver.find_element(*Navbar.open_nav_button).click()

    def click_close_nav_button(self):
        return self.driver.find_element(*Navbar.close_nav_button).click()

    def get_mobile_nav_menu_div(self):
        return self.driver.find_element(*Navbar.mobile_menu_div)
