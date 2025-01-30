import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Прокрутка страницы')
    def scroll_page(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))
        self.wait_to_visibility(locator)

    @allure.step("Ожидаем загрузки элемента")
    def wait_to_visibility(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидаем, что элемент станет кликабельным')
    def wait_to_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    @allure.step('Клик по элементу')
    def click_element(self, locator):
        self.wait_to_clickable(locator)
        self.driver.find_element(*locator).click()

    @allure.step("Читать текст элемента")
    def read_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Ввод данных')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Ожидание загрузки страницы')
    def wait_for_url(self, expected_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.current_url == expected_url)
