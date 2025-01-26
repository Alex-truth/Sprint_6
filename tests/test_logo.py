import allure
from selenium.webdriver.common.by import By
from pages.order_page import OrderPage
from locators import OrderPageLocators
from urls import Urls


class TestSwitch:
    @allure.title('При клике на логототип Самоката - попадаем на главную страницу Самоката')
    @allure.description('С главной страницы переходим на форму заказа и кликаем на лого Самоката')
    def test_switch_logo_scooter(self,driver):
        scooter = OrderPage(driver)
        scooter.click_element(OrderPageLocators.BUTTON_ORDER_IN_HEADER)
        scooter.click_element((By.XPATH, OrderPageLocators.LOGO_SCOOTER))
        assert driver.current_url == Urls.MAIN_PAGE

    @allure.title('При клике на логотиа Яндекса, в новом окне открывается главная страница Дзена')
    @allure.description('C главной страницы Самоката переход на страницу Дзена, открываем вкладку, ждем загрузки страницы')
    def test_switch_logo_yandex(self,driver):
        yandex = OrderPage(driver)
        yandex.click_element((By.XPATH, OrderPageLocators.LOGO_YANDEX))
        driver.switch_to.window(driver.window_handles[1])
        yandex.wait_for_url(Urls.DZEN_PAGE)
        assert driver.current_url == Urls.DZEN_PAGE

