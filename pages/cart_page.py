class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = page.locator("#checkout")
        self.cart_items = page.locator(".cart_item")
        self.continue_shopping_button = page.locator("#continue-shopping")

    def get_item_count(self) -> int:
        return self.cart_items.count()

    def proceed_to_checkout(self):
        self.checkout_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()
