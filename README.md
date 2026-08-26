# 🛒 SauceDemo Web UI Automation Test

Automated Testing Project สำหรับเว็บไซต์ E-commerce (SauceDemo) โปรเจกต์นี้จัดทำขึ้นเพื่อสาธิตทักษะการเขียน Web UI Automation Testing โดยใช้ **Python** และ **Selenium WebDriver** 

## 🚀 Tech Stack & Tools
* **Language:** Python 3
* **Automation Tool:** Selenium WebDriver
* **Test Framework:** Pytest
* **Reporting:** Pytest-html
* **Design Pattern:** Page Object Model (POM)

## 🎯 Key Features
1. **Page Object Model (POM):** แยก Locators และ Actions ออกจาก Test Scripts เพื่อให้โค้ดอ่านง่ายและบำรุงรักษาได้ง่าย
2. **Data-Driven Testing:** แยกข้อมูลเทสต์ (เช่น Username/Password) ไว้ในไฟล์ `credentials.json` เพื่อความปลอดภัยและง่ายต่อการปรับเปลี่ยน
3. **Automated HTML Reporting:** สร้างรายงานผลการทดสอบอัตโนมัติ พร้อมสรุปผล Pass/Fail 
4. **Centralized Setup/Teardown:** จัดการ WebDriver (เปิด-ปิด เบราว์เซอร์) ผ่านไฟล์ `conftest.py` เพื่อลดความซ้ำซ้อนของโค้ด

## 📁 Project Structure
```text
saucedemo-selenium-python/
├── pages/                  # Page Object classes (Locators & Actions)
│   ├── __init__.py
│   └── login_page.py       
├── tests/                  # Test scripts
│   ├── __init__.py
│   └── test_login.py       # Login scenarios (Happy & Negative path)
├── test_data/              # Test data files
│   └── credentials.json    
├── reports/                # Folder for HTML test reports
├── conftest.py             # Pytest configuration and WebDriver setup
├── requirements.txt        # Project dependencies
└── README.md
```

## ⚙️ How to Run the Tests (วิธีติดตั้งและรันโปรเจกต์)
1. Clone the repository
โคลนโปรเจกต์นี้ลงในเครื่องคอมพิวเตอร์ของคุณ

```bash
git clone https://github.com/pakjingjing/saucedemo-selenium-python.git
```
```bash
cd saucedemo-selenium-python
```
2. Install Dependencies
ติดตั้งเครื่องมือและไลบรารีที่จำเป็นทั้งหมดผ่านไฟล์ requirements.txt

```Bash
pip install -r requirements.txt
```

3. Execute the Tests
สร้างโฟลเดอร์สำหรับเก็บรายงาน และรันเทสต์ทั้งหมดเพื่อสร้างไฟล์ HTML

```Bash
pytest tests/ -v --html=reports/report.html --self-contained-html
```
