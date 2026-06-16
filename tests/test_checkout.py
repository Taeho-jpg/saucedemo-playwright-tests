import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"


@pytest.fixture(autouse=True)
def login_and_add_item(page):
    """Login และเพิ่มสินค้าก่อนทุก test"""
    login_page = LoginPage(page)
    login_page.login(VALID_USER, VALID_PASS)
    inventory = InventoryPage(page)
    inventory.add_item_to_cart("sauce-labs-backpack")
    inventory.go_to_cart()
    cart = CartPage(page)
    cart.proceed_to_checkout()


class TestCheckout:

    def test_checkout_success(self, page):
        """กรอกข้อมูลครบถ้วน ควรสั่งซื้อสำเร็จ"""
        checkout = CheckoutPage(page)
        checkout.fill_info("Tao", "Prembupachat", "11000")
        checkout.continue_checkout()
        checkout.finish_order()
        assert checkout.get_confirmation_text() == "Thank you for your order!"

    def test_checkout_empty_firstname(self, page):
        """ไม่กรอก First Name ควรแสดง error"""
        checkout = CheckoutPage(page)
        checkout.fill_info("", "Prembupachat", "11000")
        checkout.continue_checkout()
        assert "First Name is required" in checkout.get_error_message()

    def test_checkout_empty_lastname(self, page):
        """ไม่กรอก Last Name ควรแสดง error"""
        checkout = CheckoutPage(page)
        checkout.fill_info("Tao", "", "11000")
        checkout.continue_checkout()
        assert "Last Name is required" in checkout.get_error_message()

    def test_checkout_empty_postal_code(self, page):
        """ไม่กรอก Postal Code ควรแสดง error"""
        checkout = CheckoutPage(page)
        checkout.fill_info("Tao", "Prembupachat", "")
        checkout.continue_checkout()
        assert "Postal Code is required" in checkout.get_error_message()
