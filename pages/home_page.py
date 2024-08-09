
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    MODAL_REJECT_LINK = (By.ID, "sp-cc-rejectall-link")

    def enter_search_term(self, term):
        search_box = self.wait_for_element(*self.SEARCH_BOX)
        search_box.send_keys(term)
        search_box.submit()

    def close_modal(self):
        try:
            self.click_element(*self.MODAL_REJECT_LINK)
        except:
            print("Modal veya pop-up bulunamadı veya kapatılamadı.")
