import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"


class TestLogin:

    def test_login_success(self, page):
        """Login ด้วย credential ถูกต้อง ควรเข้าหน้า inventory ได้"""
        login = LoginPage(page)
        login.login(VALID_USER, VALID_PASS)
        inventory = InventoryPage(page)
        assert inventory.title.inner_text() == "Products"

    def test_login_wrong_password(self, page):
        """Login ด้วย password ผิด ควรแสดง error message"""
        login = LoginPage(page)
        login.login(VALID_USER, "wrong_password")
        assert "Username and password do not match" in login.get_error_message()

    def test_login_wrong_username(self, page):
        """Login ด้วย username ผิด ควรแสดง error message"""
        login = LoginPage(page)
        login.login("wrong_user", VALID_PASS)
        assert "Username and password do not match" in login.get_error_message()

    def test_login_empty_username(self, page):
        """Login โดยไม่กรอก username ควรแสดง error"""
        login = LoginPage(page)
        login.login("", VALID_PASS)
        assert "Username is required" in login.get_error_message()

    def test_login_empty_password(self, page):
        """Login โดยไม่กรอก password ควรแสดง error"""
        login = LoginPage(page)
        login.login(VALID_USER, "")
        assert "Password is required" in login.get_error_message()

    def test_login_locked_user(self, page):
        """Login ด้วย locked_out_user ควรแสดง error account ถูกล็อก"""
        login = LoginPage(page)
        login.login("locked_out_user", VALID_PASS)
        assert "locked out" in login.get_error_message()

    def test_login_sql_injection(self, page):
        """ใส่ SQL injection ใน username ไม่ควรเข้าระบบได้"""
        login = LoginPage(page)
        login.login("' OR '1'='1", VALID_PASS)
        assert "Username and password do not match" in login.get_error_message()

    def test_login_special_characters(self, page):
        """ใส่ special characters ใน username ไม่ควรเข้าระบบได้"""
        login = LoginPage(page)
        login.login("!@#$%^&*()", VALID_PASS)
        assert "Username and password do not match" in login.get_error_message()

    def test_login_whitespace_username(self, page):
        """ใส่แค่ space ใน username ควรแสดง error"""
        login = LoginPage(page)
        login.login("   ", VALID_PASS)
        assert "Username and password do not match" in login.get_error_message()

    def test_login_case_sensitive(self, page):
        """username พิมพ์ตัวใหญ่ ควร fail เพราะ case sensitive"""
        login = LoginPage(page)
        login.login("Standard_User", VALID_PASS)
        assert "Username and password do not match" in login.get_error_message()
