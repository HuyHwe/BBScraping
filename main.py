from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    searchKeyword = "Văn quán"
    driver.get("https://www.google.com/maps")
    search_box = driver.find_element(By.ID, "searchboxinput")
    search_box.send_keys(searchKeyword + Keys.ENTER)
    driver.implicitly_wait(10)
    time.sleep(5)

    print(driver.title)
    for i in range(len(searchKeyword)):
        search_box.send_keys(Keys.BACK_SPACE)
    search_box.send_keys("bún bò" + Keys.ENTER)
finally: 
    input("Press Enter to close the browser...")  
    driver.quit()