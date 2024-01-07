from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# Регистрируем класс, который будет описывать вэб страницу
class RegPage:
    # Размечаем элементы страницы:
    locators = {
        # кнопка авторизации
        'LOGIN_BTN_CLS': 'header__signin-link',
        'LOGIN_BTN_XPATH': '//*[@id="root"]/header/div/div/a',
        # чекбокс выбора категории пользователя - врач
        'DOC_CHK_BX_SEL': '#root > div > div > div > div > div > label:nth-child(3) > img',
        # чекбокс выбора категории пользователя - пациент
        'PATIENT_CHK_BX_SEL': '#root > div > div > div > div > div > label:nth-child(2) > img',
        # поле ввода номера телефона
        'PHONE_FLD_ID': 'phone',
        'PHONE_FLD_XPATH': '//*[@id="phone"]',
        # чекбокс принятия соглашения
        'AGRMT_CHK_BX_ID': 'agreement',
        'GRMT_CHK_BX_XPATH': '//*[@id="agreement"]',
        # кнопка далее
        "NXT_BTN_CLS": 'btn',
        'NXT_BTN_XPATH1': '//*[@id="root"]/div/div/div/div/form/div[2]/button',
        'NXT_BTN_XPATH2': '//*[@id="root"]/div/div/div/div/form/div[3]/button',
        # поля ввода кода
        'CODE_1_NM': 'first',
        'CODE_2_NM': 'second',
        'CODE_3_NM': 'third',
        'CODE_4_NM': 'fourth',
        # кнопка входя в личный кабинет
        'PROFL_BTN_XP': '//*[@id="root"]/header/div/div/a/img',
        # поле вводя фамилии
        'LNAME_XP': '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/form/div[1]/label[1]/input',
        # поле ввода имени
        'FNAME_XP': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[1]/label[2]/input',
        # поле ввода отчества
        'PATRONYMIC_XP': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[1]/label[3]/input',
        # сообщение об ошибке валидации поля фамилия
        'ER_MESS_LNAME_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[1]/label[1]/p',
        # сообщение об ошибке валидации поля имя
        'ER_MESS_FNAME_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[1]/label[2]/p',
        # сообщение об ошибке валидации поля отчество
        'ER_MESS_PATRON_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[1]/label[3]/p',
        # заголовок профиля "Личные данные"(для клика и снятия фокуса с полей)
        'PRFL_TTL_CLS': 'title'
        }

    def __init__(self, driver):
        self.driver = driver

    def fill_the_field(self, field_locator: str, test_data: str, find_meth: str) -> None:
        """Функция для заполнения поля"""
        if find_meth == 'CLASS_NAME':
            self.driver.find_element(By.CLASS_NAME, self.locators[field_locator]).send_keys(test_data)
        elif find_meth == 'ID':
            self.driver.find_element(By.ID, self.locators[field_locator]).send_keys(test_data)
        elif find_meth == 'NAME':
            self.driver.find_element(By.NAME, self.locators[field_locator]).send_keys(test_data)
        elif find_meth == 'XPATH':
            self.driver.find_element(By.XPATH, self.locators[field_locator]).send_keys(test_data)

    def click_element(self, elem_locator: str, find_meth:str) -> None:
        """Функция для клика по элементу"""
        if find_meth == 'ID':
            self.driver.find_element(By.ID, self.locators[elem_locator]).click()
        elif find_meth == 'CLASS_NAME':
            self.driver.find_element(By.CLASS_NAME, self.locators[elem_locator]).click()
        elif find_meth == 'SELECTOR':
            self.driver.find_element(By.CSS_SELECTOR, self.locators[elem_locator]).click()
        elif find_meth == 'XPATH':
            self.driver.find_element(By.XPATH, self.locators[elem_locator]).click()

    def get_elem_obj_or_ex(self, elem: str, find_meth: str):
        """Функция для получения объекта элемента"""
        elem_obj = None
        try:
            if find_meth == 'ID':
                elem_obj = self.driver.find_element(By.ID, self.locators[elem])
            elif find_meth == 'CLASS_NAME':
                elem_obj = self.driver.find_element(By.CLASS_NAME, self.locators[elem])
            elif find_meth == 'SELECTOR':
                elem_obj = self.driver.find_element(By.CSS_SELECTOR, self.locators[elem])
            elif find_meth == 'XPATH':
                elem_obj = self.driver.find_element(By.XPATH, self.locators[elem])
        except:
            print("Element is not found on the page!")

        return elem_obj


