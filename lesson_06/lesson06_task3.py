from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.binary_location =\
                r"D:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()), options=options)


driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
)


driver.implicitly_wait(15)

driver.find_element(By.CSS_SELECTOR, "#landscape")

img_element = driver.find_element(By.CSS_SELECTOR, "#award")

src_value = img_element.get_attribute("src")
print(src_value)


driver.quit()
