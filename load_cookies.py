# import pickle
# import time
# import numpy as np
# import pandas as pd

# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import json

# if __name__ == '__main__':
#     # Khởi tạo trình duyệt với undetected-chromedriver
#     options = uc.ChromeOptions()

#     # Thêm các tùy chọn nếu cần (ví dụ: ẩn automation flags)
#     options.add_argument("--disable-blink-features=AutomationControlled")

#     # Khởi động trình duyệt
#     driver = uc.Chrome(
#         options=options,
#         headless=False,
#         use_subprocess=True
#     )

#     # Mở trang chủ Shopee (hoặc để trống cho người dùng tự nhập)
#     driver.get("https://shopee.vn/search?keyword=m%C5%A9%203%2F4")

#     cookies = pickle.load(open("cookies.pkl", "rb"))
#     for cookie in cookies:
#         cookie['domain'] = ".shopee.vn"

#         try:
#             driver.add_cookie(cookie)
#         except Exception as e:
#             print(e)
#     driver.get("https://shopee.vn/search?keyword=m%C5%A9%203%2F4")

#     elems = driver.find_elements(By.CSS_SELECTOR, ".line-clamp-2.break-words.min-h-\\[2\\.5rem\\].text-sm")    title = [elem.text for elem in elems]



#     df1 = pd.DataFrame(list(zip(title)), columns = ['title'])
#     df1['index_']= np.arange(1, len(df1) + 1)

#     time.sleep(60)


# source nay lay duoc nhung chi 4 cai nam tren recomend 

# import pickle
# import time
# import numpy as np
# import pandas as pd
# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# if __name__ == '__main__':
#     # Khởi tạo trình duyệt với undetected-chromedriver
#     options = uc.ChromeOptions()
#     options.add_argument("--disable-blink-features=AutLỗi khi tìm phần tử:omationControlled")

#     # Khởi động trình duyệt
#     driver = uc.Chrome(
#         options=options,
#         headless=False,
#         use_subprocess=True
#     )

#     # Mở trang Shopee
#     driver.get("https://shopee.vn/search?keyword=m%C5%A9%203%2F4")

#     # Load cookies từ file
#     try:
#         cookies = pickle.load(open("cookies.pkl", "rb"))
#         for cookie in cookies:
#             cookie['domain'] = ".shopee.vn"
#             try:
#                 driver.add_cookie(cookie)
#             except Exception as e:
#                 print(f"error add cookie: {e}")

#         driver.get("https://shopee.vn/search?keyword=m%C5%A9%203%2F4")
#     except Exception as e:
#         print(f"error load cookies: {e}")

#     try:
#         wait = WebDriverWait(driver, 10)  
#         elems = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.line-clamp-2.break-words")))

#         titles = [elem.text.strip() for elem in elems if elem.text.strip()]

#         df1 = pd.DataFrame({'index_': np.arange(1, len(titles) + 1), 'title': titles})
#         print(df1)  

#     except Exception as e:
#         print(f"error search prod: {e}")

#     time.sleep(50)
#     driver.quit()

# ordinal 
# row shopee-search-item-result__items
# col-xs-2-4 shopee-search-item-result__item
# shopee_ic
# h-full duration-100 ease-sharp-motion-curve hover:shadow-hover active:shadow-active hover:-translate-y-[1px] active:translate-y-0 relative hover:z-[1] box-content relative group border border-solid hover:border-shopee-primary border border-solid border-shopee-black9
# contents
# flex flex-col bg-white cursor-pointer h-full
# p-2 flex-1 flex flex-col justify-between
# space-y-1 mb-1 flex-1 flex flex-col justify-between min-h-[4rem]
# line-clamp-2 break-words min-h-[2.5rem] text-sm

# lay duoc 10 san pham 
# import pickle
# import time
# import numpy as np
# import pandas as pd
# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# if __name__ == '__main__':
#     options = uc.ChromeOptions()
#     options.add_argument("--disable-blink-features=AutomationControlled")

#     driver = uc.Chrome(
#         options=options,
#         headless=False,
#         use_subprocess=True
#     )

#     driver.get("https://shopee.vn/search?keyword=m%C5%A9%203%2F4")

#     try:
#         cookies = pickle.load(open("cookies.pkl", "rb"))
#         for cookie in cookies:
#             cookie['domain'] = ".shopee.vn"
#             try:
#                 driver.add_cookie(cookie)
#             except Exception as e:
#                 print(f"error add cookie: {e}")

#         driver.get("https://shopee.vn/search?keyword=m%C5%A9%203%2F4")
#     except Exception as e:
#         print(f"error load cookies: {e}")

#     wait = WebDriverWait(driver, 50)  

#     try:
#         # wait = WebDriverWait(driver, 20)  

#         elems = wait.until(EC.presence_of_all_elements_located(
#             (By.CSS_SELECTOR, ".shopee-search-item-result__item .line-clamp-2.break-words.min-h-\\[2\\.5rem\\].text-sm")
#         ))

#         titles = [elem.text.strip() for elem in elems[:60] if elem.text.strip()]

#         df1 = pd.DataFrame({'index_': np.arange(1, len(titles) + 1), 'title': titles})
#         print(df1)  

#     except Exception as e:
#         print(f"error search prod: {e}")

#     time.sleep(50)
#     driver.quit()

import pickle
import time
import numpy as np
import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':
    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = uc.Chrome(
        options=options,
        headless=False,
        use_subprocess=True
    )

    driver.get("https://shopee.vn/search?keyword=m%C5%A9%203%2F4")

    try:
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            cookie['domain'] = ".shopee.vn"
            try:
                driver.add_cookie(cookie)
            except Exception as e:
                print(f"error add cookie: {e}")

        driver.get("https://shopee.vn/search?keyword=m%C5%A9%203%2F4")
    except Exception as e:
        print(f"error load cookies: {e}")

    wait = WebDriverWait(driver, 50)  

    try:
        # 🔹 **Tạo action kéo xuống cuối trang nhiều lần**
        body = driver.find_element(By.TAG_NAME, "body")
        for _ in range(10):  # Kéo xuống 10 lần để load thêm sản phẩm
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(2)

        # 🔹 **Đợi cho đến khi đủ sản phẩm xuất hiện**
        wait.until(lambda driver: len(driver.find_elements(
            By.CSS_SELECTOR, ".shopee-search-item-result__item .line-clamp-2.break-words.min-h-\\[2\\.5rem\\].text-sm"
        )) >= 60)

        # 🔹 **Lấy danh sách sản phẩm**
        elems = driver.find_elements(
            By.CSS_SELECTOR, ".shopee-search-item-result__item .line-clamp-2.break-words.min-h-\\[2\\.5rem\\].text-sm"
        )

        titles = [elem.text.strip() for elem in elems[:60] if elem.text.strip()]
        df1 = pd.DataFrame({'index_': np.arange(1, len(titles) + 1), 'title': titles})
        print(df1)  

    except Exception as e:
        print(f"error search prod: {e}")

    time.sleep(50)
    driver.quit()
