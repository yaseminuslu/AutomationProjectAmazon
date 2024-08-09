import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class SearchResultsPage(BasePage):
    SECOND_PAGE_LINK = (By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[66]/div/div/span/a[1]')
    PRODUCT_ITEMS = (By.CSS_SELECTOR, 'div.s-main-slot div.s-result-item')

    def go_to_second_page(self):
        try:
            second_page_link = self.wait_for_element(*self.SECOND_PAGE_LINK)

            self.driver.execute_script("window.scrollBy(0, 8500);")
            time.sleep(2)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", second_page_link)
            self.driver.execute_script("arguments[0].click();", second_page_link)

            WebDriverWait(self.driver, 20).until(
                EC.url_contains("page=2")
            )
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
            raise

    def get_products(self):
            return self.driver.find_elements(*self.PRODUCT_ITEMS)


