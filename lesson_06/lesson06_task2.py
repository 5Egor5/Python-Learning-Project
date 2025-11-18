from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.binary_location =\
                r"D:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()), options=options)


waiter = WebDriverWait(driver, 30)

driver.get("http://uitestingplayground.com/textinput")

driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"),
                                     "SkyPro")
)

txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

print('"' + txt + '"')

driver.quit()
