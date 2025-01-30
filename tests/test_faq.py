import allure
import pytest
from conftest import driver
from data import Answers
from pages.main_page import MainPage


class TestFAQ:
    @allure.title('Открывается текст ответа, соответствующий вопросу')
    @pytest.mark.parametrize('number_questions, answer',
                             [(0, Answers.answer_1),
                             (1, Answers.answer_2),
                             (2, Answers.answer_3),
                             (3, Answers.answer_4),
                             (4, Answers.answer_5),
                             (5, Answers.answer_6),
                             (6, Answers.answer_7),
                             (7, Answers.answer_8)])
    def test_faq(self, number_questions, answer, driver):
        main_page = MainPage(driver)
        main_page.scroll_page_to_faq()
        main_page.wait_to_faq()
        main_page.click_question(number_questions)
        assert main_page.read_answer_value(number_questions) == answer






