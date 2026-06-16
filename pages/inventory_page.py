class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator(".title")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def add_item_to_cart(self, item_name: str):
        button_id = item_name.lower().replace(" ", "-")
        self.page.locator(f"#add-to-cart-{button_id}").click()

    def go_to_cart(self):
        self.cart_link.click()

    def get_cart_count(self) -> str:
        return self.cart_badge.inner_text()
