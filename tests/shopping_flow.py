from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
import time


class ShoppingFlow:
    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.product_page = ProductPage(driver)
        self.cart_page = CartPage(driver)

    def perform_shopping(self):
        self.driver.get("https://www.amazon.com.tr/")
        assert "Amazon" in self.driver.title, "Ana sayfa doğrulanamadı."

        self.home_page.enter_search_term("samsung")
        self.home_page.close_modal()
        time.sleep(2)

        self.search_results_page.go_to_second_page()
        assert "page=2" in self.driver.current_url, "2. sayfaya gidilmedi."
        time.sleep(2)

        self.select_and_handle_product()

    def select_and_handle_product(self):
        products = self.search_results_page.get_products()
        num_products = len(products)

        if num_products >= 21:
            # 5. satırın 1. ürünü
            row_length = 5
            fifth_row_first_product_index = (5 - 1) * row_length  # 5. satırın ilk ürünü

            if fifth_row_first_product_index < num_products:
                fifth_row_first_product = products[fifth_row_first_product_index]

                actions = ActionChains(self.driver)
                actions.move_to_element(fifth_row_first_product).perform()

                fifth_row_first_product.click()

                assert 'Samsung' in self.driver.title, "Ürün sayfasına gidilmedi veya başlık 'Samsung' içermiyor."

                self.product_page.add_product_to_cart()
                self.cart_page.go_to_cart()

                assert 'Alışveriş Sepeti' in self.driver.title, "Sepet sayfasına gidilmedi veya başlık 'Alışveriş Sepeti' içermiyor."

                self.cart_page.return_to_home()
                assert "Amazon" in self.driver.title, "Ana sayfaya dönülemedi."
            else:
                raise AssertionError("5. satırın 1. ürünü bulunamadı.")
        else:
            raise AssertionError("Yeterli ürün bulunamadı.")

