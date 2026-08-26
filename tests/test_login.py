import json
import os
from pages.login_page import LoginPage


# สร้างฟังก์ชันสำหรับอ่านไฟล์ JSON
def load_credentials():
    # หา Path ของไฟล์ JSON (อ้างอิงจากตำแหน่งโฟลเดอร์ปัจจุบัน)
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '../test_data/credentials.json')
    
    with open(file_path, 'r') as file:
        return json.load(file)
    
class TestLogin:
    def test_tc_log_01_successful_login(self, driver):
        # 1. โหลดข้อมูลจากไฟล์ credentials.json
        data = load_credentials()
        username = data["valid_user"]["username"]
        password = data["valid_user"]["password"]

        # 2. Initialize Page Object
        login_page = LoginPage(driver)

        # 3. Test Steps (ส่งตัวแปรเข้าไปแทนการพิมพ์ข้อความตรงๆ)
        login_page.login(username, password)

        # 3. Assertions (ตรวจสอบผลลัพธ์)
        assert "inventory" in driver.current_url.lower(), "Login failed: URL did not change to inventory"

    def test_tc_log_02_invalid_login(self, driver):
        # 1. โหลดข้อมูลจากไฟล์ credentials.json
        data = load_credentials()
        username = data["invalid_user"]["username"]
        password = data["invalid_user"]["password"]

        # 2. Initialize Page Object
        login_page = LoginPage(driver)

        # 3. Test Steps (ส่งตัวแปรเข้าไปแทนการพิมพ์ข้อความตรงๆ)
        login_page.login(username, password)

        # 4. Assertions (ตรวจสอบผลลัพธ์ 2 ชั้น)
        # ชั้นที่ 1: ตรวจสอบว่าระบบต้องไม่เปลี่ยนไปหน้า inventory
        assert "inventory" not in driver.current_url.lower(), "Login should have failed but succeeded"
        
        # ชั้นที่ 2: ตรวจสอบว่า Error Message แสดงผลถูกต้องหรือไม่
        expected_error = "Epic sadface: Sorry, this user has been locked out."
        actual_error = login_page.get_error_message()
        assert actual_error == expected_error, f"Expected error to be '{expected_error}', but got '{actual_error}'"