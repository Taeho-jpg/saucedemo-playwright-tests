import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"


@pytest.fixture(autouse=True)
def login(page):
    """Login ก่อนทุก test ใน class นี้"""
    login_page = LoginPage(page)
    login_page.login(VALID_USER, VALID_PASS)


class TestCart:

    def test_add_single_item_to_cart(self, page):
        """เพิ่มสินค้า 1 ชิ้น ควรแสดง badge เป็น 1"""
        inventory = InventoryPage(page)
        inventory.add_item_to_cart("sauce-labs-backpack")
        assert inventory.get_cart_count() == "1"

    def test_add_multiple_items_to_cart(self, page):
        """เพิ่มสินค้า 2 ชิ้น ควรแสดง badge เป็น 2"""
        inventory = InventoryPage(page)
        inventory.add_item_to_cart("sauce-labs-backpack")
        inventory.add_item_to_cart("sauce-labs-bike-light")
        assert inventory.get_cart_count() == "2"

    def test_cart_shows_correct_item_count(self, page):
        """ตะกร้าควรแสดงจำนวนสินค้าที่ถูกต้อง"""
        inventory = InventoryPage(page)
        inventory.add_item_to_cart("sauce-labs-backpack")
        inventory.add_item_to_cart("sauce-labs-fleece-jacket")
        inventory.go_to_cart()
        cart = CartPage(page)
        assert cart.get_item_count() == 2

    def test_continue_shopping_returns_to_inventory(self, page):
        """กด Continue Shopping ควรกลับไปหน้า inventory"""
        inventory = InventoryPage(page)
        inventory.go_to_cart()
        cart = CartPage(page)
        cart.continue_shopping()
        assert page.url == "https://www.saucedemo.com/inventory.html"

    def test_remove_item_from_cart(self, page):
        """เพิ่มสินค้าแล้วลบออก ตะกร้าควรว่าง"""
        inventory = InventoryPage(page)
        inventory.add_item_to_cart("sauce-labs-backpack")
        inventory.go_to_cart()
        cart = CartPage(page)
        cart.remove_item("sauce-labs-backpack")
        assert cart.get_item_count() == 0

    def test_cart_empty_on_fresh_login(self, page):
        """Login ใหม่ ตะกร้าควรว่างเปล่า"""
        inventory = InventoryPage(page)
        assert inventory.cart_badge.count() == 0

    def test_checkout_button_disabled_when_cart_empty(self, page):
        """กด checkout ตอนตะกร้าว่าง ควรไม่ให้ผ่าน"""
        inventory = InventoryPage(page)
        inventory.go_to_cart()
        cart = CartPage(page)
        cart.proceed_to_checkout()
        assert page.url == "https://www.saucedemo.com/checkout-step-one.html"
