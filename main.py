from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
def getLinksByPrompt(searchArea, searchKeyword):
    storeLinks = []
    try:
        driver.get("https://www.google.com/maps")
        search_box = driver.find_element(By.ID, "searchboxinput")
        search_box.send_keys(searchArea + Keys.ENTER)
        driver.implicitly_wait(10)
        time.sleep(5)

        print(driver.title)
        for i in range(len(searchArea)):
            search_box.send_keys(Keys.BACK_SPACE)
        search_box.send_keys(searchKeyword + Keys.ENTER)

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
            try:
                curBox = driver.find_element(By.CSS_SELECTOR, f'#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div:nth-child({curIndex}) > div > a')
            except:
                if len (driver.find_elements(By.CSS_SELECTOR, '#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd.QjC7t > div.m6QErb.XiKgde.tLjsW.eKbjU > div > p > span > span')) > 0: 
                    print("end reached")
                    break
                else: continue

            driver.execute_script("arguments[0].scrollIntoView()", curBox)
            time.sleep(0.2)
            print(curIndex)
        print("done search")
        for i in range(3, curIndex, 2):
            store = driver.find_element(By.CSS_SELECTOR, f'#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div:nth-child({i}) > div > a')
            if (store != None): storeLinks.append(store.get_attribute("href"))
        return storeLinks
    except Exception as e:
        print(e)
    finally: 

        driver.quit()



print(getLinksByPrompt("Hanoi", "bun cha"))
    #QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd.QjC7t > div:nth-child(78) > div > div

    #QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd.QjC7t > div.m6QErb.XiKgde.tLjsW.eKbjU > div > p > span > span

    #QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd.QjC7t > div:nth-child(241) > div > div

    #QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div:nth-child(3) > div > a