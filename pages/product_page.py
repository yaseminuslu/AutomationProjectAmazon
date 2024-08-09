
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_TITLE = (By.ID, 'productTitle')
    ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')

    def add_product_to_cart(self):
        self.click_element(*self.ADD_TO_CART_BUTTON)
