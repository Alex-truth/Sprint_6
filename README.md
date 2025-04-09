Цель проекта:
Автоматизация пользовательских сценариев для учебного веб-приложения «Яндекс.Самокат» с использованием Selenium WebDriver, Pytest, Page Object Model (POM) и Allure-отчётов.

Реализованные тесты:
Раздел «Вопросы о важном»:

Написаны автотесты для каждого вопроса в FAQ.

Проверка: по клику на стрелку открывается нужный текст-ответ.

Флоу оформления заказа:

Два позитивных сценария с разными наборами данных.

Две точки входа: кнопка «Заказать» вверху и внизу страницы.

Проверка формы заказа и всплывающего окна об успешном оформлении.

Переходы по логотипам:

Клик по логотипу «Самоката» ведёт на главную.

Клик по логотипу Яндекса открывает Dzen в новой вкладке.

Технологии:
Язык: Python

Фреймворк: Pytest

Браузер: Mozilla Firefox

Библиотеки: Selenium, Allure, Pytest-parameters

Подход: Page Object Model (POM)

Отчётность: Allure Report

Особенности реализации:
Структурированный код: страницы — в pages/, тесты — в tests/

Использована параметризация для повторяющихся сценариев

Все тесты снабжены Allure-шагами и названиями
