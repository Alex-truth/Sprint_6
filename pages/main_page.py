import allure
from locators import MainPaigeLocators
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Скролл к блоку Вопросы о важном')
    def scroll_page_to_faq(self):
        self.scroll_page((By.CLASS_NAME, MainPaigeLocators.BLOCK_TO_FAQ))

    @allure.step('Ожидаем загрузки вопросов')
    def wait_to_faq(self):
        self.wait_to_visibility((By.CLASS_NAME,MainPaigeLocators.QUESTIONS))

    @allure.step("Выбираем вопрос")
    def get_question(self, number_questions):
        return MainPaigeLocators.QUESTIONS_LOCATOR.format(number_questions)

    @allure.step('Клик по вопросу')
    def click_question(self, number_question):
        self.click_element((By.ID, self.get_question(number_question)))

    @allure.step("Выбираем ответ")
    def get_answer(self, number_questions):
        return MainPaigeLocators.ANSWERS_LOCATOR.format(number_questions)

    @allure.step("Ответ на вопрос")
    def read_answer_value(self, number_questions):
        self.wait_to_visibility((By.XPATH, self.get_answer(number_questions)))
        return self.read_text((By.XPATH, self.get_answer(number_questions)))
