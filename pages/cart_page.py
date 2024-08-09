
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ICON = (By.ID, 'nav-cart')
    SUBTOTAL_AMOUNT = (By.ID, 'sc-subtotal-amount-activecart')
    LOGO = (By.ID, 'nav-logo-sprites')

    def go_to_cart(self):
        self.click_element(*self.CART_ICON)

    def return_to_home(self):
        self.click_element(*self.LOGO)
