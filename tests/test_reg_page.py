# Импортируем библиотеку pytest для работы с фикстурами
import allure
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from conftest import browser
from data_conf import data_test_possitive as dtp
from data_conf import data_test_negotive as dtn


@allure.feature('Проверки валидации поля Фамилия')
class TestLastNameField:
    @allure.story('Позитивные проверки валидации фамилии поо кол-ву символов')
    @pytest.mark.parametrize('last_name',
                            dtp.ALLNAME_FLD_LEN_POSSITIVE[0],
                            ids=dtp.ALLNAME_FLD_LEN_POSSITIVE[1])
    def test_lname_len_valid_possitive(self, login_patient, last_name):
        """Позитивные проверки валидации фамилии поо кол-ву символов"""

        login_patient.click_element('PROFL_BTN_XP',
                           'XPATH')

        login_patient.fill_the_field('LNAME_XP',
                            last_name['INPUT'],
                            'XPATH')
        err_mess = str(login_patient.get_elem_obj_or_ex('ER_MESS_LNAME_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess == ''


    @allure.story('Позитивные проверки валидации фамилии по типу принимаемых символов')
    @pytest.mark.parametrize('last_name',
                         dtp.ALLNAME_FLD_SYMB_POSSITIVE[0],
                         ids=dtp.ALLNAME_FLD_SYMB_POSSITIVE[1])
    def test_lname_symbols_valid_possitive(self, login_patient, last_name):
        """Позитивные проверки валидации фамилии по вводимым символам"""

        login_patient.click_element('PROFL_BTN_XP',
                           'XPATH')

        login_patient.fill_the_field('LNAME_XP',
                            last_name['INPUT'],
                            'XPATH')
        err_mess = str(login_patient.get_elem_obj_or_ex('ER_MESS_LNAME_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess == ''

    @allure.story('Позитивные проверки удаления пробелов в начале и в конце')
    @pytest.mark.parametrize('last_name',
                         dtp.ALLNAME_FLD_SPACE_DELETE[0],
                         ids=dtp.ALLNAME_FLD_SPACE_DELETE[1])
    def test_lname_space_del_possitive(self, login_patient, last_name):
        """Позитивные проверки удаления пробела в начале и в конце"""

        login_patient.click_element('PROFL_BTN_XP',
                           'XPATH')

        login_patient.fill_the_field('LNAME_XP',
                            last_name['INPUT'],
                            'XPATH')
        login_patient.click_element('PRFL_TTL_CLS',
                        'CLASS_NAME')
        field_fact_data = str(login_patient.get_elem_obj_or_ex('LNAME_XP', 'XPATH').get_attribute('value'))

        assert field_fact_data == str(last_name['INPUT']).strip()

    @allure.story('Позитивные проверки сохранения ввода в том регистре, как ввел юзер')
    @pytest.mark.parametrize('last_name',
                         dtp.ALLNAME_FLD_TEXT_REGISTR[0],
                         ids=dtp.ALLNAME_FLD_TEXT_REGISTR[1])
    def test_lname_text_registr_possitive(self, login_patient, last_name):
        """Позитивные проверки сохранения текста в том регистре, в каком его ввел юзер"""

        login_patient.click_element('PROFL_BTN_XP',
                           'XPATH')
        login_patient.fill_the_field('LNAME_XP',
                            last_name['INPUT'],
                            'XPATH')
        login_patient.click_element('PRFL_TTL_CLS',
                        'CLASS_NAME')
        # time.sleep(2)
        field_fact_data = str(login_patient.get_elem_obj_or_ex('LNAME_XP', 'XPATH').get_attribute('value'))

        assert field_fact_data == str(last_name['INPUT'])

    @allure.story('Негативные проверки валидации минимального кол-ва символов')
    @pytest.mark.parametrize('last_name',
                         dtn.ALLNAME_FLD_MIN_LEN[0],
                         ids=dtn.ALLNAME_FLD_MIN_LEN[1])
    def test_lname_valid_min_len_negotive(self, login_patient, last_name):
        """Негативные проверки валидации фамилии по минимальному кол-ву символов"""

        login_patient.click_element('PROFL_BTN_XP',
                           'XPATH')
        login_patient.fill_the_field('LNAME_XP',
                            last_name['INPUT'],
                            'XPATH')
        # time.sleep(3)
        err_mess = str(login_patient.get_elem_obj_or_ex('ER_MESS_LNAME_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess == 'Минимальная длина: 3 символа'

    @allure.story('Негативные проверки валидации максимального кол-ва символов')
    @pytest.mark.parametrize('last_name',
                         dtn.ALLNAME_FLD_MAX_LEN[0],
                         ids=dtn.ALLNAME_FLD_MAX_LEN[1])
    def test_lname_valid_max_len_negotive(self, login_patient, last_name):
        """Негативные проверки валидации фамилии по максимальному кол-ву символов"""

        login_patient.click_element('PROFL_BTN_XP',
                           'XPATH')
        login_patient.fill_the_field('LNAME_XP',
                            last_name['INPUT'],
                            'XPATH')
        err_mess = str(login_patient.get_elem_obj_or_ex('ER_MESS_LNAME_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess == 'Максимальная длина: 30 символов'


@allure.feature('Проверки валидации поля Имя')
class TestFirstNameField:
    @allure.story('Позитивные проверки валидации имени по кол-ву символов')
    @pytest.mark.parametrize('first_name',
                            dtp.ALLNAME_FLD_LEN_POSSITIVE[0],
                            ids=dtp.ALLNAME_FLD_LEN_POSSITIVE[1])
    def test_fname_len_valid_possitive(self, login_patient, first_name):
        """Позитивные проверки валидации имени по кол-ву символов"""

        login_patient.click_element('PROFL_BTN_XP',
                           'XPATH')

        login_patient.fill_the_field('FNAME_XP',
                            first_name['INPUT'],
                            'XPATH')
        err_mess = str(login_patient.get_elem_obj_or_ex('ER_MESS_FNAME_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess == ''


    @allure.story('Позитивные проверки валидации имени по типу принимаемых символов')
    @pytest.mark.parametrize('first_name',
                         dtp.ALLNAME_FLD_SYMB_POSSITIVE[0],
                         ids=dtp.ALLNAME_FLD_SYMB_POSSITIVE[1])
    def test_fname_symbols_valid_possitive(self, login_patient, first_name):
        """Позитивные проверки валидации имени по вводимым символам"""

        login_patient.click_element('PROFL_BTN_XP',
                           'XPATH')

        login_patient.fill_the_field('FNAME_XP',
                            first_name['INPUT'],
                            'XPATH')
        err_mess = str(login_patient.get_elem_obj_or_ex('ER_MESS_FNAME_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess == ''

    @allure.story('Позитивные проверки удаления пробелов в начале и в конце')
    @pytest.mark.parametrize('first_name',
                         dtp.ALLNAME_FLD_SPACE_DELETE[0],
                         ids=dtp.ALLNAME_FLD_SPACE_DELETE[1])
    def test_fname_space_del_possitive(self, login_patient, first_name):
        """Позитивные проверки удаления пробела в начале и в конце"""

        login_patient.click_element('PROFL_BTN_XP',
                           'XPATH')

        login_patient.fill_the_field('FNAME_XP',
                            first_name['INPUT'],
                            'XPATH')
        login_patient.click_element('PRFL_TTL_CLS',
                        'CLASS_NAME')
        field_fact_data = str(login_patient.get_elem_obj_or_ex('FNAME_XP', 'XPATH').get_attribute('value'))

        assert field_fact_data == str(first_name['INPUT']).strip()

    @allure.story('Позитивные проверки сохранения ввода в том регистре, как ввел юзер')
    @pytest.mark.parametrize('first_name',
                         dtp.ALLNAME_FLD_TEXT_REGISTR[0],
                         ids=dtp.ALLNAME_FLD_TEXT_REGISTR[1])
    def test_fname_text_registr_possitive(self, login_patient, first_name):
        """Позитивные проверки сохранения текста в том регистре, в каком его ввел юзер"""

        login_patient.click_element('PROFL_BTN_XP',
                           'XPATH')
        login_patient.fill_the_field('FNAME_XP',
                            first_name['INPUT'],
                            'XPATH')
        login_patient.click_element('PRFL_TTL_CLS',
                        'CLASS_NAME')
        # time.sleep(2)
        field_fact_data = str(login_patient.get_elem_obj_or_ex('FNAME_XP', 'XPATH').get_attribute('value'))

        assert field_fact_data == str(first_name['INPUT'])

    @allure.story('Негативные проверки валидации минимального кол-ва символов')
    @pytest.mark.parametrize('first_name',
                         dtn.ALLNAME_FLD_MIN_LEN[0],
                         ids=dtn.ALLNAME_FLD_MIN_LEN[1])
    def test_fname_valid_min_len_negotive(self, login_patient, first_name):
        """Негативные проверки валидации имени по минимальному кол-ву символов"""

        login_patient.click_element('PROFL_BTN_XP',
                           'XPATH')
        login_patient.fill_the_field('FNAME_XP',
                            first_name['INPUT'],
                            'XPATH')
        # time.sleep(3)
        err_mess = str(login_patient.get_elem_obj_or_ex('ER_MESS_FNAME_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess == 'Минимальная длина: 3 символа'

    @allure.story('Негативные проверки валидации максимального кол-ва символов')
    @pytest.mark.parametrize('first_name',
                         dtn.ALLNAME_FLD_MAX_LEN[0],
                         ids=dtn.ALLNAME_FLD_MAX_LEN[1])
    def test_fname_valid_max_len_negotive(self, login_patient, first_name):
        """Негативные проверки валидации имени по максимальному кол-ву символов"""

        login_patient.click_element('PROFL_BTN_XP',
                           'XPATH')
        login_patient.fill_the_field('FNAME_XP',
                            first_name['INPUT'],
                            'XPATH')
        err_mess = str(login_patient.get_elem_obj_or_ex('ER_MESS_FNAME_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess == 'Максимальная длина: 30 символов'


@allure.feature('Проверки валидации поля Отчество')
class TestPatronField:
    @allure.story('Позитивные проверки валидации  отчества по кол-ву символов')
    @pytest.mark.parametrize('patronymic',
                            dtp.ALLNAME_FLD_LEN_POSSITIVE[0],
                            ids=dtp.ALLNAME_FLD_LEN_POSSITIVE[1])
    def test_patron_len_valid_possitive(self, login_patient, patronymic):
        """Позитивные проверки валидации отчества по кол-ву символов"""

        login_patient.click_element('PROFL_BTN_XP',
                                        'XPATH')

        login_patient.fill_the_field('PATRONYMIC_XP',
                                         patronymic['INPUT'],
                                         'XPATH')
        err_mess = str(
                login_patient.get_elem_obj_or_ex('ER_MESS_PATRON_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess == ''

    @allure.story('Позитивные проверки валидации отчества по типу принимаемых символов')
    @pytest.mark.parametrize('patronymic',
                            dtp.ALLNAME_FLD_SYMB_POSSITIVE[0],
                            ids=dtp.ALLNAME_FLD_SYMB_POSSITIVE[1])
    def test_patron_symbols_valid_possitive(self, login_patient, patronymic):
        """Позитивные проверки валидации отчества по вводимым символам"""

        login_patient.click_element('PROFL_BTN_XP',
                                        'XPATH')

        login_patient.fill_the_field('PATRONYMIC_XP',
                                         patronymic['INPUT'],
                                         'XPATH')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_PATRON_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess == ''

    @allure.story('Позитивные проверки удаления пробелов в начале и в конце')
    @pytest.mark.parametrize('patronymic',
                            dtp.ALLNAME_FLD_SPACE_DELETE[0],
                            ids=dtp.ALLNAME_FLD_SPACE_DELETE[1])
    def test_patron_space_del_possitive(self, login_patient, patronymic):
        """Позитивные проверки удаления пробела в начале и в конце"""

        login_patient.click_element('PROFL_BTN_XP',
                                        'XPATH')

        login_patient.fill_the_field('PATRONYMIC_XP',
                                         patronymic['INPUT'],
                                         'XPATH')
        login_patient.click_element('PRFL_TTL_CLS',
                                        'CLASS_NAME')
        field_fact_data = str(login_patient.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').get_attribute('value'))

        assert field_fact_data == str(patronymic['INPUT']).strip()

    @allure.story('Позитивные проверки сохранения ввода в том регистре, как ввел юзер')
    @pytest.mark.parametrize('patronymic',
                            dtp.ALLNAME_FLD_TEXT_REGISTR[0],
                            ids=dtp.ALLNAME_FLD_TEXT_REGISTR[1])
    def test_patron_text_registr_possitive(self, login_patient, patronymic):
        """Позитивные проверки сохранения текста в том регистре, в каком его ввел юзер"""

        login_patient.click_element('PROFL_BTN_XP',
                                        'XPATH')
        login_patient.fill_the_field('PATRONYMIC_XP',
                                         patronymic['INPUT'],
                                         'XPATH')
        login_patient.click_element('PRFL_TTL_CLS',
                                        'CLASS_NAME')
        # time.sleep(2)
        field_fact_data = str(login_patient.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').get_attribute('value'))

        assert field_fact_data == str(patronymic['INPUT'])

    @allure.story('Негативные проверки валидации минимального кол-ва символов')
    @pytest.mark.parametrize('patronymic',
                            dtn.ALLNAME_FLD_MIN_LEN[0],
                            ids=dtn.ALLNAME_FLD_MIN_LEN[1])
    def test_patron_valid_min_len_negotive(self, login_patient, patronymic):
        """Негативные проверки валидации отчества по минимальному кол-ву символов"""

        login_patient.click_element('PROFL_BTN_XP',
                                        'XPATH')
        login_patient.fill_the_field('PATRONYMIC_XP',
                                         patronymic['INPUT'],
                                         'XPATH')
        # time.sleep(3)
        err_mess = str(
                login_patient.get_elem_obj_or_ex('ER_MESS_PATRON_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess == 'Минимальная длина: 3 символа'

    @allure.story('Негативные проверки валидации максимального кол-ва символов')
    @pytest.mark.parametrize('patronymic',
                            dtn.ALLNAME_FLD_MAX_LEN[0],
                            ids=dtn.ALLNAME_FLD_MAX_LEN[1])
    def test_patron_valid_max_len_negotive(self, login_patient, patronymic):
        """Негативные проверки валидации отчества по максимальному кол-ву символов"""

        login_patient.click_element('PROFL_BTN_XP',
                                        'XPATH')
        login_patient.fill_the_field('PATRONYMIC_XP',
                                         patronymic['INPUT'],
                                         'XPATH')
        err_mess = str(
                login_patient.get_elem_obj_or_ex('ER_MESS_PATRON_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess == 'Максимальная длина: 30 символов'
