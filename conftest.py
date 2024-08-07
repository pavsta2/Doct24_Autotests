# Импортируем библиотеку pytest для работы с фикстурами
import time

import pytest
# Импортируем библиотеку Selenium WebDriver для работы с веб-драйвером
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService

from pages.reg_page import RegPage
from config import URL_LOGIN, PHONE_NUMBER, EMAIL
from locators import locators_patient, locators_doctor


# Регистрируем метод для возможности параметризации браузера при запуске
# Пример: запуск тестов с помощью драйвера firefox: Pytest --browser firefox
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser name")


# Создаем фикстуру с областью видимости "session" для задания данных для авторизации
@pytest.fixture(scope="session", autouse=False)
def login_data():
    return {
        "PHONE": PHONE_NUMBER,
        "EMAIL": EMAIL,
        'CODE_1': '1',
        'CODE_2': '1',
        'CODE_3': '1',
        'CODE_4': '1'
    }


# Создаем фикстуру с областью видимости "session" для создания и закрытия веб-драйвера
@pytest.fixture(scope="session", autouse=False)
def browser(request):
    # получаем параметр введенный в терминале
    browser = request.config.getoption("--browser")
    # создаем экз драйвера нужного браузера либо вызываем ошибку
    if browser == "chrome":
        options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--load-extension=/Users/darinastarshinova/Library/Application Support/Google/'
        #                      'Chrome/Default/Extensions/padekgcemlokbadohgkifijomclgjgif/2.5.21_0')
        options.add_argument("--window-size=2800,1200")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option("useAutomationExtension", False)
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
    driver.implicitly_wait(2)

    # Используем инструкцию yield для предоставления веб-драйвера тестам и ожидания завершения тестов
    yield driver

    # Закрываем веб-драйвер после завершения каждого теста
    driver.quit()


@pytest.fixture(scope="session", autouse=False)
def enter_auth(browser, login_data):
    """Авторизация и вход в профиль"""

    # Создаем экземпляр RegPage, передавая веб-драйвер (фикстура browser) в качестве аргумента
    reg_page = RegPage(browser, locators_patient.locators)
    # Открываем страницу с помощью веб-драйвера
    browser.get(URL_LOGIN)
    # Заходим на страницу авторизации
    reg_page.click_element('LOGIN_BTN_XPATH',
                           'XPATH')
    return reg_page


@pytest.fixture(scope="session", autouse=False)
def login_patient(browser, login_data):
    """Авторизация и вход в профиль"""

    # Создаем экземпляр RegPage, передавая веб-драйвер (фикстура browser) в качестве аргумента
    reg_page = RegPage(browser, locators_patient.locators)
    # Открываем страницу с помощью веб-драйвера
    browser.get(URL_LOGIN)
    # Заходим на страницу авторизации
    reg_page.click_element('LOGIN_BTN_XPATH',
                           'XPATH')
    time.sleep(3)
    # Заполняем поля
    reg_page.fill_the_field('PHONE_FLD_ID',
                            login_data['PHONE'],
                            'ID')
    reg_page.click_element('PATIENT_CHK_BX_SEL',
                           'SELECTOR')
    reg_page.click_element('AGRMT_CHK_BX_XPATH',
                           'XPATH')
    # нажимаем на кнопку Далее
    reg_page.click_element("NXT_BTN_XPATH1",
                           'XPATH')
    time.sleep(2)
    # вносим проверочный код (по умолчанию 1111 на тестовом стенде)
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
    # Нажимаем кнопку Далее
    reg_page.click_element("NXT_BTN_XPATH2",
                           'XPATH')
    time.sleep(1)
    # вводим тестовый имейл пользователя (реальный)
    reg_page.fill_the_field('AUTH_EMAIL_FLD_ID',
                            login_data['EMAIL'],
                            'ID')
    # нажимаем кнопку Далее
    reg_page.click_element("NXT_BTN_XPATH3",
                           'XPATH')
    # по новой логике необходимо вручную зайти в почту, взять оттуда код и вручную ввести его в окно подтверждения,
    # программа в это время ждет 30 сек (кнопку Далее вручную нажимать НЕ НАДО)
    # нажимаем кнопку Далее
    time.sleep(30)
    # Снова нажимаем кнопку Далее
    reg_page.click_element("NXT_BTN_XPATH4",
                           'XPATH')
    time.sleep(2)
    # переходим в профиль
    reg_page.click_element('PROFL_BTN_XP',
                           'XPATH')
    reg_page.click_element('PROFL_BTN_XP',
                           'XPATH')
    time.sleep(2)

    return reg_page


@pytest.fixture(scope="session", autouse=False)
def login_doctor(browser, login_data):
    """Авторизация и вход в профиль"""

    # Создаем экземпляр RegPage, передавая веб-драйвер (фикстура browser) в качестве аргумента
    reg_page = RegPage(browser, locators_doctor.locators)
    # Открываем страницу с помощью веб-драйвера
    browser.get(URL_LOGIN)
    # Заходим на страницу авторизации
    reg_page.click_element('LOGIN_BTN_XPATH',
                           'XPATH')
    time.sleep(1)
    # Заполняем поля
    reg_page.fill_the_field('PHONE_FLD_ID',
                            login_data['PHONE'],
                            'ID')
    reg_page.click_element('DOCTOR_CHK_BX_XP',
                           'XPATH')
    reg_page.click_element('AGRMT_CHK_BX_XPATH',
                           'XPATH')
    # нажимаем на кнопку Далее
    reg_page.click_element("NXT_BTN_XPATH1",
                           'XPATH')
    # вносим проверочный код (по дефолту 1111 для тестового стенда)
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
    # нажимаем кнопку Далее
    reg_page.click_element("NXT_BTN_XPATH2",
                           'XPATH')
    time.sleep(1)
    # вводим тестовый имейл пользователя (реальный)
    reg_page.fill_the_field('AUTH_EMAIL_FLD_ID',
                            login_data['EMAIL'],
                            'ID')
    # нажимаем кнопку Далее
    reg_page.click_element("NXT_BTN_XPATH3",
                           'XPATH')
    # по новой логике необходимо вручную зайти в почту, взять оттуда код и вручную ввести его в окно подтверждения,
    # программа в это время ждет 30 сек (кнопку Далее вручную нажимать НЕ НАДО)
    # нажимаем кнопку Далее
    time.sleep(30)
    # Снова нажимаем кнопку Далее
    reg_page.click_element("NXT_BTN_XPATH4",
                           'XPATH')
    time.sleep(1)
    # переходим в профиль
    reg_page.click_element('PROFL_BTN_XP',
                           'XPATH')
    reg_page.click_element('PROFL_BTN_XP',
                           'XPATH')
    time.sleep(1)

    return reg_page


# фикстура для нажатия на кнопку Добавить аллергию
@pytest.fixture(scope="function", autouse=False)
def open_allegry_section(browser, login_patient):
    login_patient.click_element('ALLERGY_BTN_XPATH', 'XPATH')
    yield
    login_patient.click_element('ALLERGY_BTN_DEL_XP', 'XPATH')


# фикстура для нажатия на кнопку Добавить операцию
@pytest.fixture(scope="function", autouse=False)
def open_surgeries_section(browser, login_patient):
    login_patient.click_element('SURGERIES_BTN_XPATH', 'XPATH')
    yield
    # после завершения теста, удаляем форму
    login_patient.click_element('SURGERIES_DEL_BTN_XP', 'XPATH')


# фикстура для нажатия на кнопку Добавить операцию
@pytest.fixture(scope="function", autouse=False)
def open_medication_section(browser, login_patient):
    login_patient.click_element('MEDICATION_BTN_XPATH', 'XPATH')
    yield
    # после завершения теста, удаляем форму
    login_patient.click_element('MEDICATION_DEL_BTN_XP', 'XPATH')


# фикстура для нажатия на кнопку Добавить заболевание
@pytest.fixture(scope="function", autouse=False)
def open_chron_des_section(browser, login_patient):
    login_patient.click_element('CHRON_DES_BTN_XPATH', 'XPATH')
    yield
    # после завершения теста, удаляем форму
    login_patient.click_element('CHRON_DES_DEL_BTN_XP', 'XPATH')


def get_test_case_docstring(item):
    """ Эта функция получает текст из doc string функции и форматирует ее
    для показа в качестве названия теста в отчете.
    """
    full_name = ''

    if item._obj.__doc__:
        # Удаляем лишние пробелы из текущего названия:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        # Генерируем список параметров для тестов с параметризацией:
        if hasattr(item, 'callspec'):
            params = item.callspec.params
            # создаем список ключей
            res_keys = sorted([k for k in params])
            # Создаем cписок:
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            # Добавляем словарь со всеми параметрами к названию теста:
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


def pytest_itemcollected(item):
    """ Эта функция подменят название теста на результат функции get_test_case_docstring во время его исполнения."""
    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """ Эта функция модифицирует названия тестов при вызове --collect-only параметра
        (получения списка всех имеющихся тестов).
    """
    if session.config.option.collectonly is True:
        for item in session.items:
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('Done!')

