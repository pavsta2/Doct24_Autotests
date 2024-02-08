import time, datetime

from selenium.webdriver.common.by import By
from datetime import timedelta
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import locators_patient


# Регистрируем класс, который будет описывать вэб страницу
class RegPage:

    def __init__(self, driver, locators):
        self.driver = driver
        self.locators = locators

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
        time.sleep(0.3)
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