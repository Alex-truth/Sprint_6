import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Клик по кнопке Заказать в шапке')
    def click_button_order_in_header(self):
        self.click_element(OrderPageLocators.BUTTON_ORDER_IN_HEADER)

    @allure.step('Клик по кнопке Заказать внизу страницы')
    def click_button_order_in_page(self):
        self.wait_to_clickable((By.XPATH, OrderPageLocators.BUTTON_ORDER_IN_PAGE))
        self.click_element(OrderPageLocators.BUTTON_ORDER_IN_PAGE)

    @allure.step('Ввод имени')
    def name_input(self, name):
        self.send_keys_to_input((By.XPATH, OrderPageLocators.NAME_INPUT), name)

    @allure.step('Ввод фамилии')
    def surname_input(self, surname):
        self.send_keys_to_input((By.XPATH, OrderPageLocators.SURNAME_INPUT), surname)

    @allure.step('Ввод адреса куда привезти')
    def address_input(self, address):
        self.send_keys_to_input((By.XPATH, OrderPageLocators.ADDRESS_INPUT), address)

    @allure.step('Выбор станции метро')
    def set_underground(self, station):
        self.send_keys_to_input((By.XPATH,OrderPageLocators.UNDERGROUND), station)
        self.click_element((By.XPATH, OrderPageLocators.METRO_DROPDOWN))

    @allure.step('Ввод номера телефона')
    def number_input(self, number):
        self.send_keys_to_input((By.XPATH,OrderPageLocators.PHONE_NUMBER), number)

    @allure.step('Клик по кнопке далее')
    def button_continue(self):
        self.click_element((By.XPATH, OrderPageLocators.CONTINUE_BUTTON))

    @allure.step('Ввод даты когда привезти самокат')
    def date_delivery(self, date):
        self.send_keys_to_input((By.XPATH, OrderPageLocators.DATE), date)
        self.send_keys_to_input((By.XPATH, OrderPageLocators.DATE), Keys.ENTER)


    @allure.step('Срок аренды')
    def rend_days(self, rental_period):
        self.click_element((By.XPATH, OrderPageLocators.RENT_DAYS))
        self.click_element(rental_period)

    @allure.step('Выбор цвета самоката')
    def color_scooter(self,color):
        self.click_element(color)

    @allure.step('Комментарий для курьера')
    def comment_for_courier(self, comment):
        self.send_keys_to_input((By.XPATH, OrderPageLocators.COMMENT_DELIVERY), comment)

    @allure.step('Финальная кнопка Заказать')
    def click_finish_button_order(self):
        self.click_element((By.XPATH, OrderPageLocators.BUTTON_ORDER_IN_FINISH))

    @allure.step('Подтверждение заказа')
    def order_confirmation(self):
        self.click_element((By.XPATH, OrderPageLocators.BUTTON_YES))

    @allure.step('Подтверждение куки')
    def cookie_accept(self):
        self.click_element((By.CSS_SELECTOR, OrderPageLocators.COOKIE_BUTTON))








