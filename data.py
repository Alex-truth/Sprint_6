from locators import OrderPageLocators

class Answers:
    answer_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    answer_2 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    answer_3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    answer_4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    answer_5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    answer_6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    answer_7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    answer_8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'



class OrderSuite:
    button_order = [OrderPageLocators.BUTTON_ORDER_IN_HEADER, OrderPageLocators.BUTTON_ORDER_IN_PAGE]
    name = ['Иван', 'Катя']
    surname = ['Иванов', 'Катина']
    address = ['Москва, ул. Улюлювица 15', 'Москва, ул. Замученная 25']
    station = ['Коньково', 'Юго-Западная']
    phone = ["88005555555", "88006666666"]
    date = ["25.01.2025", "28.01.2025"]
    rental_period = [OrderPageLocators.RENTAL_PERIOD_2, OrderPageLocators.RENTAL_PERIOD_5]
    color = [OrderPageLocators.COLOR_BLACK, OrderPageLocators.COLOR_GREY]
    comment = ["Оставьте самокат у подъезда.", "Пожалуйста, привезите вовремя."]

