# Импортируем библиотеку pytest для работы с фикстурами
import allure
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from conftest import browser
from data_conf import data_test_possit_doc as dtp
from data_conf import data_test_negot_doc as dtn
from datetime import timedelta


@allure.feature('Проверки валидации поля Фамилия - Врач')
class TestLastNameFieldDoc:
    @allure.story('Позитивные проверки валидации фамилии врача по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.ALLNAME_FLD_LEN_POSSITIVE[0],
                            ids=dtp.ALLNAME_FLD_LEN_POSSITIVE[1])
    def test_doc_lname_len_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации фамилии врача по кол-ву символов"""
        login_doctor.get_elem_obj_or_ex('LNAME_XP', 'XPATH').clear()
        login_doctor.screen_shot()
        login_doctor.fill_the_field('LNAME_XP',
                            params['INPUT'],
                            'XPATH')
        err_mess = str(login_doctor.get_elem_obj_or_ex('ER_MESS_LNAME_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('LNAME_XP', 'XPATH').clear()
        assert err_mess == '', 'При вводе допустимого кол-ва символов появляется ошибка'

    @allure.story('Позитивные проверки валидации фамилии врача по типу принимаемых символов')
    @pytest.mark.parametrize('params',
                         dtp.ALLNAME_FLD_SYMB_POSSITIVE[0],
                         ids=dtp.ALLNAME_FLD_SYMB_POSSITIVE[1])
    def test_doc_lname_symbols_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации фамилии врача по вводимым символам"""
        login_doctor.get_elem_obj_or_ex('LNAME_XP', 'XPATH').clear()
        login_doctor.fill_the_field('LNAME_XP',
                            params['INPUT'],
                            'XPATH')
        err_mess = str(login_doctor.get_elem_obj_or_ex('ER_MESS_LNAME_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('LNAME_XP', 'XPATH').clear()
        assert err_mess == '', 'При вводе допустимых типов символов появляется ошибка'


    @allure.story('Позитивные проверки удаления пробелов в начале и в конце фамилии врача')
    @pytest.mark.parametrize('params',
                         dtp.ALLNAME_FLD_SPACE_DELETE[0],
                         ids=dtp.ALLNAME_FLD_SPACE_DELETE[1])
    def test_doc_lname_space_del_possit(self, login_doctor, params):
        """Позитивные проверки удаления пробела в начале и в конце фамилии врача"""
        login_doctor.get_elem_obj_or_ex('LNAME_XP', 'XPATH').clear()
        login_doctor.fill_the_field('LNAME_XP',
                            params['INPUT'],
                            'XPATH')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH',
                                    'XPATH')
        field_fact_data = str(login_doctor.get_elem_obj_or_ex('LNAME_XP', 'XPATH').get_attribute('value'))
        login_doctor.get_elem_obj_or_ex('LNAME_XP', 'XPATH').clear()
        assert field_fact_data == str(params['INPUT']).strip(), 'Пробелы не удаляются'

    @allure.story('Позитивные проверки сохранения фамилии врача в том регистре, как ввел юзер')
    @pytest.mark.parametrize('params',
                         dtp.ALLNAME_FLD_TEXT_REGISTR[0],
                         ids=dtp.ALLNAME_FLD_TEXT_REGISTR[1])
    def test_doc_lname_text_registr_possit(self, login_doctor, params):
        """Позитивные проверки сохранения фамилии врача в том регистре, в каком его ввел юзер"""
        login_doctor.get_elem_obj_or_ex('LNAME_XP', 'XPATH').clear()
        login_doctor.fill_the_field('LNAME_XP',
                            params['INPUT'],
                            'XPATH')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH',
                        'XPATH')
        field_fact_data = str(login_doctor.get_elem_obj_or_ex('LNAME_XP', 'XPATH').get_attribute('value'))
        login_doctor.get_elem_obj_or_ex('LNAME_XP', 'XPATH').clear()
        assert field_fact_data == str(params['INPUT']), (f"Введенные данные сохраняются не том регистре, в каком ввел"
                                                            f'юзер, expected: {str(params["INPUT"])}, '
                                                            f'fact: {field_fact_data}')

    @allure.story('Негативные проверки валидации фамилии врача по мин кол-ву символов')
    @pytest.mark.parametrize('params',
                         dtn.ALLNAME_FLD_MIN_LEN[0],
                         ids=dtn.ALLNAME_FLD_MIN_LEN[1])
    def test_doc_lname_valid_min_len_negot(self, login_doctor, params):
        """Негативные проверки валидации фамилии врача по мин кол-ву символов"""
        login_doctor.get_elem_obj_or_ex('LNAME_XP', 'XPATH').clear()
        login_doctor.fill_the_field('LNAME_XP',
                            params['INPUT'],
                            'XPATH')
        err_mess = str(login_doctor.get_elem_obj_or_ex('ER_MESS_LNAME_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('LNAME_XP', 'XPATH').clear()

        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Минимальная длина: 2 символа', (f'Текст ошибки не соответсвует '
                                                                                   f'требованиям, expected mess: '
                                                                                   f'Минимальная длина: 2 символа, '
                                                                                    f'fact mess: {err_mess}')

    @allure.story('Негативные проверки валидации фамилии врача по макс кол-ву символов')
    @pytest.mark.parametrize('params',
                         dtn.ALLNAME_FLD_MAX_LEN[0],
                         ids=dtn.ALLNAME_FLD_MAX_LEN[1])
    def test_doc_lname_valid_max_len_negot(self, login_doctor, params):
        """Негативные проверки валидации фамилии врача по макс кол-ву символов"""
        login_doctor.get_elem_obj_or_ex('LNAME_XP', 'XPATH').clear()
        login_doctor.fill_the_field('LNAME_XP',
                            params['INPUT'],
                            'XPATH')
        err_mess = str(login_doctor.get_elem_obj_or_ex('ER_MESS_LNAME_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('LNAME_XP', 'XPATH').clear()
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Максимальная длина: 50 символов', (f'Текст ошибки не соответсвует '
                                                                               f'требованиям, expected mess: '
                                                                               f'Максимальная длина: 50 символов, '
                                                                               f'fact mess: {err_mess}')


@allure.feature('Проверки валидации поля Имя Врача')
class TestFirstNameFieldDoc:
    @allure.story('Позитивные проверки валидации имени врача по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.ALLNAME_FLD_LEN_POSSITIVE[0],
                            ids=dtp.ALLNAME_FLD_LEN_POSSITIVE[1])
    def test_doc_fname_len_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации имени врача по кол-ву символов"""
        login_doctor.get_elem_obj_or_ex('FNAME_XP', 'XPATH').clear()
        login_doctor.fill_the_field('FNAME_XP',
                            params['INPUT'],
                            'XPATH')
        err_mess = str(login_doctor.get_elem_obj_or_ex('ER_MESS_FNAME_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('FNAME_XP', 'XPATH').clear()
        assert err_mess == '', 'При вводе валидного кол-ва символов появляется ошибка'

    @allure.story('Позитивные проверки валидации имени врача по типу принимаемых символов')
    @pytest.mark.parametrize('params',
                         dtp.ALLNAME_FLD_SYMB_POSSITIVE[0],
                         ids=dtp.ALLNAME_FLD_SYMB_POSSITIVE[1])
    def test_doc_fname_symbols_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации имени врача по вводимым символам"""
        login_doctor.get_elem_obj_or_ex('FNAME_XP', 'XPATH').clear()
        login_doctor.fill_the_field('FNAME_XP',
                            params['INPUT'],
                            'XPATH')
        err_mess = str(login_doctor.get_elem_obj_or_ex('ER_MESS_FNAME_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('FNAME_XP', 'XPATH').clear()
        assert err_mess == '', 'При вводе валидных типов символов появляется ошибка'

    @allure.story('Позитивные проверки удаления пробелов в начале и в конце имени врача')
    @pytest.mark.parametrize('params',
                         dtp.ALLNAME_FLD_SPACE_DELETE[0],
                         ids=dtp.ALLNAME_FLD_SPACE_DELETE[1])
    def test_doc_fname_space_del_possit(self, login_doctor, params):
        """Позитивные проверки удаления пробела в начале и в конце имени врача"""
        login_doctor.get_elem_obj_or_ex('FNAME_XP', 'XPATH').clear()
        login_doctor.fill_the_field('FNAME_XP',
                            params['INPUT'],
                            'XPATH')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH',
                        'XPATH')
        field_fact_data = str(login_doctor.get_elem_obj_or_ex('FNAME_XP', 'XPATH').get_attribute('value'))
        login_doctor.get_elem_obj_or_ex('FNAME_XP', 'XPATH').clear()
        assert field_fact_data == str(params['INPUT']).strip(), 'Пробелы не удаляются после снятия фокуса'

    @allure.story('Позитивные проверки сохранения ввода имени врача в том регистре, как ввел юзер')
    @pytest.mark.parametrize('params',
                         dtp.ALLNAME_FLD_TEXT_REGISTR[0],
                         ids=dtp.ALLNAME_FLD_TEXT_REGISTR[1])
    def test_doc_fname_text_registr_possit(self, login_doctor, params):
        """Позитивные проверки сохранения ввода имени врача в том регистре, в каком его ввел юзер"""
        login_doctor.get_elem_obj_or_ex('FNAME_XP', 'XPATH').clear()
        login_doctor.fill_the_field('FNAME_XP',
                            params['INPUT'],
                            'XPATH')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH',
                        'XPATH')
        field_fact_data = str(login_doctor.get_elem_obj_or_ex('FNAME_XP', 'XPATH').get_attribute('value'))
        login_doctor.get_elem_obj_or_ex('FNAME_XP', 'XPATH').clear()
        assert field_fact_data == str(params['INPUT']), (f'Ввод сохраняется не в том регистре, в каком ввел юзер, '
                                                         f'expected: str(params["INPUT"]), fact: {field_fact_data}')

    @allure.story('Негативные проверки валидации имени врача по мин кол-ву символов')
    @pytest.mark.parametrize('params',
                         dtn.ALLNAME_FLD_MIN_LEN[0],
                         ids=dtn.ALLNAME_FLD_MIN_LEN[1])
    def test_doc_fname_valid_min_len_negot(self, login_doctor, params):
        """Негативные проверки валидации имени врача по мин кол-ву символов"""
        login_doctor.get_elem_obj_or_ex('FNAME_XP', 'XPATH').clear()
        login_doctor.fill_the_field('FNAME_XP',
                            params['INPUT'],
                            'XPATH')
        err_mess = str(login_doctor.get_elem_obj_or_ex('ER_MESS_FNAME_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('FNAME_XP', 'XPATH').clear()
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Минимальная длина: 2 символа', (f'Текст ошибки не соответсвует '
                                                                                  f'требованиям, expected mess: '
                                                                                  f'Минимальная длина: 2 символа, '
                                                                                  f'fact mess: {err_mess}')

    @allure.story('Негативные проверки валидации имени врача по макс кол-ву символов')
    @pytest.mark.parametrize('params',
                         dtn.ALLNAME_FLD_MAX_LEN[0],
                         ids=dtn.ALLNAME_FLD_MAX_LEN[1])
    def test_doc_fname_valid_max_len_negot(self, login_doctor, params):
        """Негативные проверки валидации имени врача по макс кол-ву символов"""
        login_doctor.get_elem_obj_or_ex('FNAME_XP', 'XPATH').clear()
        login_doctor.fill_the_field('FNAME_XP',
                            params['INPUT'],
                            'XPATH')
        err_mess = str(login_doctor.get_elem_obj_or_ex('ER_MESS_FNAME_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('FNAME_XP', 'XPATH').clear()
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Максимальная длина: 50 символов', (f'Текст ошибки не соответсвует '
                                                                               f'требованиям, expected mess: '
                                                                               f'Максимальная длина: 50 символов, '
                                                                               f'fact mess: {err_mess}')


@allure.feature('Проверки валидации поля Отчество Врача')
class TestPatronFieldDoctor:
    @allure.story('Позитивные проверки валидации  отчества Врача по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.ALLNAME_FLD_LEN_POSSITIVE[0],
                            ids=dtp.ALLNAME_FLD_LEN_POSSITIVE[1])
    def test_doc_patron_len_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации отчества Врача по кол-ву символов"""
        login_doctor.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').clear()
        login_doctor.fill_the_field('PATRONYMIC_XP',
                                         params['INPUT'],
                                         'XPATH')
        err_mess = str(login_doctor.get_elem_obj_or_ex('ER_MESS_PATRON_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').clear()
        assert err_mess == '', 'При вводе валиднjго кол-ва символов возникает ошибка'

    @allure.story('Позитивные проверки валидации отчества Врача по типу принимаемых символов')
    @pytest.mark.parametrize('params',
                            dtp.ALLNAME_FLD_SYMB_POSSITIVE[0],
                            ids=dtp.ALLNAME_FLD_SYMB_POSSITIVE[1])
    def test_doc_patron_symbols_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации отчества Врача по вводимым символам"""
        login_doctor.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').clear()
        login_doctor.fill_the_field('PATRONYMIC_XP',
                                         params['INPUT'],
                                         'XPATH')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_PATRON_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').clear()
        assert err_mess == '', 'При вводе валидных типов символов появляется ошибка'

    @allure.story('Позитивные проверки удаления пробелов в начале и в конце отчества врача')
    @pytest.mark.parametrize('params',
                            dtp.ALLNAME_FLD_SPACE_DELETE[0],
                            ids=dtp.ALLNAME_FLD_SPACE_DELETE[1])
    def test_doc_patron_space_del_possit(self, login_doctor, params):
        """Позитивные проверки удаления пробела в начале и в конце отчества врача"""
        login_doctor.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').clear()
        login_doctor.fill_the_field('PATRONYMIC_XP',
                                         params['INPUT'],
                                         'XPATH')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH',
                                        'XPATH')
        field_fact_data = str(login_doctor.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').get_attribute('value'))
        login_doctor.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').clear()
        assert field_fact_data == str(params['INPUT']).strip(), 'Пробелы не удаляются после снятия фокуса'

    @allure.story('Позитивные проверки сохранения ввода отчества врача в том регистре, как ввел юзер')
    @pytest.mark.parametrize('params',
                            dtp.ALLNAME_FLD_TEXT_REGISTR[0],
                            ids=dtp.ALLNAME_FLD_TEXT_REGISTR[1])
    def test_вoc_patron_text_registr_possit(self, login_doctor, params):
        """Позитивные проверки сохранения ввода отчества врача в том регистре, в каком его ввел юзер"""
        login_doctor.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').clear()
        login_doctor.fill_the_field('PATRONYMIC_XP',
                                         params['INPUT'],
                                         'XPATH')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH',
                                        'XPATH')
        field_fact_data = str(login_doctor.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').get_attribute('value'))
        login_doctor.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').clear()
        assert field_fact_data == str(params['INPUT']), 'Ввод сохраняется не в том регистре, в каком ввел юзер'

    @allure.story('Негативные проверки валидации отчества врача по мин кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtn.ALLNAME_FLD_MIN_LEN[0],
                            ids=dtn.ALLNAME_FLD_MIN_LEN[1])
    def test_doc_patron_valid_min_len_negot(self, login_doctor, params):
        """Негативные проверки валидации отчества врача по мин кол-ву символов"""
        login_doctor.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').clear()
        login_doctor.fill_the_field('PATRONYMIC_XP',
                                         params['INPUT'],
                                         'XPATH')
        err_mess = str(
                login_doctor.get_elem_obj_or_ex('ER_MESS_PATRON_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').clear()
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Минимальная длина: 2 символа', (f'Текст ошибки не соответсвует '
                                                                               f'требованиям, expected mess: '
                                                                               f'Минимальная длина: 2 символа, '
                                                                               f'fact mess: {err_mess}')

    @allure.story('Негативные проверки валидации отчества врача по макс кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtn.ALLNAME_FLD_MAX_LEN[0],
                            ids=dtn.ALLNAME_FLD_MAX_LEN[1])
    def test_doc_patron_valid_max_len_negot(self, login_doctor, params):
        """Негативные проверки валидации отчества врача по макс кол-ву символов"""
        login_doctor.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').clear()
        login_doctor.fill_the_field('PATRONYMIC_XP',
                                         params['INPUT'],
                                         'XPATH')
        err_mess = str(
                login_doctor.get_elem_obj_or_ex('ER_MESS_PATRON_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').clear()
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Максимальная длина: 50 символов', (f'Текст ошибки не соответсвует '
                                                                               f'требованиям, expected mess: '
                                                                               f'Максимальная длина: 50 символов, '
                                                                               f'fact mess: {err_mess}')


@allure.feature('Проверки валидации поля Дата рождения врача')
class TestDBirthFieldDoctor:
    @allure.story('Позитивные проверки ввода валидной даты рождения врача')
    @pytest.mark.parametrize('params',
                            dtp.DBIRTH_FLD_POSSITIVE[0],
                            ids=dtp.DBIRTH_FLD_POSSITIVE[1])
    def test_doc_birthdate_valid_possit(self, login_doctor, params):
        """Позитивные проверки ввода валидной даты рождения врача"""
        login_doctor.get_elem_obj_or_ex('DBIRTH_FLD_NM','NAME').clear()
        login_doctor.fill_the_field('DBIRTH_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        date_inserted = login_doctor.get_elem_obj_or_ex('DBIRTH_FLD_NM','NAME').get_attribute('value')
        assert date_inserted == params['INPUT'], 'Ввод сохраняется не так, как ввел пользователь'

        err_mess = str(
                login_doctor.get_elem_obj_or_ex('ER_MESS_DBIRTH_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('DBIRTH_FLD_NM', 'NAME').clear()
        assert err_mess == '', 'При вводе валидной даты рождения появляется ошибка'

    @allure.story('Негативные проверки ввода невалидной даты рождения врача')
    @pytest.mark.parametrize('params',
                             dtn.DBIRTH_FLD_UNVALID[0],
                             ids=dtn.DBIRTH_FLD_UNVALID[1])
    def test_doc_birthdate_valid_negot(self, login_doctor, params):
        """Негативные проверки ввода невалидной даты рождения врача"""
        login_doctor.get_elem_obj_or_ex('DBIRTH_FLD_NM', 'NAME').clear()
        login_doctor.fill_the_field('DBIRTH_FLD_NM',
                                     params['INPUT'],
                                     'NAME')

        date_inserted = login_doctor.get_elem_obj_or_ex('DBIRTH_FLD_NM', 'NAME').get_attribute('value')
        assert date_inserted == params['INPUT'], 'Ввод сохраняется не так, как ввел пользователь'

        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_DBIRTH_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('DBIRTH_FLD_NM', 'NAME').clear()
        assert err_mess != '', 'При вводе невалидной даты ошибки не возникает '
        assert err_mess != '' and err_mess == 'Некорректная дата', (f'Текст ошибки не соответсвует '
                                                                               f'требованиям, expected mess: '
                                                                               f'Некорректная дата, '
                                                                               f'fact mess: {err_mess}')

    @allure.story('Позитивная проверка ввода даты рождения при которой врачу ровно 18 лет')
    def test_doc_birthdate_eq_18(self, login_doctor):
        """Позитивные проверки ввода даты рождения, при которой врачу ровно 18"""
        # очищаем поле
        login_doctor.get_elem_obj_or_ex('DBIRTH_FLD_NM', 'NAME').clear()
        # получаем дату 18 лет назад от текущей
        birthdate_to_test = login_doctor.get_date_18_years_ago().strftime("%d/%m/%Y")
        # вносим полученную дату
        login_doctor.fill_the_field('DBIRTH_FLD_NM',
                                     birthdate_to_test,
                                     'NAME')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_DBIRTH_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('DBIRTH_FLD_NM', 'NAME').clear()
        assert err_mess == '', 'При вводе валидной даты появляется сообщение об ошибке'

    @allure.story('Позитивная проверка ввода даты рождения при которой врач старше 18 лет')
    def test_doc_birthdate_more_then_18(self, login_doctor):
        """Позитивные проверки ввода даты рождения, при которой врач старше 18"""
        # очищаем поле
        login_doctor.get_elem_obj_or_ex('DBIRTH_FLD_NM', 'NAME').clear()
        # получаем дату 18 лет назад и еще минус один день
        birthdate_to_test = (login_doctor.get_date_18_years_ago() - timedelta(days=1)).strftime("%d/%m/%Y")
        # вводим полученную дату
        login_doctor.fill_the_field('DBIRTH_FLD_NM',
                                     birthdate_to_test,
                                     'NAME')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_DBIRTH_XPATH', 'XPATH').get_attribute('textContent'))
        assert err_mess == '', 'При вводе валидной даты появляется сообщение об ошибке'

    @allure.story('Негативная проверка ввода даты рождения при которой врач младше 18 лет')
    def test_doc_birthdate_less_then_18(self, login_doctor):
        """Негативная проверка ввода даты рождения при которой врач младше 18 лет"""
        # очищаем поле
        login_doctor.get_elem_obj_or_ex('DBIRTH_FLD_NM', 'NAME').clear()
        birthdate_to_test = (login_doctor.get_date_18_years_ago() + timedelta(days=1)).strftime("%d/%m/%Y")
        login_doctor.fill_the_field('DBIRTH_FLD_NM',
                                     birthdate_to_test,
                                     'NAME')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_DBIRTH_XPATH', 'XPATH').get_attribute('textContent'))

        assert err_mess != '', 'При вводе даты рождения, при которой юзер младше 18 лет, ошибки не возникает '
        assert err_mess != '' and err_mess == 'Нельзя зарегистрироваться на сайте, если Вам меньше 18 лет', \
            (f'Текст ошибки не соответсвует требованиям, expected mess: "Нельзя зарегистрироваться на сайте, если Вам'
             f' меньше 18 лет", fact mess: "{err_mess}"')


@allure.feature('Проверки валидации поля Email врача')
class TestEmailFieldDoctor:
    @allure.story('Позитивные проверки валидации email врача по кол-ву симовлов')
    @pytest.mark.parametrize('params',
                            dtp.EMAIL_FLD_LEN[0],
                            ids=dtp.EMAIL_FLD_LEN[1])
    def test_doc_email_len_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации поля Email врача по кол-ву символов"""
        login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').clear()
        login_doctor.fill_the_field('EMAIL_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        err_mess = str(
                login_doctor.get_elem_obj_or_ex('ER_MESS_EMAIL_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').clear()
        assert err_mess == '', 'При вводе валидного кол-ва символов появляется ошибка'

    @allure.story('Позитивные проверки валидации email врача по типу вводимых симовлов')
    @pytest.mark.parametrize('params',
                             dtp.EMAIL_FLD_SYMB[0],
                             ids=dtp.EMAIL_FLD_SYMB[1])
    def test_doc_email_symb_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации поля Email врача по типу вводимых символов"""
        login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').clear()
        login_doctor.fill_the_field('EMAIL_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_EMAIL_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').clear()
        assert err_mess == '', 'При вводе валидных типов символов появляется ошибка'

    @allure.story('Негативные проверки валидации email врача по минимальному кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.EMAIL_FLD_MIN_LEN[0],
                             ids=dtn.EMAIL_FLD_MIN_LEN[1])
    def test_doc_email_len_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Email врача по минимальному кол-ву символов"""
        login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').clear()
        login_doctor.fill_the_field('EMAIL_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_EMAIL_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').clear()
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'В поле должно быть минимум 6 символов', \
            (f'Текст ошибки не соответсвует требованиям, expected mess: "В поле должно быть минимум 6 символов",'
             f'fact mess: "{err_mess}"')

    @allure.story('Негативные проверки валидации email врача по максимальному кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.EMAIL_FLD_MAX_LEN[0],
                             ids=dtn.EMAIL_FLD_MAX_LEN[1])
    def test_doc_email_len_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Email врача по максимальному кол-ву символов"""
        login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').clear()
        login_doctor.fill_the_field('EMAIL_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_EMAIL_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').clear()
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'В поле должно быть максимум 70 символов', \
            (f'Текст ошибки не соответствует требованиям, expected mess: "В поле должно быть максимум 70 символов",'
             f'fact mess: "{err_mess}"')

    @allure.story('Негативные проверки валидации email врача по маске')
    @pytest.mark.parametrize('params',
                             dtn.EMAIL_FLD_MASK[0],
                             ids=dtn.EMAIL_FLD_MASK[1])
    def test_doc_email_mask_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Email врача по маске"""
        login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').clear()
        login_doctor.fill_the_field('EMAIL_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_EMAIL_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').clear()
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Допустимый формат почты: test@test.ru', \
            (f'Текст ошибки не соответствует требованиям, expected mess: Допустимый формат почты: test@test.ru, '
                                                                               f'fact mess: {err_mess}')

    @allure.story('Позитивные проверки удаления пробелов в начале и в конце email врача')
    @pytest.mark.parametrize('params',
                             dtp.EMAIL_FLD_SPACE_DELETE[0],
                             ids=dtp.EMAIL_FLD_SPACE_DELETE[1])
    def test_doc_email_space_del_possit(self, login_doctor, params):
        """Позитивные проверки удаления пробела в начале и в конце email врача"""
        login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').clear()
        login_doctor.fill_the_field('EMAIL_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH',
                                    'XPATH')
        field_fact_data = str(login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').get_attribute('value'))
        login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').clear()
        assert field_fact_data == str(params['INPUT']).strip(), 'При вводе пробелы не удаляются'


@allure.feature('Проверки валидации поля Учебное заведение врача')
class TestEduInstitField:
    @allure.story('Позитивные проверки валидации поля Учебное заведение врача по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.EDU_INSTIT_FLD_LEN[0],
                            ids=dtp.EDU_INSTIT_FLD_LEN[1])
    def test_doc_edu_instit_len_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации поля Учебное заведение врача по кол-ву символов"""

        login_doctor.get_elem_obj_or_ex('UDU_INSTIT_FLD_NM', 'NAME').clear()
        login_doctor.fill_the_field('UDU_INSTIT_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('UDU_INSTIT_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_EDU_INSTIT_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('UDU_INSTIT_FLD_NM', 'NAME').clear()
        assert err_mess == '', 'при вводе валидного кол-ва символов появл ошибка'

    @allure.story('Негативные проверки валидации поля Учебное заведение врача по min кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.EDU_INSTIT_FLD_MIN_LEN[0],
                             ids=dtn.EDU_INSTIT_FLD_MIN_LEN[1])
    def test_doc_edu_instit_min_len_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Учеюное заведение врача по min кол-ву символов"""
        login_doctor.get_elem_obj_or_ex('UDU_INSTIT_FLD_NM', 'NAME').clear()
        login_doctor.fill_the_field('UDU_INSTIT_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        allergen_inserted = login_doctor.get_elem_obj_or_ex('UDU_INSTIT_FLD_NM', 'NAME').get_attribute('value')
        assert allergen_inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {allergen_inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_EDU_INSTIT_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('UDU_INSTIT_FLD_NM', 'NAME').clear()
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Минимальная длина: 2 символа', \
            f'Текст ошибки не соответствует требованиям. Expect: "Минимальная длина: 2 символа", fact: "{err_mess}" '

    @allure.story('Негативные проверки валидации поля Учебное заведение врача по max кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.EDU_INSTIT_FLD_MAX_LEN[0],
                             ids=dtn.EDU_INSTIT_FLD_MAX_LEN[1])
    def test_doc_edu_instit_max_len_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Учебное заведение врача по max кол-ву символов"""
        login_doctor.get_elem_obj_or_ex('UDU_INSTIT_FLD_NM', 'NAME').clear()
        login_doctor.fill_the_field('UDU_INSTIT_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('UDU_INSTIT_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                      f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_EDU_INSTIT_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('UDU_INSTIT_FLD_NM', 'NAME').clear()
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Максимальная длина: 50 символов', \
            (f'Текст ошибки не соответсвует требованиям. Expected: "Максимальная длина: 50 символов", fact:'
             f'"{err_mess}" ')

    @allure.story('Позитивные проверки валидации поля Учебное заведение врача по типам символов')
    @pytest.mark.parametrize('params',
                             dtp.EDU_INSTIT_FLD_SYMB[0],
                             ids=dtp.EDU_INSTIT_FLD_SYMB[1])
    def test_doc_edu_instit_symb_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации поля Учебное заведение врача по типам символов"""
        login_doctor.get_elem_obj_or_ex('UDU_INSTIT_FLD_NM', 'NAME').clear()
        login_doctor.fill_the_field('UDU_INSTIT_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('UDU_INSTIT_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (
            f'введенный текст отображается не так как ожидалось, expected input: {params["INPUT"]}, '
            f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_EDU_INSTIT_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('UDU_INSTIT_FLD_NM', 'NAME').clear()
        assert err_mess == '', 'при вводе валидных типов символов появл ошибка'

    @allure.story('Негативные проверки валидации поля Учебное заведение врача по типам символов')
    @pytest.mark.parametrize('params',
                             dtn.EDU_INSTIT_FLD_SYMB[0],
                             ids=dtn.EDU_INSTIT_FLD_SYMB[1])
    def test_doc_edu_instit_symb_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Учебное заведение врача по типам символов"""
        login_doctor.get_elem_obj_or_ex('UDU_INSTIT_FLD_NM', 'NAME').clear()
        login_doctor.fill_the_field('UDU_INSTIT_FLD_NM',
                                    params['INPUT'],
                                    'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('UDU_INSTIT_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (
            f'введенный текст отображается не так как ожидалось, expected input: {params["INPUT"]}, '
            f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_EDU_INSTIT_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.get_elem_obj_or_ex('UDU_INSTIT_FLD_NM', 'NAME').clear()
        assert err_mess != '', 'При вводе невалидных типов символов ошибки не возникает '
        assert err_mess != '' and err_mess == ('Значение может содержать символы алфавита, пробел, '
                                               'дефис, цифры, символы ()№""'), \
            (f'Текст ошибки не соответсвует требованиям. Expected: "Значение может содержать символы алфавита, '
             f'пробел, дефис, цифры, символы ()№""", fact: "{err_mess}" ')

