from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys  # 引入按鍵盤的按鍵
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:/Users/User/Desktop/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com")
search = driver.find_element_by_name("q")  # google首頁的name剛好是q，並非都一樣

search.clear()  #先把搜尋欄清空
search.send_keys("比特幣")  # 搜尋比特幣
search.send_keys(Keys.RETURN)  # 按下ENTER

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "LC20lb"))
    )
# 打開An explicit wait is a code you define to wait for a certain condition to occur before proceeding further in the code. 
# The extreme case of this is time.sleep(), which sets the condition to an exact time period to wait. 
# There are some convenience methods provided that help you write code that will wait only as long as required. 
# WebDriverWait in combination with ExpectedCondition is one way this can be accomplished.

titles = driver.find_elements(By.CLASS_NAME,"LC20lb")
for title in titles:  #對每一個標題的標籤
    print(title.text)

link = driver.find_element_by_xpath('//*[@id="rso"]/div[2]/div/div/div/div[1]/a/h3')  # COPY裡面的XPATH
# link = driver.find_element(By.CLASS_NAME,"LC20lb MBeuO DKV0Md") #不能用，因為搜尋的每個CLASSNAME都叫做LC20lb MBeuO DKV0Md
link.click()
driver.back()  # driver 瀏覽器，back：回到上一頁
driver.back()
driver.forward() # 回到下一頁 

print(driver.title)  # 印出網頁上面顯示的東西



time.sleep(5)
driver.quit()