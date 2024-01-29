import time, datetime

from selenium.webdriver.common.by import By
from datetime import timedelta
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Регистрируем класс, который будет описывать вэб страницу
class RegPage:
    # Размечаем элементы страницы:
    locators = {
        # кнопки
        # кнопка авторизации
        'LOGIN_BTN_CLS': 'header__signin-link',
        'LOGIN_BTN_XPATH': '//*[@id="root"]/header/div/div/a',
        # кнопка далее
        "NXT_BTN_CLS": 'btn',
        'NXT_BTN_XPATH1': '//*[@id="root"]/div/div/div/div/form/div[2]/button',
        'NXT_BTN_XPATH2': '/html/body/div[1]/div/div/div/div/form/div[3]/button',
        # кнопка входя в личный кабинет
        'PROFL_BTN_XP': '//*[@id="root"]/header/div/div/a/img',
        # кнопка добавления информации об аллергии
        'ALLERGY_BTN_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[3]/button',
        # кнопка добавления информации об операции
        'SURGERIES_BTN_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[4]/button',
        'SURGERIES_BTN_SEL': '#root > section > div > div.content > div > div > div.data > div > form > div:nth-child(3) > div:nth-child(5) > button',
        # кнопка добавления информации о приеме препаратов
        'MEDICATION_BTN_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[5]/button',
        # кнопка добавления информации о хронич заболеваниях
        'CHRON_DES_BTN_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[6]/button',

        # чекбоксы
        # чекбокс выбора категории пользователя - врач
        'DOC_CHK_BX_SEL': '#root > div > div > div > div > div > label:nth-child(3) > img',
        # чекбокс выбора категории пользователя - пациент
        'PATIENT_CHK_BX_SEL': '#root > div > div > div > div > div > label:nth-child(2) > img',
        # чекбокс принятия соглашения
        'AGRMT_CHK_BX_ID': 'agreement',
        'GRMT_CHK_BX_XPATH': '//*[@id="agreement"]',

        # поля ввода
        # поле ввода номера телефона
        'PHONE_FLD_ID': 'phone',
        'PHONE_FLD_XPATH': '//*[@id="phone"]',
        # поля ввода кода
        'CODE_1_NM': 'first',
        'CODE_1_XPATH': '//*[@id="root"]/div/div/div/div/form/div[1]/input[1]',
        'CODE_2_NM': 'second',
        'CODE_2_XPATH': '//*[@id="root"]/div/div/div/div/form/div[1]/input[2]',
        'CODE_3_NM': 'third',
        'CODE_3_XPATH': '//*[@id="root"]/div/div/div/div/form/div[1]/input[3]',
        'CODE_4_NM': 'fourth',
        'CODE_4_XPATH': '//*[@id="root"]/div/div/div/div/form/div[1]/input[4]',
        # поле вводя фамилии
        'LNAME_XP': '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/form/div[1]/label[1]/input',
        # поле ввода имени
        'FNAME_XP': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[1]/label[2]/input',
        # поле ввода отчества
        'PATRONYMIC_XP': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[1]/label[3]/input',
        # поле ввода email
        'EMAIL_FLD_NM': 'user.email',
        # поле ввода даты рождения
        'DBIRTH_FLD_NM': 'user.birthday',
        # поле ввода роста
        'HEIGHT_FLD_NM': 'patientProfile.height',
        # поле ввода веса
        'WEIGHT_FLD_NM': 'patientProfile.weight',
        # поле аллерген
        'ALLRGEN_FLD_NM': 'allergies.0.title',
        # поле Реакиция
        'REACTION_FLD_NM': 'allergies.0.value',
        # поле Операции
        'SURGERIES_FLD_NM': 'operations.0.description',
        # поле Год проведения (операции)
        'SURGERIE_YEAR_FLD_NM': 'operations.0.date',
        # поле Препарат
        'MEDICATION_FLD_NM': 'medicines.0.title',
        # поле дозировка
        'DOSAGE_FLD_NM': 'medicines.0.dosage',
        # поле периодичность приема
        'FREQ_OF_TAKING_FLD_NM': 'medicines.0.frequency',
        # поле Хронические заболевания
        'CHRON_DES_FLD_NM': 'diseases.0.title',
        # поле Год обнаружения (хронич заболеваний)
        'CHRON_DISC_YEAR_FLD_NM': 'diseases.0.value',

        # сообщения об ошибках
        # сообщение об ошибке валидации поля фамилия
        'ER_MESS_LNAME_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[1]/label[1]/p',
        # сообщение об ошибке валидации поля имя
        'ER_MESS_FNAME_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[1]/label[2]/p',
        # сообщение об ошибке валидации поля отчество
        'ER_MESS_PATRON_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[1]/label[3]/p',
        # сообщение об ошибке валидации поля Дата рождения
        'ER_MESS_DBIRTH_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[1]/label[4]/p',
        # сообщение об ошибке валидации поля Email
        'ER_MESS_EMAIL_XPATH': '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/form/div[1]/label[5]/p',
        # сообщение об ошибке валидации поля Рост
        'ER_MESS_HEIGHT_XPATH': '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/form/div[2]/div/label[1]/p',
        # сообщение обошибке валидации поля Вес
        'ER_MESS_WEIGHT_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[2]/div/label[2]/p',
        # сообщение об ошибке валидации поля Аллерген
        'ER_MESS_ALLERGEN_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[3]/div/label/p',
        # сообщение об ошибке валидации поля Реакция
        'ER_MESS_REACTION_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[3]/div/div/label/p',
        # сообщение об ошибке валидации поля Операции
        'ER_MESS_SURGERIES_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[4]/div/label/p',
        # сообщение об ошибке валидации поля Год проведения(операции)
        'ER_MESS_SURGERIE_YEAR_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[4]/div/div/label/p',
        # сообщение об ошибке валидации поля Препарат
        'ER_MESS_MEDICATION_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[5]/div/label[1]/p',
        # сообшение об ошибке валидации поля Дозировка
        'ER_MESS_DOSAGE_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[5]/div/label[2]/p',
        # сообщение об ошибке валидации поля периодичность приема
        'ER_MESS_FREQ_OF_TKNG_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[5]/div/div/label/p',
        # сообщение об ошибке валидации поля Хронич заболевания
        'ER_MESS_CHRON_DES_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[6]/div/label/p',
        # сообщение об ошибке валидации поля Год обнаружения (хронич заболевания)
        'ER_MESS_CHRON_DISC_YEAR_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[6]/div/div/label/p',

        # прочие элементы
        # задний блок на странице профиля (для клика, что снять фокус с полей)
        'BLOCK_PRFL_SEL': 'rightBlock',
        # нейтральная область страницы (для клика, чтоб снять фокус)
        'LEFT_PAGE_AREA_XPATH': '//*[@id="root"]/section/div/div[2]/nav',
        }

    def __init__(self, driver):
        self.driver = driver

    def fill_the_field(self, field_locator: str, test_data: str, find_meth: str) -> None:
        """Функция для заполнения поля"""
        time.sleep(0.1)
        if find_meth == 'CLASS_NAME':
            self.driver.find_element(By.CLASS_NAME, self.locators[field_locator]).send_keys(test_data)
        elif find_meth == 'ID':
            self.driver.find_element(By.ID, self.locators[field_locator]).send_keys(test_data)
        elif find_meth == 'NAME':
            self.driver.find_element(By.NAME, self.locators[field_locator]).send_keys(test_data)
        elif find_meth == 'XPATH':
            self.driver.find_element(By.XPATH, self.locators[field_locator]).send_keys(test_data)

    def click_element(self, elem_locator: str, find_meth: str) -> None:
        """Функция для клика по элементу"""
        time.sleep(0.1)
        if find_meth == 'ID':
            self.driver.find_element(By.ID, self.locators[elem_locator]).click()
        elif find_meth == 'CLASS_NAME':
            self.driver.find_element(By.CLASS_NAME, self.locators[elem_locator]).click()
        elif find_meth == 'SELECTOR':
            self.driver.find_element(By.CSS_SELECTOR, self.locators[elem_locator]).click()
        elif find_meth == 'XPATH':
            self.driver.find_element(By.XPATH, self.locators[elem_locator]).click()

    def get_elem_obj_or_ex(self, elem_locator: str, find_meth: str):
        """Функция для получения объекта элемента"""
        elem_obj = None
        time.sleep(0.2)
        if find_meth == 'ID':
            elem_obj = self.driver.find_element(By.ID, self.locators[elem_locator])
        elif find_meth == 'CLASS_NAME':
            elem_obj = self.driver.find_element(By.CLASS_NAME, self.locators[elem_locator])
        elif find_meth == 'SELECTOR':
            elem_obj = self.driver.find_element(By.CSS_SELECTOR, self.locators[elem_locator])
        elif find_meth == 'XPATH':
            elem_obj = self.driver.find_element(By.XPATH, self.locators[elem_locator])
        elif find_meth == 'NAME':
            elem_obj = self.driver.find_element(By.NAME, self.locators[elem_locator])
        if elem_obj:
            return elem_obj
        else:
            return False

    def get_date_18_years_ago(self):
        """Функция для получения даты 18 лет назад от текущей"""
        present_date = datetime.datetime.now().strftime("%d/%m/%Y")
        present_y = int(present_date[-4:])
        eigtheen_y_ago = present_y - 18
        date_eighteen_y_ago = datetime.datetime(eigtheen_y_ago, int(present_date[3:5]), int(present_date[:2]))

        return date_eighteen_y_ago

    def check_exists_elem(self, elem_locator:str, find_meth:str):
        """Функция для проверки наличия элемента на странице"""
        if find_meth == 'NAME':
            try:
                self.driver.find_element(By.NAME, elem_locator)
            except NoSuchElementException:
                return False
            return True
        elif find_meth == 'XPATH':
            try:
                self.driver.find_element(By.XPATH, elem_locator)
            except NoSuchElementException:
                return False
            return True
        elif find_meth == 'ID':
            try:
                self.driver.find_element(By.ID, elem_locator)
            except NoSuchElementException:
                return False
            return True
        elif find_meth == 'SELECTOR':
            try:
                self.driver.find_element(By.CSS_SELECTOR, elem_locator)
            except NoSuchElementException:
                return False
            return True

# метод делает скриншот страницы
    def screen_shot(self):
        self.driver.get_screenshot_as_file("screenshot.png")

# метод скроллит страницу
    def scroll_by_pix(self):
        self.driver.execute_script("window.scrollBy(0,100)", "")