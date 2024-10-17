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

    time.sleep(5)
    while (True):
        firstBox = driver.find_element(By.CSS_SELECTOR, "#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div:nth-child(3) > div > a")
        if (firstBox != None): break
        print("see no")
        time.sleep(5)
    print("ok")
    curIndex = 3
    while (True):
        curIndex += 2
        curBox = driver.find_element(By.CSS_SELECTOR, f'#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div:nth-child({curIndex}) > div > a')
        driver.execute_script("arguments[0].scrollIntoView()", curBox)
        if (curBox == None): print("no box")
        time.sleep(0.2)
    
finally: 
    input("Press Enter to close the browser...")  
    driver.quit()

    #QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd.QjC7t > div:nth-child(78) > div > div