from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Khởi tạo trình duyệt Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def storeFetcher(storeLink, max_count=0):
    cnt = 0
    crawlData = []
    try:
        for idx, link in enumerate(storeLink):
            print(f"Accessing link: {link}")
            driver.get(link)
            wait = WebDriverWait(driver, 5)  # Đợi tối đa 10 giây
            page_html = driver.page_source
            soup = BeautifulSoup(page_html, 'html.parser')

            # Kiểm tra sự tồn tại của h1_tag và address_div
            h1_tag = soup.find('h1', class_="DUwDvf lfPIob")
            address_div = soup.find('div', class_="Io6YTe fontBodyMedium kR99db fdkmkc")
            print("Address div:", address_div)

            # Kiểm tra sự tồn tại của div_element
            
            try:
                div_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.t39EBf.GUrTXd")))
    # Lấy giá trị aria-label nếu phần tử có
                aria_label_value = div_element.get_attribute('aria-label') if div_element else ""
            except Exception as e:
                print(f"Error occurred while waiting for the div element: {e}")
                aria_label_value = ""  # Gán giá trị mặc định là chuỗi rỗng
            # Lấy tất cả span
            phone=""
            try:
                div_elements = driver.find_elements(By.CSS_SELECTOR, "div.Io6YTe.fontBodyMedium.kR99db.fdkmkc")
                if len(div_elements) >= 6:
        # Lấy div thứ 6 (chỉ số 5 vì chỉ số bắt đầu từ 0)
                    div_sixth = div_elements[5]
                    phone=div_elements[5]
                    print(f"Found 6th div: {div_sixth.text}")
                else:
                    phone=""
                    print("Không tìm thấy đủ 6 div với class 'Io6YTe fontBodyMedium kR99db fdkmkc'")
            except Exception as e:
                print(f"Error occurred: {e}")
            spans = soup.find_all('span', class_='notranslate')

            # Lấy đánh giá
            rating = ""
            try:
                parent_div = driver.find_element(By.CSS_SELECTOR, 'div.fontBodyMedium.dmRWX')
                div_elements = parent_div.find_elements(By.CSS_SELECTOR, 'div')

                if len(div_elements) > 1:
                    second_child_div = div_elements[1]
                    span_elements = second_child_div.find_elements(By.CSS_SELECTOR, 'span')
                    if span_elements:
                        rating = span_elements[0].text
            except Exception as e:
                print(f"Error getting rating: {e}")
                rating = "No rating"
            
                print
            # Lấy giá trị Price
            priceRange = ""
            for span in spans:
                div = span.find_next_sibling('div')
                if div:
                    print(f"Div content: {div.text}")
                    parts = div.text.split(' ', 1)
                    priceRange = parts[0]  # Lấy giá trị cho priceRange

            # Lưu dữ liệu vào objDataEachLink
            objDataEachLink = {
                "storeName": h1_tag.text.strip() if h1_tag else "No store name",
                "Address": address_div.text.strip() if address_div else "No address",
                "Price": priceRange,
                "canBeOrderAt": aria_label_value,
                "rating": rating,
                "contact":phone,
                "mapLink":link
            }

            # Thêm dữ liệu vào crawlData
            crawlData.append(objDataEachLink)
            if (max_count > 0):
                cnt += 1
                if (cnt >= max_count): break
            print(f"Data fetched for link {idx + 1}: {objDataEachLink}")
    except Exception as e:
        print("Error occurred:", e)

    finally:
        print("Closing the browser")
        driver.quit()

    print("Crawl data:")
    for data in crawlData:
        print(data)
    return crawlData

