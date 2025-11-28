import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


@pytest.fixture
def driver():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    driver_path = os.path.join(current_dir, 'msedgedriver.exe')
    service = Service(executable_path=driver_path)
    _driver = webdriver.Edge(service=service)
    yield _driver
    _driver.quit()


@pytest.mark.positive
def test_validation(driver):

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    zip_field = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_field.get_attribute(
        "class"), "Поле zip некрасное"

    green_fields = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    wait = WebDriverWait(driver, 4)

    for field in green_fields:

        try:

            a_loc = f".form-group[data-bs-toggle='tooltip']\
                    [data-bs-target='#{field}'] .alert"
            alert_element = wait.until(
                EC.presence_of_element_located(By.CSS_SELECTOR, a_loc)
            )

            assert "alert-success" in alert_element.get_attribute("class"), (
                f"Поле {field} не подсвечено зелёным")

        except Exception as e:
            print(f"Ошибка при проверке поля {field}: {str(e)}")
