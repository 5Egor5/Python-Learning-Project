from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")

name = driver.find_element(By.CSS_SELECTOR, "input#username")
name.send_keys("tomsmith")

pas = driver.find_element(By.CSS_SELECTOR, "input#password")
pas.send_keys("SuperSecretPassword!")

driver.find_element(By.CSS_SELECTOR, "button.radius").click()

sleep(2)

grean = driver.find_element(By.CSS_SELECTOR, "div#flash").text
print(grean)

sleep(3)

driver.quit()
