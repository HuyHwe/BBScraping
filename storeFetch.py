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


            wait = WebDriverWait(driver, 10)  # Đợi tối đa 10 giây
            page_html = driver.page_source
            soup = BeautifulSoup(page_html, 'html.parser')
            h1_tag = soup.find('h1', class_="DUwDvf lfPIob")
            address_div = soup.find('div', class_="Io6YTe fontBodyMedium kR99db fdkmkc")
            phoneOfStore = ""
            divPhones1 = soup.find_all('div', class_=['Io6YTe', 'fontBodyMedium', 'kR99db', 'fdkmkc'])
            index = 0
            if divPhones1:
                for idx, elementPhone in enumerate(divPhones1):
                    index = index + 1
                    if index == 10 or index == 9 or index == 8:
                        if (len(elementPhone.text) == 12 and elementPhone.text[1].isdigit()):
                            phoneOfStore = elementPhone.text
            else:
                print("No divPhones found.")

            
            Timeline=""
            try:
                div_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.t39EBf.GUrTXd")))
               
                aria_label_value = div_element.get_attribute('aria-label') if div_element else ""
                Timeline=aria_label_value.replace("\u202f", "")
                Timeline = Timeline.replace("Hours might differ", "")
                Timeline = Timeline.replace("Hide open hours for the week", "")
              
            except Exception as e:
                print(f"Error occurred while waiting for the div element because it not exits: {e}")
                aria_label_value = ""  

            
            phone = ""
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "AeaXub"))
            )
            divPhone = driver.find_elements(By.CLASS_NAME, "AeaXub")

           
            for div in divPhone:
               
                if div.text: 
                    phone = div.text.strip()

            spans = soup.find_all('span', class_='notranslate')

            # Lấy đánh giá
            rating = ""
            ##################
            try:
                rating = soup.select('div.fontBodyMedium.dmRWX > div.F7nice > :nth-child(1) > :nth-child(1)')[0].text
            except Exception as e:
              
                rating = "No rating"
            
            # Lấy giá trị Price
            priceRange = ""
            #################
            for span in spans:
                div = span.find_next_sibling('div')
                if div:
                   
                    parts = div.text.split(' ', 1)
                    priceRange = parts[0]  

            # Lưu dữ liệu vào objDataEachLink
            objDataEachLink = {
                "Store name": h1_tag.text.strip() if h1_tag else "No store name",
                "Address": address_div.text.strip() if address_div else "No address",
                "Price": priceRange,
                "Open Time": Timeline,
                "Rating": rating,
                "Contact": phoneOfStore,
                "MapLink": link
            }

            # Thêm dữ liệu vào crawlData
            crawlData.append(objDataEachLink)
            print(f"Data fetched for link {idx + 1}: {objDataEachLink}")
            ###########################
            if (max_count > 0):
                cnt += 1
                if (cnt >= max_count): break
    except Exception as e:
        print("Error occurred:", e)

    finally:
        driver.quit()

    print("Crawl data:")
    for data in crawlData:
        print(data)
    return crawlData
           
# storeFetcher(["https://www.google.com/maps/place/M%E1%BA%B8T+Vietnamese+restaurant+%26+Vegetarian+Food+3/@21.0341334,105.8512454,17z/data=!3m1!4b1!4m6!3m5!1s0x3135ab7f21065107:0x77777fbbc86b65f4!8m2!3d21.0341334!4d105.8512454!16s%2Fg%2F11ts3_jvc3?authuser=0&hl=en&entry=ttu&g_ep=EgoyMDI0MTExMy4xIKXMDSoASAFQAw%3D%3D"])