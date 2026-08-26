import pytest
from selenium import webdriver

# ใช้ @pytest.fixture เพื่อประกาศว่านี่คือฟังก์ชันสำหรับ Setup / Teardown
@pytest.fixture()
def driver():
    # ---------- ส่วน Setup (ก่อนเริ่มเทสต์) ----------
    print("\n[Setup] เปิดเบราว์เซอร์ Chrome...")
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    # ส่งตัวแปร driver ไปให้ Test Case ใช้งาน
    yield driver 
    
    # ---------- ส่วน Teardown (หลังเทสต์เสร็จ) ----------
    print("\n[Teardown] ปิดเบราว์เซอร์...")
    driver.quit()

def pytest_html_report_title(report):
    report.title = "UI Automation Test Report - SauceDemo (Portfolio)"