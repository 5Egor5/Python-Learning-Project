from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")
inter = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
inter.send_keys("Sky")
sleep(2)
inter.clear()
sleep(2)
inter.send_keys("Pro")

sleep(3)

driver.quit()
