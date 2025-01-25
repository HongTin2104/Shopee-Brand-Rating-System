import pickle
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json

if __name__ == '__main__':
    # Khởi tạo trình duyệt với undetected-chromedriver
    options = uc.ChromeOptions()
    
    # Thêm các tùy chọn nếu cần (ví dụ: ẩn automation flags)
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    # Khởi động trình duyệt
    driver = uc.Chrome(
        options=options,
        headless=False,
        use_subprocess=True
    )

    # Mở trang chủ Shopee (hoặc để trống cho người dùng tự nhập)
    driver.get("https://shopee.vn")
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        cookie['domain'] = ".shopee.vn"
        
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(e)

    driver.get('https://shopee.vn/')

    time.sleep(30)
    
    with open("data.json", "w") as f:
        json.dump([], f)

def write_json(new_data, filename='data.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

driver.get('https://shopee.vn/M%C3%A1y-T%C3%ADnh-Laptop-cat.11035954')
time.sleep(60)
