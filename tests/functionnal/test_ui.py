from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_index_ui(DRIVER, SAMPLE_DATABASE):
    SAMPLE_DATABASE.load()

    email_input = DRIVER.find_element_by_name("email")
    email_input.send_keys("test1@test.com")
    email_input.submit()

    WebDriverWait(DRIVER, 5).until(
        ec.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Welcome, test1@test.com')]")
        )
    )

    assert "Welcome, test1@test.com" in DRIVER.page_source
