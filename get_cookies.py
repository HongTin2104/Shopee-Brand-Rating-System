# file nay de lay cookies thu cong va tranh bi dinh anti bot tracking 


import pickle
import undetected_chromedriver as uc

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
    
    try:
        # Mở trang chủ Shopee (hoặc để trống cho người dùng tự nhập)
        driver.get("https://shopee.vn")
        
        # Thông báo cho người dùng
        print("Hãy thực hiện các thao tác thủ công trên trình duyệt...")
        print("Sau khi hoàn tất (ví dụ: đăng nhập xong), QUAY LẠI ĐÂY và nhấn Enter để lưu cookies.")
        
        # Dừng chương trình chờ người dùng nhấn Enter
        input()
        
        # Lấy và lưu cookies
        cookies = driver.get_cookies()
        pickle.dump(cookies, open("cookies.pkl", "wb"))
        print(f"Đã lưu {len(cookies)} cookies vào file cookies.pkl")

    finally:
        # Đảm bảo trình duyệt luôn được đóng
        driver.quit()