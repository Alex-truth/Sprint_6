import allure
import pytest
from selenium.webdriver.common.by import By
from conftest import driver
from pages.order_page import OrderPage
from data import OrderSuite
from locators import OrderPageLocators



class TestOderPage:

    @allure.title('Заказ самоката. Позитивный сценарий')
    @allure.description('Проверяем, что заказ оформляется с правильными данными через разные кнопки "Заказать"')
    @pytest.mark.parametrize("button_type, name, surname, address, station, phone, date, rental_period, color, comment",
       [(OrderSuite.button_order[0], OrderSuite.name[0], OrderSuite.surname[0], OrderSuite.address[0],
         OrderSuite.station[0], OrderSuite.phone[0], OrderSuite.date[0], OrderSuite.rental_period[0],
         OrderSuite.color[0], OrderSuite.comment[0]),
        (OrderSuite.button_order[1], OrderSuite.name[1], OrderSuite.surname[1], OrderSuite.address[1],
         OrderSuite.station[1], OrderSuite.phone[1], OrderSuite.date[1], OrderSuite.rental_period[1],
         OrderSuite.color[1], OrderSuite.comment[1])
    ]
    )
    def test_order(self, driver, button_type, name, surname, address, station, phone, date, rental_period, color, comment):
        order_page = OrderPage(driver)
        order_page.cookie_accept()
        order_page.click_element(button_type)
        order_page.name_input(name)
        order_page.surname_input(surname)
        order_page.address_input(address)
        order_page.set_underground(station)
        order_page.number_input(phone)
        order_page.button_continue()
        order_page.date_delivery(date)
        order_page.rend_days(rental_period)
        order_page.color_scooter(color)
        order_page.comment_for_courier(comment)
        order_page.click_finish_button_order()
        order_page.order_confirmation()
        confirmation_message = order_page.read_text((By.XPATH, OrderPageLocators.ORDER_HAS_BEEN_PLACED))
        assert "Заказ оформлен" in confirmation_message


