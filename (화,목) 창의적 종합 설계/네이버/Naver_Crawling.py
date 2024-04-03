from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options=Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.get('https://shopping.naver.com/home')

driver.find_element_by_xpath('')