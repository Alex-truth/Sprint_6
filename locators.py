from selenium.webdriver.common.by import By

class MainPaigeLocators:
    BLOCK_TO_FAQ = 'Home_FourPart__1uthg'
    QUESTIONS = 'Home_FAQ__3uVm4'
    FAQ_BUTTON = ".//div[@class='accordion__button']"
    QUESTIONS_LOCATOR = "accordion__heading-{0}"
    ANSWERS_LOCATOR = "//div[@id='accordion__panel-{0}']/p"


class OrderPageLocators:
    BUTTON_ORDER_IN_HEADER = [By.CLASS_NAME, 'Button_Button__ra12g']
    BUTTON_ORDER_IN_PAGE = [By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button"]
    NAME_INPUT = "//input[@placeholder='* Имя']"
    SURNAME_INPUT = "//input[@placeholder='* Фамилия']"
    ADDRESS_INPUT = "//input[@placeholder='* Адрес: куда привезти заказ']"
    UNDERGROUND = "//div[@class='select-search']//input"
    METRO_DROPDOWN = "//div[@class='select-search__select']"
    PHONE_NUMBER = "//input[contains(@placeholder, 'Телефон')]"
    CONTINUE_BUTTON = "//button[text()='Далее']"
    DATE = "//div[@class='react-datepicker__input-container']/input[@placeholder='* Когда привезти самокат']"
    RENT_DAYS = ".//div[@class='Dropdown-root']"
    COMMENT_DELIVERY = "//input[contains(@placeholder, 'Комментарий')]"
    BUTTON_ORDER_IN_FINISH = "//div[starts-with(@class, 'Order')]/button[text()='Заказать']"
    BUTTON_YES = "//div[@class='Order_Buttons__1xGrp']/button[text()='Да']"
    ORDER_HAS_BEEN_PLACED = "//div[text()='Заказ оформлен']"
    COOKIE_BUTTON = "#rcc-confirm-button"
    RENTAL_PERIOD_2 = [By.XPATH, "//div[@class='Dropdown-option'][position()=2]"]
    RENTAL_PERIOD_5 = [By.XPATH, "//div[@class='Dropdown-option'][position()=5]"]
    COLOR_BLACK = [By.XPATH, "//label[contains(@for, 'black')]"]
    COLOR_GREY = [By.XPATH, "//label[contains(@for, 'grey')]"]
    LOGO_SCOOTER = "//a[@class='Header_LogoScooter__3lsAR']"
    LOGO_YANDEX = "//a[@class='Header_LogoYandex__3TSOI']"