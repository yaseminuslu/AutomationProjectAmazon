from tests.base_test import BaseTest
from tests.shopping_flow import ShoppingFlow


class TestAmazon(BaseTest):
    def test_amazon_shopping(self):
        shopping_flow = ShoppingFlow(self.driver)
        try:
            shopping_flow.perform_shopping()
        except AssertionError as e:
            self.fail(f"Test başarısız: {e}")
