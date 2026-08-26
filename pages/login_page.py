from selenium.webdriver.common.by import By

class LoginPage: 
    # 1. กำหนด Locators ไว้ที่ Constructor
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    # 2. สร้าง Methods สำหรับ Actions ต่างๆ
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)
        
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    # Method รวมสำหรับการ Login แบบรวดเร็ว
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    # เพิ่ม Method สำหรับดึงข้อความ Error ออกมาอ่าน
    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text