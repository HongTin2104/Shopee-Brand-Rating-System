from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import random
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Thêm tùy chọn User-Agent để giả lập trình duyệt thực tế
chrome_options = Options()
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Điều hướng tới Shopee
    driver.get("https://shopee.vn")
    print("Đã truy cập Shopee.")

    # Chờ trang tải xong
    time.sleep(random.uniform(2, 4))  # Thời gian ngừng ngẫu nhiên để trông tự nhiên hơn

    # Di chuyển chuột để tránh bị phát hiện là bot
    actions = ActionChains(driver)
    actions.move_by_offset(10, 10).perform()
    time.sleep(random.uniform(0.5, 1))  # Chờ một chút

    # Chờ cửa sổ đăng nhập xuất hiện
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/form')))

    # Điền email vào trường nhập
    email_input = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/form/div[1]/div[1]/input')
    email_input.send_keys("hongtin2104@gmail.com")  # Nhập email
    time.sleep(random.uniform(0.5, 1.5))  # Chờ ngẫu nhiên giữa các hành động

    # Điền mật khẩu vào trường nhập
    pass_input = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/form/div[2]/div[1]/input')
    pass_input.send_keys("Hayato2104")  # Nhập mật khẩu
    time.sleep(random.uniform(0.5, 1.5))  # Chờ ngẫu nhiên giữa các hành động

    # Nhấn nút đăng nhập
    login_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/form/button')
    login_button.click()
    print("Đã nhấn nút đăng nhập.")

    # Chờ sau khi đăng nhập (đảm bảo mọi thứ được tải)
    time.sleep(random.uniform(2, 5))  # Đợi ngẫu nhiên để trông tự nhiên hơn

    # Kiểm tra xem có đăng nhập thành công không (kiểm tra tiêu đề trang)
    print(f"Tiêu đề trang sau khi đăng nhập: {driver.title}")

    # Giữ trình duyệt mở lâu hơn để giảm khả năng bị phát hiện
    time.sleep(random.uniform(100, 110))

except Exception as e:
    print(f"Có lỗi xảy ra: {e}")

finally:
    # Đóng trình duyệt
    driver.quit()

