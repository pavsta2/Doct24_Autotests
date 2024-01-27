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
from datetime import timedelta


@allure.feature('Проверки валидации поля Фамилия')
class TestLastNameField:
    @allure.story('Позитивные проверки валидации фамилии поо кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.ALLNAME_FLD_LEN_POSSITIVE[0],
                            ids=dtp.ALLNAME_FLD_LEN_POSSITIVE[1])
    def test_lname_len_valid_possitive(self, login_patient, params):
        """Позитивные проверки валидации фамилии поо кол-ву символов"""
        login_patient.get_elem_obj_or_ex('LNAME_XP', 'XPATH').clear()
        login_patient.screen_shot()
        login_patient.fill_the_field('LNAME_XP',
                            params['INPUT'],
                            'XPATH')
        err_mess = str(login_patient.get_elem_obj_or_ex('ER_MESS_LNAME_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess == '', 'При вводе валидных данных появляется ошибка'

    @allure.story('Позитивные проверки валидации фамилии по типу принимаемых символов')
    @pytest.mark.parametrize('params',
                         dtp.ALLNAME_FLD_SYMB_POSSITIVE[0],
                         ids=dtp.ALLNAME_FLD_SYMB_POSSITIVE[1])
    def test_lname_symbols_valid_possitive(self, login_patient, params):
        """Позитивные проверки валидации фамилии по вводимым символам"""
        login_patient.get_elem_obj_or_ex('LNAME_XP', 'XPATH').clear()
        login_patient.fill_the_field('LNAME_XP',
                            params['INPUT'],
                            'XPATH')
        err_mess = str(login_patient.get_elem_obj_or_ex('ER_MESS_LNAME_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess == '', 'При вводе валидных данных появляется ошибка'

    @allure.story('Позитивные проверки удаления пробелов в начале и в конце')
    @pytest.mark.parametrize('params',
                         dtp.ALLNAME_FLD_SPACE_DELETE[0],
                         ids=dtp.ALLNAME_FLD_SPACE_DELETE[1])
    def test_lname_space_del_possitive(self, login_patient, params):
        """Позитивные проверки удаления пробела в начале и в конце"""
        login_patient.get_elem_obj_or_ex('LNAME_XP', 'XPATH').clear()
        login_patient.fill_the_field('LNAME_XP',
                            params['INPUT'],
                            'XPATH')
        login_patient.click_element('LEFT_PAGE_AREA_XPATH',
                                    'XPATH')
        field_fact_data = str(login_patient.get_elem_obj_or_ex('LNAME_XP', 'XPATH').get_attribute('value'))
        assert field_fact_data == str(params['INPUT']).strip(), 'Пробелы не удаляются'

    @allure.story('Позитивные проверки сохранения ввода в том регистре, как ввел юзер')
    @pytest.mark.parametrize('params',
                         dtp.ALLNAME_FLD_TEXT_REGISTR[0],
                         ids=dtp.ALLNAME_FLD_TEXT_REGISTR[1])
    def test_lname_text_registr_possitive(self, login_patient, params):
        """Позитивные проверки сохранения текста в том регистре, в каком его ввел юзер"""
        login_patient.get_elem_obj_or_ex('LNAME_XP', 'XPATH').clear()
        login_patient.fill_the_field('LNAME_XP',
                            params['INPUT'],
                            'XPATH')
        login_patient.click_element('LEFT_PAGE_AREA_XPATH',
                        'XPATH')
        field_fact_data = str(login_patient.get_elem_obj_or_ex('LNAME_XP', 'XPATH').get_attribute('value'))
        assert field_fact_data == str(params['INPUT']), (f"Введенные данные сохраняются не том регистре, в каком ввел"
                                                            f'юзер, expected: {str(params["INPUT"])}, '
                                                            f'fact: {field_fact_data}')

    @allure.story('Негативные проверки валидации минимального кол-ва символов')
    @pytest.mark.parametrize('params',
                         dtn.ALLNAME_FLD_MIN_LEN[0],
                         ids=dtn.ALLNAME_FLD_MIN_LEN[1])
    def test_lname_valid_min_len_negotive(self, login_patient, params):
        """Негативные проверки валидации фамилии по минимальному кол-ву символов"""
        login_patient.get_elem_obj_or_ex('LNAME_XP', 'XPATH').clear()
        login_patient.fill_the_field('LNAME_XP',
                            params['INPUT'],
                            'XPATH')
        err_mess = str(login_patient.get_elem_obj_or_ex('ER_MESS_LNAME_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Минимальная длина: 3 символа', (f'Текст ошибки не соответсвует '
                                                                                   f'требованиям, expected mess: '
                                                                                   f'Минимальная длина: 3 символа, '
                                                                                    f'fact mess: {err_mess}')

    @allure.story('Негативные проверки валидации максимального кол-ва символов')
    @pytest.mark.parametrize('params',
                         dtn.ALLNAME_FLD_MAX_LEN[0],
                         ids=dtn.ALLNAME_FLD_MAX_LEN[1])
    def test_lname_valid_max_len_negotive(self, login_patient, params):
        """Негативные проверки валидации фамилии по максимальному кол-ву символов"""
        login_patient.get_elem_obj_or_ex('LNAME_XP', 'XPATH').clear()
        login_patient.fill_the_field('LNAME_XP',
                            params['INPUT'],
                            'XPATH')
        err_mess = str(login_patient.get_elem_obj_or_ex('ER_MESS_LNAME_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Максимальная длина: 30 символов', (f'Текст ошибки не соответсвует '
                                                                               f'требованиям, expected mess: '
                                                                               f'Максимальная длина: 30 символов, '
                                                                               f'fact mess: {err_mess}')

@allure.feature('Проверки валидации поля Имя')
class TestFirstNameField:
    @allure.story('Позитивные проверки валидации имени по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.ALLNAME_FLD_LEN_POSSITIVE[0],
                            ids=dtp.ALLNAME_FLD_LEN_POSSITIVE[1])
    def test_fname_len_valid_possitive(self, login_patient, params):
        """Позитивные проверки валидации имени по кол-ву символов"""
        login_patient.get_elem_obj_or_ex('FNAME_XP', 'XPATH').clear()
        login_patient.fill_the_field('FNAME_XP',
                            params['INPUT'],
                            'XPATH')
        err_mess = str(login_patient.get_elem_obj_or_ex('ER_MESS_FNAME_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess == '', 'При вводе валидных данных появляется ошибка'


    @allure.story('Позитивные проверки валидации имени по типу принимаемых символов')
    @pytest.mark.parametrize('params',
                         dtp.ALLNAME_FLD_SYMB_POSSITIVE[0],
                         ids=dtp.ALLNAME_FLD_SYMB_POSSITIVE[1])
    def test_fname_symbols_valid_possitive(self, login_patient, params):
        """Позитивные проверки валидации имени по вводимым символам"""
        login_patient.get_elem_obj_or_ex('FNAME_XP', 'XPATH').clear()
        login_patient.fill_the_field('FNAME_XP',
                            params['INPUT'],
                            'XPATH')
        err_mess = str(login_patient.get_elem_obj_or_ex('ER_MESS_FNAME_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess == '', 'При вводе валидных данных появляется ошибка'

    @allure.story('Позитивные проверки удаления пробелов в начале и в конце')
    @pytest.mark.parametrize('params',
                         dtp.ALLNAME_FLD_SPACE_DELETE[0],
                         ids=dtp.ALLNAME_FLD_SPACE_DELETE[1])
    def test_fname_space_del_possitive(self, login_patient, params):
        """Позитивные проверки удаления пробела в начале и в конце"""
        login_patient.get_elem_obj_or_ex('FNAME_XP', 'XPATH').clear()
        login_patient.fill_the_field('FNAME_XP',
                            params['INPUT'],
                            'XPATH')
        login_patient.click_element('LEFT_PAGE_AREA_XPATH',
                        'XPATH')
        field_fact_data = str(login_patient.get_elem_obj_or_ex('FNAME_XP', 'XPATH').get_attribute('value'))
        assert field_fact_data == str(params['INPUT']).strip(), 'Пробелы не удаляются после снятия фокуса'

    @allure.story('Позитивные проверки сохранения ввода в том регистре, как ввел юзер')
    @pytest.mark.parametrize('params',
                         dtp.ALLNAME_FLD_TEXT_REGISTR[0],
                         ids=dtp.ALLNAME_FLD_TEXT_REGISTR[1])
    def test_fname_text_registr_possitive(self, login_patient, params):
        """Позитивные проверки сохранения текста в том регистре, в каком его ввел юзер"""
        login_patient.get_elem_obj_or_ex('FNAME_XP', 'XPATH').clear()
        login_patient.fill_the_field('FNAME_XP',
                            params['INPUT'],
                            'XPATH')
        login_patient.click_element('LEFT_PAGE_AREA_XPATH',
                        'XPATH')
        field_fact_data = str(login_patient.get_elem_obj_or_ex('FNAME_XP', 'XPATH').get_attribute('value'))
        assert field_fact_data == str(params['INPUT']), (f'Ввод сохраняется не в том регистре, в каком ввел юзер, '
                                                         f'expected: str(params["INPUT"]), fact: {field_fact_data}')

    @allure.story('Негативные проверки валидации минимального кол-ва символов')
    @pytest.mark.parametrize('params',
                         dtn.ALLNAME_FLD_MIN_LEN[0],
                         ids=dtn.ALLNAME_FLD_MIN_LEN[1])
    def test_fname_valid_min_len_negotive(self, login_patient, params):
        """Негативные проверки валидации имени по минимальному кол-ву символов"""
        login_patient.get_elem_obj_or_ex('FNAME_XP', 'XPATH').clear()
        login_patient.fill_the_field('FNAME_XP',
                            params['INPUT'],
                            'XPATH')
        err_mess = str(login_patient.get_elem_obj_or_ex('ER_MESS_FNAME_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Минимальная длина: 3 символа', (f'Текст ошибки не соответсвует '
                                                                                  f'требованиям, expected mess: '
                                                                                  f'Минимальная длина: 3 символа, '
                                                                                  f'fact mess: {err_mess}')

    @allure.story('Негативные проверки валидации максимального кол-ва символов')
    @pytest.mark.parametrize('params',
                         dtn.ALLNAME_FLD_MAX_LEN[0],
                         ids=dtn.ALLNAME_FLD_MAX_LEN[1])
    def test_fname_valid_max_len_negotive(self, login_patient, params):
        """Негативные проверки валидации имени по максимальному кол-ву символов"""
        login_patient.get_elem_obj_or_ex('FNAME_XP', 'XPATH').clear()
        login_patient.fill_the_field('FNAME_XP',
                            params['INPUT'],
                            'XPATH')
        err_mess = str(login_patient.get_elem_obj_or_ex('ER_MESS_FNAME_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Максимальная длина: 30 символов', (f'Текст ошибки не соответсвует '
                                                                               f'требованиям, expected mess: '
                                                                               f'Максимальная длина: 30 символов, '
                                                                               f'fact mess: {err_mess}')


@allure.feature('Проверки валидации поля Отчество')
class TestPatronField:
    @allure.story('Позитивные проверки валидации  отчества по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.ALLNAME_FLD_LEN_POSSITIVE[0],
                            ids=dtp.ALLNAME_FLD_LEN_POSSITIVE[1])
    def test_patron_len_valid_possitive(self, login_patient, params):
        """Позитивные проверки валидации отчества по кол-ву символов"""
        login_patient.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').clear()
        login_patient.fill_the_field('PATRONYMIC_XP',
                                         params['INPUT'],
                                         'XPATH')
        err_mess = str(login_patient.get_elem_obj_or_ex('ER_MESS_PATRON_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess == '', 'При вводе валидных данных возникает ошибка'

    @allure.story('Позитивные проверки валидации отчества по типу принимаемых символов')
    @pytest.mark.parametrize('params',
                            dtp.ALLNAME_FLD_SYMB_POSSITIVE[0],
                            ids=dtp.ALLNAME_FLD_SYMB_POSSITIVE[1])
    def test_patron_symbols_valid_possitive(self, login_patient, params):
        """Позитивные проверки валидации отчества по вводимым символам"""
        login_patient.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').clear()
        login_patient.fill_the_field('PATRONYMIC_XP',
                                         params['INPUT'],
                                         'XPATH')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_PATRON_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess == '', 'При вводе валидных данных появляется ошибка'

    @allure.story('Позитивные проверки удаления пробелов в начале и в конце')
    @pytest.mark.parametrize('params',
                            dtp.ALLNAME_FLD_SPACE_DELETE[0],
                            ids=dtp.ALLNAME_FLD_SPACE_DELETE[1])
    def test_patron_space_del_possitive(self, login_patient, params):
        """Позитивные проверки удаления пробела в начале и в конце"""
        login_patient.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').clear()
        login_patient.fill_the_field('PATRONYMIC_XP',
                                         params['INPUT'],
                                         'XPATH')
        login_patient.click_element('LEFT_PAGE_AREA_XPATH',
                                        'XPATH')
        field_fact_data = str(login_patient.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').get_attribute('value'))
        assert field_fact_data == str(params['INPUT']).strip(), 'Пробелы не удаляются после снятия фокуса'

    @allure.story('Позитивные проверки сохранения ввода в том регистре, как ввел юзер')
    @pytest.mark.parametrize('params',
                            dtp.ALLNAME_FLD_TEXT_REGISTR[0],
                            ids=dtp.ALLNAME_FLD_TEXT_REGISTR[1])
    def test_patron_text_registr_possitive(self, login_patient, params):
        """Позитивные проверки сохранения текста в том регистре, в каком его ввел юзер"""
        login_patient.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').clear()
        login_patient.fill_the_field('PATRONYMIC_XP',
                                         params['INPUT'],
                                         'XPATH')
        login_patient.click_element('LEFT_PAGE_AREA_XPATH',
                                        'XPATH')
        field_fact_data = str(login_patient.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').get_attribute('value'))
        assert field_fact_data == str(params['INPUT']), 'Ввод сохраняется не в том регистре, в каком ввел юзер'

    @allure.story('Негативные проверки валидации минимального кол-ва символов')
    @pytest.mark.parametrize('params',
                            dtn.ALLNAME_FLD_MIN_LEN[0],
                            ids=dtn.ALLNAME_FLD_MIN_LEN[1])
    def test_patron_valid_min_len_negotive(self, login_patient, params):
        """Негативные проверки валидации отчества по минимальному кол-ву символов"""
        login_patient.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').clear()
        login_patient.fill_the_field('PATRONYMIC_XP',
                                         params['INPUT'],
                                         'XPATH')
        err_mess = str(
                login_patient.get_elem_obj_or_ex('ER_MESS_PATRON_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Минимальная длина: 3 символа', (f'Текст ошибки не соответсвует '
                                                                               f'требованиям, expected mess: '
                                                                               f'Минимальная длина: 3 символа, '
                                                                               f'fact mess: {err_mess}')

    @allure.story('Негативные проверки валидации максимального кол-ва символов')
    @pytest.mark.parametrize('params',
                            dtn.ALLNAME_FLD_MAX_LEN[0],
                            ids=dtn.ALLNAME_FLD_MAX_LEN[1])
    def test_patron_valid_max_len_negotive(self, login_patient, params):
        """Негативные проверки валидации отчества по максимальному кол-ву символов"""
        login_patient.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').clear()
        login_patient.fill_the_field('PATRONYMIC_XP',
                                         params['INPUT'],
                                         'XPATH')
        err_mess = str(
                login_patient.get_elem_obj_or_ex('ER_MESS_PATRON_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Максимальная длина: 30 символов', (f'Текст ошибки не соответсвует '
                                                                               f'требованиям, expected mess: '
                                                                               f'Максимальная длина: 30 символов, '
                                                                               f'fact mess: {err_mess}')


@allure.feature('Проверки валидации поля Дата рождения')
class TestDBirthField:
    @allure.story('Позитивные проверки ввода валидной даты рождения')
    @pytest.mark.parametrize('params',
                            dtp.DBIRTH_FLD_POSSITIVE[0],
                            ids=dtp.DBIRTH_FLD_POSSITIVE[1])
    def test_birthdate_valid_possitive(self, login_patient, params):
        """Позитивные проверки ввода валидной даты рождения"""
        login_patient.get_elem_obj_or_ex('DBIRTH_FLD_NM','NAME').clear()
        login_patient.fill_the_field('DBIRTH_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        date_inserted = login_patient.get_elem_obj_or_ex('DBIRTH_FLD_NM','NAME').get_attribute('value')
        assert date_inserted == params['INPUT'], 'Ввод сохраняется не так, как ввел пользователь'

        err_mess = str(
                login_patient.get_elem_obj_or_ex('ER_MESS_DBIRTH_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess == '', 'При вводе валидных данных появляется ошибка'

    @allure.story('Негативные проверки ввода невалидной даты рождения')
    @pytest.mark.parametrize('params',
                             dtn.DBIRTH_FLD_UNVALID[0],
                             ids=dtn.DBIRTH_FLD_UNVALID[1])
    def test_birthdate_valid_negotive(self, login_patient, params):
        """Негативные проверки ввода невалидной даты рождения"""
        login_patient.get_elem_obj_or_ex('DBIRTH_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('DBIRTH_FLD_NM',
                                     params['INPUT'],
                                     'NAME')

        date_inserted = login_patient.get_elem_obj_or_ex('DBIRTH_FLD_NM', 'NAME').get_attribute('value')
        assert date_inserted == params['INPUT'], 'Ввод сохраняется не так, как ввел пользователь'

        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_DBIRTH_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Некорректная дата', (f'Текст ошибки не соответсвует '
                                                                               f'требованиям, expected mess: '
                                                                               f'Некорректная дата, '
                                                                               f'fact mess: {err_mess}')

    @allure.story('Позитивная проверка ввода даты рождения при которой юзеру ровно 18 лет')
    def test_birthdate_eq_18(self, login_patient):
        """Позитивные проверки ввода даты рождения, при которой юзеру ровно 18"""
        # очищаем поле
        login_patient.get_elem_obj_or_ex('DBIRTH_FLD_NM', 'NAME').clear()
        # получаем дату 18 лет назад от текущей
        birthdate_to_test = login_patient.get_date_18_years_ago().strftime("%d/%m/%Y")
        # вносим полученную дату
        login_patient.fill_the_field('DBIRTH_FLD_NM',
                                     birthdate_to_test,
                                     'NAME')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_DBIRTH_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess == '', 'При вводе валидной даты появляется соощение об ошибке'

    @allure.story('Позитивная проверка ввода даты рождения при которой юзер старше 18 лет')
    def test_birthdate_more_then_18(self, login_patient):
        """Позитивные проверки ввода даты рождения, при которой юзер старше 18"""
        # очищаем поле
        login_patient.get_elem_obj_or_ex('DBIRTH_FLD_NM', 'NAME').clear()
        # получаем дату 18 лет назад и еще минус один день
        birthdate_to_test = (login_patient.get_date_18_years_ago() - timedelta(days=1)).strftime("%d/%m/%Y")
        # вводим полученную дату
        login_patient.fill_the_field('DBIRTH_FLD_NM',
                                     birthdate_to_test,
                                     'NAME')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_DBIRTH_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess == '', 'При вводе валидной даты появляется сообщение об ошибке'

    @allure.story('Негативная проверка ввода даты рождения при которой юзер младше 18 лет')
    def test_birthdate_less_then_18(self, login_patient):
        """Позитивные проверки ввода даты рождения, при которой юзер младше 18"""
        # очищаем поле
        login_patient.get_elem_obj_or_ex('DBIRTH_FLD_NM', 'NAME').clear()
        birthdate_to_test = (login_patient.get_date_18_years_ago() + timedelta(days=1)).strftime("%d/%m/%Y")
        login_patient.fill_the_field('DBIRTH_FLD_NM',
                                     birthdate_to_test,
                                     'NAME')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_DBIRTH_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess == 'Нельзя зарегистрироваться на сайте, если Вам меньше 18 лет'
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Нелья зарегистрироваться на сайте, если Вам меньше 18 лет', \
            (f'Текст ошибки не соответсвует требованиям, expected mess: Нельзя зарегистрироваться на сайте, если Вам'
             f'меньше 18 лет, fact mess: {err_mess}')

@allure.feature('Проверки валидации поля Email')
class TestEmailField:
    @allure.story('Позитивные проверки валидации email по кол-ву симовлов')
    @pytest.mark.parametrize('params',
                            dtp.EMAIL_FLD_LEN[0],
                            ids=dtp.EMAIL_FLD_LEN[1])
    def test_email_len_valid_possitive(self, login_patient, params):
        """Позитивные проверки валидации поля Email по кол-ву символов"""
        login_patient.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('EMAIL_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        err_mess = str(
                login_patient.get_elem_obj_or_ex('ER_MESS_EMAIL_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess == '', 'При вводе валидныз данных появляется ошибка'

    @allure.story('Позитивные проверки валидации email по типу вводимых симовлов')
    @pytest.mark.parametrize('params',
                             dtp.EMAIL_FLD_SYMB[0],
                             ids=dtp.EMAIL_FLD_SYMB[1])
    def test_email_symb_valid_possitive(self, login_patient, params):
        """Позитивные проверки валидации поля Email по типу вводимых символов"""
        login_patient.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('EMAIL_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_EMAIL_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess == '', 'При вводе валидных данный появляется ошибка'

    @allure.story('Негативные проверки валидации email по кол-ву симовлов')
    @pytest.mark.parametrize('params',
                             dtn.EMAIL_FLD_LEN[0],
                             ids=dtn.EMAIL_FLD_LEN[1])
    def test_email_len_valid_negotive(self, login_patient, params):
        """Негативные проверки валидации поля Email по кол-ву символов"""
        login_patient.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('EMAIL_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_EMAIL_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Длина E-mail не может быть менее 6 и более 70 символов', \
            (f'Текст ошибки не соответсвует требованиям, expected mess: Длина E-mail не может быть менее 6 и более'
             f'70 символов, fact mess: {err_mess}')

    @allure.story('Негативные проверки валидации email по маске')
    @pytest.mark.parametrize('params',
                             dtn.EMAIL_FLD_MASK[0],
                             ids=dtn.EMAIL_FLD_MASK[1])
    def test_email_mask_valid_negotive(self, login_patient, params):
        """Негативные проверки валидации поля Email по кол-ву символов"""
        login_patient.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('EMAIL_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_EMAIL_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Допустимый формат почты: test@test.ru', \
            (f'Текст ошибки не соответсвует требованиям, expected mess: Допустимый формат почты: test@test.ru, '
                                                                               f'fact mess: {err_mess}')

    @allure.story('Позитивные проверки удаления пробелов в начале и в конце')
    @pytest.mark.parametrize('params',
                             dtp.EMAIL_FLD_SPACE_DELETE[0],
                             ids=dtp.EMAIL_FLD_SPACE_DELETE[1])
    def test_email_space_del_possitive(self, login_patient, params):
        """Позитивные проверки удаления пробела в начале и в конце"""
        login_patient.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('EMAIL_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        login_patient.click_element('LEFT_PAGE_AREA_XPATH',
                                    'XPATH')
        field_fact_data = str(login_patient.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').get_attribute('value'))
        assert field_fact_data == str(params['INPUT']).strip(), 'При вводе пробелы не удаляются'


@allure.feature('Проверки валидации поля Рост')
class TestHeightField:
    @allure.story('Позитивные проверки валидации поля Роста')
    @pytest.mark.parametrize('params',
                            dtp.HEIGHT_FLD[0],
                            ids=dtp.HEIGHT_FLD[1])
    def test_height_valid_possitive(self, login_patient, params):
        """Позитивные проверки валидации поля Роста"""
        login_patient.get_elem_obj_or_ex('HEIGHT_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('HEIGHT_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        inserted = login_patient.get_elem_obj_or_ex('HEIGHT_FLD_NM', 'NAME').get_attribute('value')

        assert inserted == params['INPUT'], (f'Ввод НЕ сохраняется в том виде, в каком ввел юзер, expected: '
                                             f'{params["INPUT"]}, fact: {inserted}')

    @allure.story('Негативные проверки валидации поля при воде более 3 цифр в поле Роста')
    @pytest.mark.parametrize('params',
                             dtn.HEIGHT_FLD_LEN[0],
                             ids=dtn.HEIGHT_FLD_LEN[1])
    def test_height_len_valid_negotive(self, login_patient, params):
        """Негативные проверки валидации поля при воде более 3 цифр в поле Роста"""

        login_patient.get_elem_obj_or_ex('HEIGHT_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('HEIGHT_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_patient.get_elem_obj_or_ex('HEIGHT_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'][0:3], (f"Можно ввести невалидные данные, expected: {params['INPUT'][:-1]},"
                                                  f"fact: {inserted}")

    @allure.story('Негативные проверки валидации поля Роста по типу символов')
    @pytest.mark.parametrize('params',
                             dtn.HEIGHT_FLD_SYMB[0],
                             ids=dtn.HEIGHT_FLD_SYMB[1])
    def test_height_symb_valid_negotive(self, login_patient, params):
        """Негативные проверки валидации поля Роста по типу символов"""

        login_patient.get_elem_obj_or_ex('HEIGHT_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('HEIGHT_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_patient.get_elem_obj_or_ex('HEIGHT_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == '', 'Можно ввести невалидные символы'


@allure.feature('Проверки валидации поля Вес')
class TestWeightField:
    @allure.story('Позитивные проверки валидации поля Вес')
    @pytest.mark.parametrize('params',
                            dtp.WEIGHT_FLD[0],
                            ids=dtp.WEIGHT_FLD[1])
    def test_weight_valid_possitive(self, login_patient, params):
        """Позитивные проверки валидации поля Вес"""

        login_patient.get_elem_obj_or_ex('WEIGHT_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('WEIGHT_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        inserted = login_patient.get_elem_obj_or_ex('WEIGHT_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], 'Ввод сохраняется не в том виде, как ввел пользователь'

    @allure.story('Негативные проверки валидации поля Вес по кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.WEIGHT_FLD_LEN[0],
                             ids=dtn.WEIGHT_FLD_LEN[1])
    def test_weight_len_valid_negotive(self, login_patient, params):
        """Негативные проверки валидации поля Вес по кол-ву символов"""

        login_patient.get_elem_obj_or_ex('WEIGHT_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('WEIGHT_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        height_inserted = login_patient.get_elem_obj_or_ex('WEIGHT_FLD_NM', 'NAME').get_attribute('value')
        assert height_inserted == params['INPUT'][0:3], (f'При вводе 4-х знач числа, 4-й символ в поле должен '
                                                         f'обрезаться и в поле оставаться 3-х знач число, но expected:'
                                                         f' {params["INPUT"][0:3]}, '
                                                         f'fact: {height_inserted} !')

    @allure.story('Негативные проверки валидации поля Вес по типу символов')
    @pytest.mark.parametrize('params',
                             dtn.WEIGHT_FLD_SYMB[0],
                             ids=dtn.WEIGHT_FLD_SYMB[1])
    def test_weight_symb_valid_negotive(self, login_patient, params):
        """Негативные проверки валидации поля Вес по типу символов"""

        login_patient.get_elem_obj_or_ex('WEIGHT_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('WEIGHT_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        height_inserted = login_patient.get_elem_obj_or_ex('WEIGHT_FLD_NM', 'NAME').get_attribute('value')
        assert height_inserted == '', 'можно ввести НЕ цифры в качестве значения веса'


@allure.feature('Проверки валидации поля Аллерген')
class TestAllergenField:
    @allure.story('Позитивные проверки валидации поля Аллерген по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.ALLERGEN_FLD_LEN[0],
                            ids=dtp.ALLERGEN_FLD_LEN[1])
    def test_allergen_len_valid_possitive(self, login_patient, params, open_allegry_section):
        """Позитивные проверки валидации поля Аллерген по кол-ву символов"""

        login_patient.get_elem_obj_or_ex('ALLRGEN_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('ALLRGEN_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        allergen_inserted = login_patient.get_elem_obj_or_ex('ALLRGEN_FLD_NM', 'NAME').get_attribute('value')
        assert allergen_inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {allergen_inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_ALLERGEN_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess == '', 'при вводе валидного кол-ва символов появл ошибка'

    @allure.story('Негативные проверки валидации поля Аллерген по min кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.ALLERGEN_FLD_MIN_LEN[0],
                             ids=dtn.ALLERGEN_FLD_MIN_LEN[1])
    def test_allergen_min_len_valid_negotive(self, login_patient, params, open_allegry_section):
        """Негативные проверки валидации поля Аллерген по min кол-ву символов"""
        login_patient.get_elem_obj_or_ex('ALLRGEN_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('ALLRGEN_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        allergen_inserted = login_patient.get_elem_obj_or_ex('ALLRGEN_FLD_NM', 'NAME').get_attribute('value')
        assert allergen_inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {allergen_inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_ALLERGEN_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Минимальная длина: 2 символа', ('Текст ошибки не соответсвует '
                                                                               'требованиям ')

    @allure.story('Негативные проверки валидации поля Аллерген по max кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.ALLERGEN_FLD_MAX_LEN[0],
                             ids=dtn.ALLERGEN_FLD_MAX_LEN[1])
    def test_allergen_max_len_valid_negotive(self, login_patient, params, open_allegry_section):
        """Негативные проверки валидации поля Аллерген по max кол-ву символов"""
        login_patient.get_elem_obj_or_ex('ALLRGEN_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('ALLRGEN_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        allergen_inserted = login_patient.get_elem_obj_or_ex('ALLRGEN_FLD_NM', 'NAME').get_attribute('value')
        assert allergen_inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                      f'fact input: {allergen_inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_ALLERGEN_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Максимальная длина: 50 символов', \
            (f'Текст ошибки не соответсвует требованиям. Expected: Максимальная длина: 50 символов, fact:'
             f'{err_mess} ')

    @allure.story('Позитивные проверки валидации поля Аллерген по типам символов')
    @pytest.mark.parametrize('params',
                             dtp.ALLERGEN_FLD_SYMB[0],
                             ids=dtp.ALLERGEN_FLD_SYMB[1])
    def test_allergen_symb_valid_possitive(self, login_patient, params, open_allegry_section):
        """Позитивные проверки валидации поля Аллерген по типам символов"""
        login_patient.get_elem_obj_or_ex('ALLRGEN_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('ALLRGEN_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        allergen_inserted = login_patient.get_elem_obj_or_ex('ALLRGEN_FLD_NM', 'NAME').get_attribute('value')
        assert allergen_inserted == params['INPUT'], (
            f'введенный текст отображается не так как ожидалось, expected input: {params["INPUT"]}, '
            f'fact input: {allergen_inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_ALLERGEN_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess == '', 'при вводе валидных типов символов появл ошибка'

@allure.feature('Проверки валидации поля Реакция (на аллерген)')
class TestReactionField:
    @allure.story('Позитивные проверки валидации поля Реакция по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.REACTION_FLD_LEN[0],
                            ids=dtp.REACTION_FLD_LEN[1])
    def test_reaction_len_valid_possitive(self, login_patient, params, open_allegry_section):
        """Позитивные проверки валидации поля Реакция по кол-ву символов"""

        login_patient.get_elem_obj_or_ex('REACTION_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('REACTION_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        value_inserted = login_patient.get_elem_obj_or_ex('REACTION_FLD_NM', 'NAME').get_attribute('value')
        assert value_inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {value_inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_REACTION_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess == '', f'При вводе валидного кол-ва символов появл ошибка: {err_mess}'

    @allure.story('Негативные проверки валидации поля Реакция по минимальному кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.REACTION_FLD_MIN_LEN[0],
                             ids=dtn.REACTION_FLD_MIN_LEN[1])
    def test_reaction_min_len_valid_negotive(self, login_patient, params, open_allegry_section):
        """Негативные проверки валидации поля Реакция по минимальному кол-ву символов"""

        login_patient.get_elem_obj_or_ex('REACTION_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('REACTION_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        value_inserted = login_patient.get_elem_obj_or_ex('REACTION_FLD_NM', 'NAME').get_attribute('value')
        assert value_inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {value_inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_REACTION_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Минимальная длина: 2 символа', \
            (f'Текст ошибки не соответсвует требованиям, expected: Минимальная длина: 2 символа, fact: {err_mess}')

    @allure.story('Негативные проверки валидации поля Реакция по максимальному кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.REACTION_FLD_MAX_LEN[0],
                             ids=dtn.REACTION_FLD_MAX_LEN[1])
    def test_reaction_max_len_valid_negotive(self, login_patient, params, open_allegry_section):
        """Негативные проверки валидации поля Реакция по максимальному кол-ву символов"""

        login_patient.get_elem_obj_or_ex('REACTION_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('REACTION_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        value_inserted = login_patient.get_elem_obj_or_ex('REACTION_FLD_NM', 'NAME').get_attribute('value')

        assert value_inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                   f'fact input: {value_inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_REACTION_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Максимальная длина: 200 символов', \
            (f'Текст ошибки не соответсвует требованиям. Expected: Максимальная длина: 200 символов, fact: {err_mess}')

    @allure.story('Позитивные проверки валидации поля Реакция по типам символов')
    @pytest.mark.parametrize('param',
                             dtp.ALLERGEN_FLD_SYMB[0],
                             ids=dtp.ALLERGEN_FLD_SYMB[1])
    def test_reaction_symb_valid_possitive(self, login_patient, param, open_allegry_section):
        """Позитивные проверки валидации поля Реакция по типам символов"""

        login_patient.get_elem_obj_or_ex('REACTION_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('REACTION_FLD_NM',
                                     param['INPUT'],
                                     'NAME')
        value_inserted = login_patient.get_elem_obj_or_ex('REACTION_FLD_NM', 'NAME').get_attribute('value')

        assert value_inserted == param['INPUT'], (
            f'введенный текст отображается не так как ожидалось, expected input: {param["INPUT"]}, '
            f'fact input: {value_inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_REACTION_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess == '', 'при вводе валидных типов символов появл ошибка'


@allure.feature('Проверки валидации поля Операции')
class TestSurgeriesField:
    @allure.story('Позитивные проверки валидации поля Операции по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.SURGERIES_FLD_LEN[0],
                            ids=dtp.SURGERIES_FLD_LEN[1])
    def test_surgeries_len_valid_possitive(self, login_patient, params, open_surgeries_section):
        """Позитивные проверки валидации поля Операции по кол-ву символов"""

        login_patient.get_elem_obj_or_ex('SURGERIES_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('SURGERIES_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        inserted = login_patient.get_elem_obj_or_ex('SURGERIES_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_SURGERIES_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess == '', 'при вводе валидного кол-ва символов появл ошибка'

    @allure.story('Негативные проверки валидации поля Операции по min кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.SURGERIES_FLD_MIN_LEN[0],
                             ids=dtn.SURGERIES_FLD_MIN_LEN[1])
    def test_surgeries_min_len_valid_negotive(self, login_patient, params, open_surgeries_section):
        """Негативные проверки валидации поля Операции по min кол-ву символов"""
        login_patient.get_elem_obj_or_ex('SURGERIES_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('SURGERIES_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        inserted = login_patient.get_elem_obj_or_ex('SURGERIES_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_SURGERIES_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Минимальная длина: 2 символа', (f'Текст ошибки не соответсвует '
                                                                               f'требованиям, expected mess: '
                                                                               f'Минимальная длина: 2 символа, '
                                                                                f'fact mess: {err_mess}')

    @allure.story('Негативные проверки валидации поля Операции по max кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.SURGERIES_FLD_MAX_LEN[0],
                             ids=dtn.SURGERIES_FLD_MAX_LEN[1])
    def test_surgeries_max_len_valid_negotive(self, login_patient, params, open_surgeries_section):
        """Негативные проверки валидации поля Операции по max кол-ву символов"""

        login_patient.get_elem_obj_or_ex('SURGERIES_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('SURGERIES_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_patient.get_elem_obj_or_ex('SURGERIES_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                      f'fact input: {inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_SURGERIES_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Максимальная длина: 200 символов', (f'Текст ошибки не соответсвует '
                                                                                   f'требованиям, expected mess: '
                                                                                   f'Максимальная длина: 200 символов, '
                                                                                    f'fact mess: {err_mess}')

    @allure.story('Позитивные проверки валидации поля Операции по типам символов')
    @pytest.mark.parametrize('params',
                             dtp.SURGERIES_FLD_SYMB[0],
                             ids=dtp.SURGERIES_FLD_SYMB[1])
    def test_surgeries_symb_valid_possitive(self, login_patient, params, open_surgeries_section):
        """Позитивные проверки валидации поля Операции по типам символов"""

        login_patient.get_elem_obj_or_ex('SURGERIES_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('SURGERIES_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_patient.get_elem_obj_or_ex('SURGERIES_FLD_NM', 'NAME').get_attribute('value')

        assert inserted == params['INPUT'], (f'введенный текст отображается не так как ожидалось, expected input: '
                                             f'{params["INPUT"]}, fact input: {inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_SURGERIES_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess == '', 'при вводе валидных типов символов появл ошибка'


@allure.feature('Проверки валидации поля Год проведения (операции)')
class TestSurgerieYearField:

    @allure.story('Позитивные проверки валидации поля Год проведения (операции)')
    @pytest.mark.parametrize('params',
                            dtp.SURGERIE_YEAR_FLD[0],
                            ids=dtp.SURGERIE_YEAR_FLD[1])
    def test_surgerie_year_valid_possitive(self, login_patient, params, open_surgeries_section):
        """Позитивные проверки валидации поля Год проведения (операции) по кол-ву символов"""

        login_patient.get_elem_obj_or_ex('SURGERIE_YEAR_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('SURGERIE_YEAR_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        inserted = login_patient.get_elem_obj_or_ex('SURGERIE_YEAR_FLD_NM', 'NAME').get_attribute('value')

        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_SURGERIE_YEAR_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess == '', 'при вводе валидного года проведения операции появл ошибка'

    @allure.story('Негативные проверки валидации поля Год проведения (операции) при вводе менее 4 цифр')
    @pytest.mark.parametrize('params',
                            dtn.SURGERIE_YEAR_LEN_LESS_THEN_FOUR_DGT_FLD[0],
                            ids=dtn.SURGERIE_YEAR_LEN_LESS_THEN_FOUR_DGT_FLD[1])
    def test_surger_year_len_less_then_4_digits_valid_negotive(self, login_patient, params, open_surgeries_section):
        """ПНегативные проверки валидации поля Год проведения (операции) при вводе менее 4 цифр"""

        login_patient.get_elem_obj_or_ex('SURGERIE_YEAR_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('SURGERIE_YEAR_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        inserted = login_patient.get_elem_obj_or_ex('SURGERIE_YEAR_FLD_NM', 'NAME').get_attribute('value')

        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')

        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_SURGERIE_YEAR_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Неверный формат года', 'Текст ошибки не соответсвует требованиям'

    @allure.story('Негативные проверки валидации поля Год проведения (операции) на невозможность ввести символы, '
                  'отличные от цифр')
    @pytest.mark.parametrize('params',
                             dtn.SURGERIE_YEAR_FLD_CANT_INPUT[0],
                             ids=dtn.SURGERIE_YEAR_FLD_CANT_INPUT[1])
    def test_surger_year_cant_input_valid_negotive(self, login_patient, params, open_surgeries_section):
        """Негативные проверки валидации поля Год проведения (операции) на невозможность ввести символы,
        отличные от цифр"""

        login_patient.get_elem_obj_or_ex('SURGERIE_YEAR_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('SURGERIE_YEAR_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_patient.get_elem_obj_or_ex('SURGERIE_YEAR_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == '', 'в поле можно ввести символы, отличные от цифр'

    @allure.story('Негативные проверки валидации поля Год проведения (операции) на невозможность ввести более 4 цифр')
    @pytest.mark.parametrize('params',
                             dtn.SURGERIE_YEAR_LEN_MORE_THEN_FOUR_DGT_FLD[0],
                             ids=dtn.SURGERIE_YEAR_LEN_MORE_THEN_FOUR_DGT_FLD[1])
    def test_surger_year_len_more_than_4_digits_valid_negotive(self, login_patient, params, open_surgeries_section):
        """Негативные проверки валидации поля Год проведения (операции) на невозможность ввести более 4 цифр"""

        login_patient.get_elem_obj_or_ex('SURGERIE_YEAR_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('SURGERIE_YEAR_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_patient.get_elem_obj_or_ex('SURGERIE_YEAR_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'][0:4], (f'Можно ввести более 4 цифр, expected {params["INPUT"][0:4]},'
                                                  f'fact: {inserted}')


@allure.feature('Проверки валидации поля Препарат')
class TestMedicationField:
    @allure.story('Позитивные проверки валидации поля Препарат по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.MEDICATION_FLD_LEN[0],
                            ids=dtp.MEDICATION_FLD_LEN[1])
    def test_medication_len_valid_possitive(self, login_patient, params, open_medication_section):
        """Позитивные проверки валидации поля Препарат по кол-ву символов"""
        login_patient.get_elem_obj_or_ex('MEDICATION_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('MEDICATION_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        inserted = login_patient.get_elem_obj_or_ex('MEDICATION_FLD_NM', 'NAME').get_attribute('value')

        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_MEDICATION_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess == '', 'при вводе валидного кол-ва символов появл ошибка'

    @allure.story('Негативные проверки валидации поля Препарат по min кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.MEDICATION_FLD_MIN_LEN[0],
                             ids=dtn.MEDICATION_FLD_MIN_LEN[1])
    def test_medication_min_len_valid_negotive(self, login_patient, params, open_medication_section):
        """Негативные проверки валидации поля Препарат по min кол-ву символов"""
        login_patient.get_elem_obj_or_ex('MEDICATION_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('MEDICATION_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        inserted = login_patient.get_elem_obj_or_ex('MEDICATION_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_MEDICATION_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Минимальная длина: 2 символа', (f'Текст ошибки не соответсвует '
                                                                                   f'требованиям, expected mess: '
                                                                                   f'Минимальная длина: 2 символа, '
                                                                                    f'fact mess: {err_mess}')

    @allure.story('Негативные проверки валидации поля Препарат по max кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.MEDICATION_FLD_MAX_LEN[0],
                             ids=dtn.MEDICATION_FLD_MAX_LEN[1])
    def test_medication_max_len_valid_negotive(self, login_patient, params, open_medication_section):
        """Негативные проверки валидации поля Препарат по max кол-ву символов"""
        login_patient.get_elem_obj_or_ex('MEDICATION_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('MEDICATION_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_patient.get_elem_obj_or_ex('MEDICATION_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                      f'fact input: {inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_MEDICATION_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Максимальная длина: 100 символов', (f'Текст ошибки не соответсвует '
                                                                                   f'требованиям, expected mess: '
                                                                                   f'Максимальная длина: 100 символов, '
                                                                                    f'fact mess: {err_mess}')

    @allure.story('Позитивные проверки валидации поля Препарат по типам символов')
    @pytest.mark.parametrize('params',
                             dtp.MEDICATION_FLD_SYMB[0],
                             ids=dtp.MEDICATION_FLD_SYMB[1])
    def test_medication_symb_valid_possitive(self, login_patient, params, open_medication_section):
        """Позитивные проверки валидации поля Препарат по типам символов"""
        login_patient.get_elem_obj_or_ex('MEDICATION_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('MEDICATION_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_patient.get_elem_obj_or_ex('MEDICATION_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст отображается не так как ожидалось, expected input: '
                                             f'{params["INPUT"]}, fact input: {inserted}')

        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_MEDICATION_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess == '', 'при вводе валидных типов символов появл ошибка'


@allure.feature('Проверки валидации поля Дозировка (препарата)')
class TestDosageField:
    @allure.story('Позитивные проверки валидации поля Дозировка по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.DOSAGE_FLD_LEN[0],
                            ids=dtp.DOSAGE_FLD_LEN[1])
    def test_dosage_len_valid_possitive(self, login_patient, params, open_medication_section):
        """Позитивные проверки валидации поля Дозировка по кол-ву символов"""
        login_patient.get_elem_obj_or_ex('DOSAGE_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('DOSAGE_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        inserted = login_patient.get_elem_obj_or_ex('DOSAGE_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_DOSAGE_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess == '', 'при вводе валидного кол-ва символов появл ошибка'

    @allure.story('Негативные проверки валидации поля Дозировка по min кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.DASAGE_FLD_MIN_LEN[0],
                             ids=dtn.DASAGE_FLD_MIN_LEN[1])
    def test_dosage_min_len_valid_negotive(self, login_patient, params, open_medication_section):
        """Негативные проверки валидации поля Дозировка по min кол-ву символов"""
        login_patient.get_elem_obj_or_ex('DOSAGE_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('DOSAGE_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        inserted = login_patient.get_elem_obj_or_ex('DOSAGE_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_DOSAGE_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Минимальная длина: 2 символа', (f'Текст ошибки не соответсвует '
                                                                                   f'требованиям, expected mess: '
                                                                                   f'Минимальная длина: 2 символа, '
                                                                                    f'fact mess: {err_mess}')

    @allure.story('Негативные проверки валидации поля Дозировка по max кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.DOSAGE_FLD_MAX_LEN[0],
                             ids=dtn.DOSAGE_FLD_MAX_LEN[1])
    def test_dosage_max_len_valid_negotive(self, login_patient, params, open_medication_section):
        """Негативные проверки валидации поля Дозировка по max кол-ву символов"""
        login_patient.get_elem_obj_or_ex('DOSAGE_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('DOSAGE_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_patient.get_elem_obj_or_ex('DOSAGE_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                      f'fact input: {inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_DOSAGE_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Максимальная длина: 100 символов', (f'Текст ошибки не соответсвует '
                                                                                   f'требованиям, expected mess: '
                                                                                   f'Максимальная длина: 100 символов, '
                                                                                    f'fact mess: {err_mess}')

    @allure.story('Позитивные проверки валидации поля Дозировка по типам символов')
    @pytest.mark.parametrize('params',
                             dtp.DASAGE_FLD_SYMB[0],
                             ids=dtp.DASAGE_FLD_SYMB[1])
    def test_dosage_symb_valid_possitive(self, login_patient, params, open_medication_section):
        """Позитивные проверки валидации поля Дозировка по типам символов"""
        login_patient.get_elem_obj_or_ex('DOSAGE_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('DOSAGE_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_patient.get_elem_obj_or_ex('DOSAGE_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст отображается не так как ожидалось, expected input: '
                                             f'{params["INPUT"]}, fact input: {inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_DOSAGE_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess == '', 'при вводе валидных типов символов появл ошибка'


@allure.feature('Проверки валидации поля Периодичность приема (препарата)')
class TestFregOfTakingField:
    @allure.story('Позитивные проверки валидации поля Периодичность приема по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.FREQ_OF_TKNG_FLD_LEN[0],
                            ids=dtp.FREQ_OF_TKNG_FLD_LEN[1])
    def test_freq_of_taking_len_valid_possitive(self, login_patient, params, open_medication_section):
        """Позитивные проверки валидации поля Периодичность приема по кол-ву символов"""
        login_patient.get_elem_obj_or_ex('FREQ_OF_TAKING_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('FREQ_OF_TAKING_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        inserted = login_patient.get_elem_obj_or_ex('FREQ_OF_TAKING_FLD_NM', 'NAME').get_attribute('value')

        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_FREQ_OF_TKNG_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess == '', 'при вводе валидного кол-ва символов появл ошибка'


    @allure.story('Негативные проверки валидации поля Периодичность приема по min кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.FREQ_OF_TKNG_FLD_MIN_LEN[0],
                             ids=dtn.FREQ_OF_TKNG_FLD_MIN_LEN[1])
    def test_freq_of_taking_min_len_valid_negotive(self, login_patient, params, open_medication_section):
        """Негативные проверки валидации поля Периодичность приема по min кол-ву символов"""
        login_patient.get_elem_obj_or_ex('FREQ_OF_TAKING_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('FREQ_OF_TAKING_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        inserted = login_patient.get_elem_obj_or_ex('FREQ_OF_TAKING_FLD_NM', 'NAME').get_attribute('value')

        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')

        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_FREQ_OF_TKNG_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Минимальная длина: 2 символа', (f'Текст ошибки не соответсвует '
                                                                                   f'требованиям, expected mess: '
                                                                                   f'Минимальная длина: 2 символа, '
                                                                                    f'fact mess: {err_mess}')

    @allure.story('Негативные проверки валидации поля Периодичность приема по max кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.FREQ_OF_TKNG_FLD_MAX_LEN[0],
                             ids=dtn.FREQ_OF_TKNG_FLD_MAX_LEN[1])
    def test_freq_of_taking_max_len_valid_negotive(self, login_patient, params, open_medication_section):
        """Негативные проверки валидации поля Периодичность приема по max кол-ву символов"""
        login_patient.get_elem_obj_or_ex('FREQ_OF_TAKING_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('FREQ_OF_TAKING_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_patient.get_elem_obj_or_ex('FREQ_OF_TAKING_FLD_NM', 'NAME').get_attribute('value')

        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                      f'fact input: {inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_FREQ_OF_TKNG_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Максимальная длина: 100 символов', (f'Текст ошибки не соответсвует '
                                                                                   f'требованиям, expected mess: '
                                                                                   f'Максимальная длина: 100 символов, '
                                                                                    f'fact mess: {err_mess}')

    @allure.story('Позитивные проверки валидации поля Периодичность приема по типам символов')
    @pytest.mark.parametrize('params',
                             dtp.FREQ_OF_TKNG_FLD_SYMB[0],
                             ids=dtp.FREQ_OF_TKNG_FLD_SYMB[1])
    def test_freq_of_taking_symb_valid_possitive(self, login_patient, params, open_medication_section):
        """Позитивные проверки валидации поля Периодичность приема по типам символов"""
        login_patient.get_elem_obj_or_ex('FREQ_OF_TAKING_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('FREQ_OF_TAKING_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_patient.get_elem_obj_or_ex('FREQ_OF_TAKING_FLD_NM', 'NAME').get_attribute('value')

        assert inserted == params['INPUT'], (f'введенный текст отображается не так как ожидалось, expected input: '
                                             f'{params["INPUT"]}, fact input: {inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_FREQ_OF_TKNG_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess == '', 'при вводе валидных типов символов появл ошибка'


@allure.feature('Проверки валидации поля Хронические заболевания')
class TestChronDesField:
    @allure.story('Позитивные проверки валидации поля Хронические заболевания по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.CHRON_DES_FLD_LEN[0],
                            ids=dtp.CHRON_DES_FLD_LEN[1])
    def test_chron_des_len_valid_possitive(self, login_patient, params, open_chron_des_section):
        """Позитивные проверки валидации поля Хронические заболевания по кол-ву символов"""
        login_patient.get_elem_obj_or_ex('CHRON_DES_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('CHRON_DES_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        inserted = login_patient.get_elem_obj_or_ex('CHRON_DES_FLD_NM', 'NAME').get_attribute('value')

        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_CHRON_DES_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess == '', 'при вводе валидного кол-ва символов появл ошибка'


    @allure.story('Негативные проверки валидации поля Хронические заболевания по min кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.CHRON_DES_FLD_MIN_LEN[0],
                             ids=dtn.CHRON_DES_FLD_MIN_LEN[1])
    def test_chron_des_min_len_valid_negotive(self, login_patient, params, open_chron_des_section):
        """Негативные проверки валидации поля Хронические заболевания по min кол-ву символов"""
        login_patient.get_elem_obj_or_ex('CHRON_DES_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('CHRON_DES_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        inserted = login_patient.get_elem_obj_or_ex('CHRON_DES_FLD_NM', 'NAME').get_attribute('value')

        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_CHRON_DES_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Минимальная длина: 2 символа', (f'Текст ошибки не соответсвует '
                                                                               f'требованиям, expected mess: '
                                                                               f'Минимальная длина: 2 символа, '
                                                                                f'fact mess: {err_mess}')

    @allure.story('Негативные проверки валидации поля Хронические заболевания по max кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.CHRON_DES_FLD_MAX_LEN[0],
                             ids=dtn.CHRON_DES_FLD_MAX_LEN[1])
    def test_chron_des_max_len_valid_negotive(self, login_patient, params, open_chron_des_section):
        """Негативные проверки валидации поля Хронические заболевания по max кол-ву символов"""
        login_patient.get_elem_obj_or_ex('CHRON_DES_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('CHRON_DES_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_patient.get_elem_obj_or_ex('CHRON_DES_FLD_NM', 'NAME').get_attribute('value')

        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                      f'fact input: {inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_CHRON_DES_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Максимальная длина: 200 символов', (f'Текст ошибки не соответсвует '
                                                                                   f'требованиям, expected mess: '
                                                                                   f'Максимальная длина: 200 символов, '
                                                                                    f'fact mess: {err_mess}')

    @allure.story('Позитивные проверки валидации поля Хронические заболевания по типам символов')
    @pytest.mark.parametrize('params',
                             dtp.CHRON_DES_FLD_SYMB[0],
                             ids=dtp.CHRON_DES_FLD_SYMB[1])
    def test_chron_des_symb_valid_possitive(self, login_patient, params, open_chron_des_section):
        """Позитивные проверки валидации поля Хронические заболевания по типам символов"""
        login_patient.get_elem_obj_or_ex('CHRON_DES_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('CHRON_DES_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_patient.get_elem_obj_or_ex('CHRON_DES_FLD_NM', 'NAME').get_attribute('value')

        assert inserted == params['INPUT'], (f'введенный текст отображается не так как ожидалось, expected input: '
                                             f'{params["INPUT"]}, fact input: {inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_CHRON_DES_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess == '', 'при вводе валидных типов символов появл ошибка'


@allure.feature('Проверки валидации поля Год обнаружения (хрон заболевания)')
class TestChronDiscYearField:

    @allure.story('Позитивные проверки валидации поля Год обнаружения (хрон заболевания)')
    @pytest.mark.parametrize('params',
                            dtp.CHRON_DISC_YEAR_FLD[0],
                            ids=dtp.CHRON_DISC_YEAR_FLD[1])
    def test_chron_dics_year_valid_possitive(self, login_patient, params, open_chron_des_section):
        """Позитивные проверки валидации поля Год обнаружения (хрон заболевания) по кол-ву символов"""

        login_patient.get_elem_obj_or_ex('CHRON_DISC_YEAR_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('CHRON_DISC_YEAR_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        inserted = login_patient.get_elem_obj_or_ex('CHRON_DISC_YEAR_FLD_NM', 'NAME').get_attribute('value')

        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_CHRON_DISC_YEAR_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess == '', 'при вводе валидного года проведения операции появл ошибка'

    @allure.story('Негативные проверки валидации поля Год обнаружения (хрон заболевания) при вводе менее 4 цифр')
    @pytest.mark.parametrize('params',
                            dtn.CHRON_DISC_YEAR_LEN_LESS_THEN_FOUR_DGT_FLD[0],
                            ids=dtn.CHRON_DISC_YEAR_LEN_LESS_THEN_FOUR_DGT_FLD[1])
    def test_chron_dics_year_less_than_4_digits_valid_negotive(self, login_patient, params, open_chron_des_section):
        """ПНегативные проверки валидации поля Год обнаружения (хрон заболевания) при вводе менее 4 цифр"""

        login_patient.get_elem_obj_or_ex('CHRON_DISC_YEAR_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('CHRON_DISC_YEAR_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        inserted = login_patient.get_elem_obj_or_ex('CHRON_DISC_YEAR_FLD_NM', 'NAME').get_attribute('value')

        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_patient.get_elem_obj_or_ex('ER_MESS_CHRON_DISC_YEAR_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Неверный формат года', 'Текст ошибки не соответсвует требованиям'

    @allure.story('Негативные проверки валидации поля Год обнаружения (хрон заболевания) на невозможность ввести символы, '
                  'отличные от цифр')
    @pytest.mark.parametrize('params',
                             dtn.CHRON_DISC_YEAR_FLD_CANT_INPUT[0],
                             ids=dtn.CHRON_DISC_YEAR_FLD_CANT_INPUT[1])
    def test_chron_dics_year_cant_input_valid_negotive(self, login_patient, params, open_chron_des_section):
        """Негативные проверки валидации поля Год обнаружения (хрон заболевания) на невозможность ввести символы,
        отличные от цифр"""

        login_patient.get_elem_obj_or_ex('CHRON_DISC_YEAR_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('CHRON_DISC_YEAR_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_patient.get_elem_obj_or_ex('CHRON_DISC_YEAR_FLD_NM', 'NAME').get_attribute('value')

        assert inserted == '', 'в поле можно ввести символы, отличные от цифр'

    @allure.story('Негативные проверки валидации поля Год обнаружения (хрон заболевания) на невозможность ввести более 4 цифр')
    @pytest.mark.parametrize('params',
                             dtn.CHRON_DISC_YEAR_LEN_MORE_THEN_FOUR_DGT_FLD[0],
                             ids=dtn.CHRON_DISC_YEAR_LEN_MORE_THEN_FOUR_DGT_FLD[1])
    def test_chron_dics_year_more_than_4_digits_valid_negotive(self, login_patient, params, open_chron_des_section):
        """Негативные проверки валидации поля Год обнаружения (хрон заболевания) на невозможность ввести более 4 цифр"""

        login_patient.get_elem_obj_or_ex('CHRON_DISC_YEAR_FLD_NM', 'NAME').clear()
        login_patient.fill_the_field('CHRON_DISC_YEAR_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_patient.get_elem_obj_or_ex('CHRON_DISC_YEAR_FLD_NM', 'NAME').get_attribute('value')

        assert inserted == params['INPUT'][0:4], 'можно ввести более 4 цифр'
