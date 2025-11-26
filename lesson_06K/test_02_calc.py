import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.binary_location =\
        r"D:\Program Files\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    yield driver
    driver.quit()


@pytest.mark.positive
def test_calkul(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    driver.find_element(By.CSS_SELECTOR, "#delay").clear()
    driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    elements = driver.find_elements(By.CSS_SELECTOR, "div.keys>span")
    elements[0].click()
    elements[3].click()
    elements[1].click()
    elements[14].click()

    try:

        wait = WebDriverWait(driver, 50)

        element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".screen"))
        )

        wait.until(
            lambda driver: element.text.strip() == "15"
        )

        result = element.text.strip()
        assert result == "15", f"Ожидалось '15', получено '{result}'"
        print("Тест пройден: результат равен 15")

    except AssertionError as e:
        print(f"Ошибка проверки: {str(e)}")

    driver.quit()
