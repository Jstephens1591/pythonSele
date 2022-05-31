import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys

#Gets driver and checks if it works.
class main:
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    chrome_driver.get('https://www.ebay.com/')

    def Get_Ebay():

        main.chrome_driver.maximize_window()

        if not "Electronics, Cars, Fashion, Collectibles & More | eBay" in main.chrome_driver.title:
            raise Exception("Page Could Not Load, Check Title Text")


    def sleep_and_quit():
        time.sleep(2)
        main.chrome_driver.quit()

#making sure that click elements dont crash application.

    def click_element(find_element_mode, item):
        s = 1
        if find_element_mode == "XPATH":
            click_element = main.chrome_driver.find_element(By.XPATH, item)
        elif find_element_mode == "ID":
            click_element = main.chrome_driver.find_element(By.ID, item)
        elif find_element_mode == "NAME":
            click_element = main.chrome_driver.find_element(By.NAME, item)
        elif find_element_mode == "CLASS_NAME":
            click_element = main.chrome_driver.find_element(By.CLASS_NAME, item)
        else:
            raise Exception("in click_element function, find_element_mode does not match.")
            s = 0

        if s == 1:
            click_element.click()
            timeout = 5
            try:
                element_present = EC.presence_of_element_located((By.ID, 'name'))
                WebDriverWait(main.chrome_driver, timeout).until(element_present)
            except TimeoutException:
                print("Timed out waiting for page to load")
            finally:
                print("Page loaded")


#very basic selenium calls     

main.Get_Ebay()
main.click_element(find_element_mode= "CLASS_NAME", item = 'gh-cart-icon')
main.chrome_driver.back()
search_input = main.chrome_driver.find_element(By.ID, "gh-ac")
search_input.send_keys("Iphone")
main.click_element(find_element_mode="XPATH", item='//*[@id="gh-btn"]')



# Call This lAST!
main.sleep_and_quit()

