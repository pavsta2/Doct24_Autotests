# Импортируем библиотеку pytest для работы с фикстурами
import pytest
# Импортируем библиотеку Selenium WebDriver для работы с веб-драйвером
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService

from pages.reg_page import RegPage
from config import URL_LOGIN


# Регистрируем метод для возможности параметризации браузера при запуске
# Пример: запуск тестов с помощью драйвера firefox: Pytest --browser firefox
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser name")


# Создаем фикстуру с областью видимости "session" для задания данных для авторизации
@pytest.fixture(scope="session", autouse=True)
def login_data():
    return {
        "PHONE": "9113459832",
        'CODE_1': '1',
        'CODE_2': '1',
        'CODE_3': '1',
        'CODE_4': '1'
    }


# Создаем фикстуру с областью видимости "session" для создания и закрытия веб-драйвера
@pytest.fixture(scope="session", autouse=True)
def browser(request):
    # получаем параметр введенный в терминале
    browser = request.config.getoption("--browser")
    # создаем экз драйвера нужного браузера либо вызываем ошибку
    if browser == "chrome":
        options = Options()
        options.add_argument('--headless')
        options.add_argument("--window-size=2800,1900")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.page_load_strategy = 'normal'
        service = ChromeService()
        driver = webdriver.Chrome(service=service, options=options)

    elif browser == "firefox":
        # options = webdriver.FirefoxOptions()
        # options.add_argument("--window-size=2000,1000")
        driver = webdriver.Firefox()
    elif browser == "safari":
        # options = webdriver.SafariOptions()
        # options.add_argument("--window-size=maxsize")
        driver = webdriver.Safari()

    else:
        raise Exception("Invalid browser name")

    # Устанавливаем время неявного ожидания элементов на странице
    driver.implicitly_wait(5)

    # Используем инструкцию yield для предоставления веб-драйвера тестам и ожидания завершения тестов
    yield driver

    # Закрываем веб-драйвер после завершения каждого теста
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def login_patient(browser, login_data):
    """Авторизация"""

    # Создаем экземпляр RegPage, передавая веб-драйвер (фикстура browser) в качестве аргумента
    reg_page = RegPage(browser)
    # Открываем страницу с помощью веб-драйвера
    browser.get(URL_LOGIN)
    # Заходим на страницу авторизации
    reg_page.click_element('LOGIN_BTN_XPATH',
                           'XPATH')
    # Заполняем поля
    reg_page.fill_the_field('PHONE_FLD_ID',
                            login_data['PHONE'],
                            'ID')
    reg_page.click_element('PATIENT_CHK_BX_SEL',
                           'SELECTOR')
    reg_page.click_element('GRMT_CHK_BX_XPATH',
                           'XPATH')
    reg_page.click_element("NXT_BTN_XPATH1",
                           'XPATH')
    reg_page.fill_the_field('CODE_1_NM',
                            login_data['CODE_1'],
                            'NAME')
    reg_page.fill_the_field('CODE_2_NM',
                            login_data['CODE_2'],
                            'NAME')
    reg_page.fill_the_field('CODE_3_NM',
                            login_data['CODE_3'],
                            'NAME')
    reg_page.fill_the_field('CODE_4_NM',
                            login_data['CODE_4'],
                            'NAME')
    reg_page.click_element("NXT_BTN_XPATH2",
                           'XPATH')

    return reg_page