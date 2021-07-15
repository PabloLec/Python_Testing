from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_ui(DRIVER, SAMPLE_DATABASE):
    SAMPLE_DATABASE.load()

    email_input = DRIVER.find_element_by_name("email")
    email_input.send_keys("test1@test.com")
    email_input.submit()

    WebDriverWait(DRIVER, 5).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Welcome')]")))

    assert "Welcome, test1@test.com" in DRIVER.page_source


def test_summary_ui(DRIVER, SAMPLE_DATABASE):
    WebDriverWait(DRIVER, 5).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Welcome')]")))

    assert "Points available: 20" in DRIVER.page_source

    competition_list = DRIVER.find_element_by_class_name("competition-list")
    competitions = competition_list.find_elements_by_tag_name("li")

    assert len(competitions) == 2

    competitions[0].find_element_by_tag_name("a").click()


def test_booking_ui(DRIVER, SAMPLE_DATABASE):
    WebDriverWait(DRIVER, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Competition')]"))
    )

    title = DRIVER.find_element_by_tag_name("h2")

    assert "Competition Test 1" in title.text
    assert "Places available: 21" in DRIVER.page_source

    places_input = DRIVER.find_element_by_name("places")

    assert places_input.get_attribute("min") == "1"
    assert places_input.get_attribute("max") == "12"

    places_input.send_keys("12")

    submit_button = DRIVER.find_element_by_xpath("//button[@type='submit']")
    submit_button.click()

    WebDriverWait(DRIVER, 5).until(EC.visibility_of_element_located((By.XPATH, "//ul[@class='flashes']")))

    assert "booking complete!" in DRIVER.page_source


def test_values_update_ui(DRIVER, SAMPLE_DATABASE):
    assert "Points available: 8" in DRIVER.page_source

    competition_list = DRIVER.find_element_by_class_name("competition-list")
    competitions = competition_list.find_elements_by_tag_name("li")

    assert "Number of Places: 9" in competitions[0].text


def test_club_list_ui(DRIVER, SAMPLE_DATABASE):
    DRIVER.get("http://127.0.0.1:5000/clubs")

    for club in SAMPLE_DATABASE.CLUBS:
        assert club["name"] in DRIVER.page_source
