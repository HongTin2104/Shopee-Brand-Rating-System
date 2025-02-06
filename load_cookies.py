# # # ordinal 
# # # row shopee-search-item-result__items
# # # col-xs-2-4 shopee-search-item-result__item
# # # shopee_ic
# # # h-full duration-100 ease-sharp-motion-curve hover:shadow-hover active:shadow-active hover:-translate-y-[1px] active:translate-y-0 relative hover:z-[1] box-content relative group border border-solid hover:border-shopee-primary border border-solid border-shopee-black9
# # # contents
# # # flex flex-col bg-white cursor-pointer h-full
# # # p-2 flex-1 flex flex-col justify-between
# # # space-y-1 mb-1 flex-1 flex flex-col justify-between min-h-[4rem]
# # # line-clamp-2 break-words min-h-[2.5rem] text-sm

# # import pickle
# # import time
# # import numpy as np
# # import pandas as pd
# # import mysql.connector
# # import undetected_chromedriver as uc
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.support.ui import WebDriverWait

# # def connect_db():
# #     return mysql.connector.connect(
# #         host="localhost",
# #         user="root", 
# #         password="Ng230204!", 
# #         database="shopee_data"
# #     )

# # def save_to_mysql(data):
# #     db = connect_db()
# #     cursor = db.cursor()

# #     query = "INSERT INTO product (title) VALUES (%s)"
# #     cursor.executemany(query, [(title,) for title in data])

# #     db.commit()
# #     cursor.close()
# #     db.close()
# #     print("Dữ liệu đã lưu vào MySQL!")

# # if __name__ == '__main__':
# #     options = uc.ChromeOptions()
# #     options.add_argument("--disable-blink-features=AutomationControlled")

# #     driver = uc.Chrome(
# #         options=options,
# #         headless=False,
# #         use_subprocess=True
# #     )

# #     driver.get("https://shopee.vn/search?keyword=m%C5%A9%203%2F4")

# #     try:
# #         cookies = pickle.load(open("cookies.pkl", "rb"))
# #         for cookie in cookies:
# #             cookie['domain'] = ".shopee.vn"
# #             try:
# #                 driver.add_cookie(cookie)
# #             except Exception as e:
# #                 print(f"error add cookie: {e}")

# #         driver.get("https://shopee.vn/search?keyword=m%C5%A9%203%2F4")
# #     except Exception as e:
# #         print(f"error load cookies: {e}")

# #     wait = WebDriverWait(driver, 50)

# #     try:
# #         body = driver.find_element(By.TAG_NAME, "body")
# #         for _ in range(10):
# #             body.send_keys(Keys.PAGE_DOWN)
# #             time.sleep(2)

# #         wait.until(lambda driver: len(driver.find_elements(
# #             By.CSS_SELECTOR, ".shopee-search-item-result__item .line-clamp-2.break-words.min-h-\\[2\\.5rem\\].text-sm"
# #         )) >= 60)

# #         elems = driver.find_elements(
# #             By.CSS_SELECTOR, ".shopee-search-item-result__item .line-clamp-2.break-words.min-h-\\[2\\.5rem\\].text-sm"
# #         )

# #         titles = [elem.text.strip() for elem in elems[:60] if elem.text.strip()]
# #         df1 = pd.DataFrame({'index_': np.arange(1, len(titles) + 1), 'title': titles})
# #         print(df1)  

# #         save_to_mysql(titles)

# #     except Exception as e:
# #         print(f"error search prod: {e}")

    # time.sleep(10)
    # driver.quit()
import pickle
import time
import numpy as np
import pandas as pd
import mysql.connector
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root", 
        password="pass", 
        database="shopee_data"
    )
def save_to_mysql(data):
    db = connect_db()
    cursor = db.cursor()

    # Xóa toàn bộ dữ liệu trong bảng product (reset AUTO_INCREMENT)
    cursor.execute("TRUNCATE TABLE product")

    # Chèn dữ liệu mới
    query = "INSERT INTO product (title, price, link) VALUES (%s, %s, %s)"
    cursor.executemany(query, [(title, price, link) for title, price, link in data])

    db.commit()
    cursor.close()
    db.close()
    print("Dữ liệu đã được cập nhật vào MySQL!")


if __name__ == '__main__':
    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = uc.Chrome(
        options=options,
        headless=False,
        use_subprocess=True
    )

    driver.get("https://shopee.vn/search?keyword=m%C5%A9%203%2F4")
    wait = WebDriverWait(driver, 10)
    # load cookies
    try:
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            cookie['domain'] = ".shopee.vn"
            try:
                driver.add_cookie(cookie)
            except Exception as e:
                print(f"error add cookie: {e}")


        wait = WebDriverWait(driver, 10)

        driver.get("https://shopee.vn/search?keyword=m%C5%A9%203%2F4")
    except Exception as e:
        print(f"error load cookies: {e}")

    wait = WebDriverWait(driver, 50)

    try:
        body = driver.find_element(By.TAG_NAME, "body")
        for _ in range(10):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(2)

        wait.until(lambda driver: len(driver.find_elements(
            By.CSS_SELECTOR, ".shopee-search-item-result__item .line-clamp-2.break-words.min-h-\\[2\\.5rem\\].text-sm"
        )) >= 60)

        # get titles
        elems_title = driver.find_elements(
            By.CSS_SELECTOR, ".shopee-search-item-result__item .line-clamp-2.break-words.min-h-\\[2\\.5rem\\].text-sm"
        )
        titles = [elem.text.strip() for elem in elems_title[:60] if elem.text.strip()]

        #get price
        elems_price = driver.find_elements(
            By.CSS_SELECTOR, ".shopee-search-item-result__item .font-medium.text-base\\/5.truncate"
        )
        prices = [elem.text.strip() for elem in elems_price[:60] if elem.text.strip()]

        elems_links = driver.find_elements(
            By.CSS_SELECTOR, ".shopee-search-item-result__item .contents"
        )
        links = [elem.get_attribute('href') for elem in elems_links[:60] if elem.get_attribute('href')]
        # combine titles and prices into Dataframe
        data = list(zip(titles, prices, links))
        df1 = pd.DataFrame(data, columns=['title', 'price', 'link'])
        print(df1)

        # save to MySQL
        save_to_mysql(data)

    except Exception as e:
        print(f"error search prod: {e}")

    time.sleep(10)
    driver.quit()
