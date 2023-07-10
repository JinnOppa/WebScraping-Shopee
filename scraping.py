from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time 

option = webdriver.ChromeOptions()
option.add_argument('--headless')
services = Service('chromedriver.exe')
driver = webdriver.Chrome(service = services, options = option)

shopee_link = "https://shopee.co.id/search?keyword=macbook"
driver.set_window_size(1300,800)
driver.get(shopee_link)
time.sleep(5)

driver.save_screenshot("home.png")
driver.quit()