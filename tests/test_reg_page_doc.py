# Импортируем библиотеку pytest для работы с фикстурами
import allure
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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
        # Заполняем поле
        login_doctor.fill_the_field('LNAME_XP', params['INPUT'], 'XPATH')
        # Получаем текст сообщения об ошибке или пустую строку, если ошибки нет
        err_mess = str(login_doctor.get_elem_obj_or_ex('ER_MESS_LNAME_XPATH', 'XPATH').get_attribute('textContent'))
        # Очищаем поле
        login_doctor.clear_field('LNAME_XP', 'XPATH')
        # Проверяем, что ошибки нет (сообщение содержит пустую строку)
        assert err_mess == '', 'При вводе допустимого кол-ва символов появляется ошибка'

    @allure.story('Позитивные проверки валидации фамилии врача по типу принимаемых символов')
    @pytest.mark.parametrize('params',
                         dtp.ALLNAME_FLD_SYMB_POSSITIVE[0],
                         ids=dtp.ALLNAME_FLD_SYMB_POSSITIVE[1])
    def test_doc_lname_symbols_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации фамилии врача по вводимым символам"""
        login_doctor.fill_the_field('LNAME_XP', params['INPUT'], 'XPATH')
        err_mess = str(login_doctor.get_elem_obj_or_ex('ER_MESS_LNAME_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('LNAME_XP', 'XPATH')
        assert err_mess == '', 'При вводе допустимых типов символов появляется ошибка'

    @allure.story('Позитивные проверки удаления пробелов в начале и в конце фамилии врача')
    @pytest.mark.parametrize('params',
                         dtp.ALLNAME_FLD_SPACE_DELETE[0],
                         ids=dtp.ALLNAME_FLD_SPACE_DELETE[1])
    def test_doc_lname_space_del_possit(self, login_doctor, params):
        """Позитивные проверки удаления пробела в начале и в конце фамилии врача"""
        # Заполняем поле
        login_doctor.fill_the_field('LNAME_XP', params['INPUT'], 'XPATH')
        # Кликаем в нейстральную область, чтобы снять фокус с поля
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH',
                                    'XPATH')
        # Получаем фактические данные, сохраненные в поле после снятия фокуса с поля
        field_fact_data = str(login_doctor.get_elem_obj_or_ex('LNAME_XP', 'XPATH').get_attribute('value'))
        # Очищаем поле
        login_doctor.clear_field('LNAME_XP', 'XPATH')
        # Проверяем, что фактические данные в поле сохранены без пробела
        assert field_fact_data == str(params['INPUT']).strip(), 'Пробелы не удаляются'

    @allure.story('Позитивные проверки сохранения фамилии врача в том регистре, как ввел юзер')
    @pytest.mark.parametrize('params',
                         dtp.ALLNAME_FLD_TEXT_REGISTR[0],
                         ids=dtp.ALLNAME_FLD_TEXT_REGISTR[1])
    def test_doc_lname_text_registr_possit(self, login_doctor, params):
        """Позитивные проверки сохранения фамилии врача в том регистре, в каком его ввел юзер"""
        # Заполняем поле
        login_doctor.fill_the_field('LNAME_XP', params['INPUT'], 'XPATH')
        # Кликаем в нейстральную область, чтобы снять фокус с поля
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH', 'XPATH')
        # Получаем фактические данные, сохраненные в поле после снятия фокуса с поля
        field_fact_data = str(login_doctor.get_elem_obj_or_ex('LNAME_XP', 'XPATH').get_attribute('value'))
        # Очищаем поле
        login_doctor.clear_field('LNAME_XP', 'XPATH')
        # Проверяем , что данные в поле сохранены в том виде, в каком ввел юзер
        assert field_fact_data == str(params['INPUT']), (f"Введенные данные сохраняются не том регистре, в каком ввел"
                                                            f'юзер, expected: {str(params["INPUT"])}, '
                                                            f'fact: {field_fact_data}')

    @allure.story('Негативные проверки валидации фамилии врача по мин кол-ву символов')
    @pytest.mark.parametrize('params',
                         dtn.ALLNAME_FLD_MIN_LEN[0],
                         ids=dtn.ALLNAME_FLD_MIN_LEN[1])
    def test_doc_lname_valid_min_len_negot(self, login_doctor, params):
        """Негативные проверки валидации фамилии врача по мин кол-ву символов"""
        login_doctor.fill_the_field('LNAME_XP', params['INPUT'], 'XPATH')
        err_mess = str(login_doctor.get_elem_obj_or_ex('ER_MESS_LNAME_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('LNAME_XP', 'XPATH')

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
        login_doctor.fill_the_field('LNAME_XP',
                            params['INPUT'],
                            'XPATH')
        err_mess = str(login_doctor.get_elem_obj_or_ex('ER_MESS_LNAME_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('LNAME_XP', 'XPATH')
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
        login_doctor.fill_the_field('FNAME_XP', params['INPUT'], 'XPATH')
        err_mess = str(login_doctor.get_elem_obj_or_ex('ER_MESS_FNAME_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('FNAME_XP', 'XPATH')
        assert err_mess == '', 'При вводе валидного кол-ва символов появляется ошибка'

    @allure.story('Позитивные проверки валидации имени врача по типу принимаемых символов')
    @pytest.mark.parametrize('params',
                         dtp.ALLNAME_FLD_SYMB_POSSITIVE[0],
                         ids=dtp.ALLNAME_FLD_SYMB_POSSITIVE[1])
    def test_doc_fname_symbols_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации имени врача по вводимым символам"""
        login_doctor.fill_the_field('FNAME_XP', params['INPUT'], 'XPATH')
        err_mess = str(login_doctor.get_elem_obj_or_ex('ER_MESS_FNAME_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('FNAME_XP', 'XPATH')
        assert err_mess == '', 'При вводе валидных типов символов появляется ошибка'

    @allure.story('Позитивные проверки удаления пробелов в начале и в конце имени врача')
    @pytest.mark.parametrize('params',
                         dtp.ALLNAME_FLD_SPACE_DELETE[0],
                         ids=dtp.ALLNAME_FLD_SPACE_DELETE[1])
    def test_doc_fname_space_del_possit(self, login_doctor, params):
        """Позитивные проверки удаления пробела в начале и в конце имени врача"""
        login_doctor.fill_the_field('FNAME_XP', params['INPUT'], 'XPATH')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH', 'XPATH')
        field_fact_data = str(login_doctor.get_elem_obj_or_ex('FNAME_XP', 'XPATH').get_attribute('value'))
        login_doctor.clear_field('FNAME_XP', 'XPATH')
        assert field_fact_data == str(params['INPUT']).strip(), 'Пробелы не удаляются после снятия фокуса'

    @allure.story('Позитивные проверки сохранения ввода имени врача в том регистре, как ввел юзер')
    @pytest.mark.parametrize('params',
                         dtp.ALLNAME_FLD_TEXT_REGISTR[0],
                         ids=dtp.ALLNAME_FLD_TEXT_REGISTR[1])
    def test_doc_fname_text_registr_possit(self, login_doctor, params):
        """Позитивные проверки сохранения ввода имени врача в том регистре, в каком его ввел юзер"""
        login_doctor.fill_the_field('FNAME_XP', params['INPUT'], 'XPATH')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH', 'XPATH')
        field_fact_data = str(login_doctor.get_elem_obj_or_ex('FNAME_XP', 'XPATH').get_attribute('value'))
        login_doctor.clear_field('FNAME_XP', 'XPATH')
        assert field_fact_data == str(params['INPUT']), (f'Ввод сохраняется не в том регистре, в каком ввел юзер, '
                                                         f'expected: str(params["INPUT"]), fact: {field_fact_data}')

    @allure.story('Негативные проверки валидации имени врача по мин кол-ву символов')
    @pytest.mark.parametrize('params',
                         dtn.ALLNAME_FLD_MIN_LEN[0],
                         ids=dtn.ALLNAME_FLD_MIN_LEN[1])
    def test_doc_fname_valid_min_len_negot(self, login_doctor, params):
        """Негативные проверки валидации имени врача по мин кол-ву символов"""
        login_doctor.fill_the_field('FNAME_XP', params['INPUT'], 'XPATH')
        err_mess = str(login_doctor.get_elem_obj_or_ex('ER_MESS_FNAME_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('FNAME_XP', 'XPATH')
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
        login_doctor.fill_the_field('FNAME_XP', params['INPUT'], 'XPATH')
        err_mess = str(login_doctor.get_elem_obj_or_ex('ER_MESS_FNAME_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('FNAME_XP', 'XPATH')
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
        login_doctor.fill_the_field('PATRONYMIC_XP', params['INPUT'], 'XPATH')
        err_mess = str(login_doctor.get_elem_obj_or_ex('ER_MESS_PATRON_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('PATRONYMIC_XP', 'XPATH')
        assert err_mess == '', 'При вводе валиднjго кол-ва символов возникает ошибка'

    @allure.story('Позитивные проверки валидации отчества Врача по типу принимаемых символов')
    @pytest.mark.parametrize('params',
                            dtp.ALLNAME_FLD_SYMB_POSSITIVE[0],
                            ids=dtp.ALLNAME_FLD_SYMB_POSSITIVE[1])
    def test_doc_patron_symbols_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации отчества Врача по вводимым символам"""
        login_doctor.fill_the_field('PATRONYMIC_XP',
                                         params['INPUT'],
                                         'XPATH')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_PATRON_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('PATRONYMIC_XP', 'XPATH')
        assert err_mess == '', 'При вводе валидных типов символов появляется ошибка'

    @allure.story('Позитивные проверки удаления пробелов в начале и в конце отчества врача')
    @pytest.mark.parametrize('params',
                            dtp.ALLNAME_FLD_SPACE_DELETE[0],
                            ids=dtp.ALLNAME_FLD_SPACE_DELETE[1])
    def test_doc_patron_space_del_possit(self, login_doctor, params):
        """Позитивные проверки удаления пробела в начале и в конце отчества врача"""
        login_doctor.fill_the_field('PATRONYMIC_XP',
                                         params['INPUT'],
                                         'XPATH')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH',
                                        'XPATH')
        field_fact_data = str(login_doctor.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').get_attribute('value'))
        login_doctor.clear_field('PATRONYMIC_XP', 'XPATH')
        assert field_fact_data == str(params['INPUT']).strip(), 'Пробелы не удаляются после снятия фокуса'

    @allure.story('Позитивные проверки сохранения ввода отчества врача в том регистре, как ввел юзер')
    @pytest.mark.parametrize('params',
                            dtp.ALLNAME_FLD_TEXT_REGISTR[0],
                            ids=dtp.ALLNAME_FLD_TEXT_REGISTR[1])
    def test_вoc_patron_text_registr_possit(self, login_doctor, params):
        """Позитивные проверки сохранения ввода отчества врача в том регистре, в каком его ввел юзер"""
        login_doctor.fill_the_field('PATRONYMIC_XP',
                                         params['INPUT'],
                                         'XPATH')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH', 'XPATH')
        field_fact_data = str(login_doctor.get_elem_obj_or_ex('PATRONYMIC_XP', 'XPATH').get_attribute('value'))
        login_doctor.clear_field('PATRONYMIC_XP', 'XPATH')
        assert field_fact_data == str(params['INPUT']), 'Ввод сохраняется не в том регистре, в каком ввел юзер'

    @allure.story('Негативные проверки валидации отчества врача по мин кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtn.ALLNAME_FLD_MIN_LEN[0],
                            ids=dtn.ALLNAME_FLD_MIN_LEN[1])
    def test_doc_patron_valid_min_len_negot(self, login_doctor, params):
        """Негативные проверки валидации отчества врача по мин кол-ву символов"""
        login_doctor.fill_the_field('PATRONYMIC_XP',
                                         params['INPUT'],
                                         'XPATH')
        err_mess = str(
                login_doctor.get_elem_obj_or_ex('ER_MESS_PATRON_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('PATRONYMIC_XP', 'XPATH')
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
        login_doctor.fill_the_field('PATRONYMIC_XP',
                                         params['INPUT'],
                                         'XPATH')
        err_mess = str(
                login_doctor.get_elem_obj_or_ex('ER_MESS_PATRON_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('PATRONYMIC_XP', 'XPATH')
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
        login_doctor.fill_the_field('DBIRTH_FLD_NM', params['INPUT'], 'NAME')
        date_inserted = login_doctor.get_elem_obj_or_ex('DBIRTH_FLD_NM','NAME').get_attribute('value')
        assert date_inserted == params['INPUT'], 'Ввод сохраняется не так, как ввел пользователь'

        err_mess = str(
                login_doctor.get_elem_obj_or_ex('ER_MESS_DBIRTH_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('DBIRTH_FLD_NM', 'NAME')
        assert err_mess == '', 'При вводе валидной даты рождения появляется ошибка'

    @allure.story('Негативные проверки ввода невалидной даты рождения врача')
    @pytest.mark.parametrize('params',
                             dtn.DBIRTH_FLD_UNVALID[0],
                             ids=dtn.DBIRTH_FLD_UNVALID[1])
    def test_doc_birthdate_valid_negot(self, login_doctor, params):
        """Негативные проверки ввода невалидной даты рождения врача"""
        login_doctor.fill_the_field('DBIRTH_FLD_NM', params['INPUT'], 'NAME')
        date_inserted = login_doctor.get_elem_obj_or_ex('DBIRTH_FLD_NM', 'NAME').get_attribute('value')
        assert date_inserted == params['INPUT'], 'Ввод сохраняется не так, как ввел пользователь'

        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_DBIRTH_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('DBIRTH_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидной даты ошибки не возникает '
        assert err_mess != '' and err_mess == 'Некорректная дата', (f'Текст ошибки не соответсвует '
                                                                               f'требованиям, expected mess: '
                                                                               f'Некорректная дата, '
                                                                               f'fact mess: {err_mess}')

    @allure.story('Позитивная проверка ввода даты рождения при которой врачу ровно 18 лет')
    def test_doc_birthdate_eq_18(self, login_doctor):
        """Позитивные проверки ввода даты рождения, при которой врачу ровно 18"""
        # получаем дату 18 лет назад от текущей
        birthdate_to_test = login_doctor.get_date_18_years_ago().strftime("%d/%m/%Y")
        # вносим полученную дату
        login_doctor.fill_the_field('DBIRTH_FLD_NM', birthdate_to_test, 'NAME')
        # Получаем текст сообщения об ошибке или пустую строку, если ее нет
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_DBIRTH_XPATH', 'XPATH').get_attribute('textContent'))
        # Очищаем поле
        login_doctor.clear_field('DBIRTH_FLD_NM', 'NAME')
        # Проверяем, что сообщения об ошибки нет (пустая строка)
        assert err_mess == '', 'При вводе валидной даты появляется сообщение об ошибке'

    @allure.story('Позитивная проверка ввода даты рождения при которой врач старше 18 лет')
    def test_doc_birthdate_more_then_18(self, login_doctor):
        """Позитивные проверки ввода даты рождения, при которой врач старше 18"""
        # получаем дату 18 лет назад и еще минус один день
        birthdate_to_test = (login_doctor.get_date_18_years_ago() - timedelta(days=1)).strftime("%d/%m/%Y")
        # вводим полученную дату
        login_doctor.fill_the_field('DBIRTH_FLD_NM', birthdate_to_test, 'NAME')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_DBIRTH_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('DBIRTH_FLD_NM', 'NAME')
        assert err_mess == '', 'При вводе валидной даты появляется сообщение об ошибке'

    @allure.story('Негативная проверка ввода даты рождения при которой врач младше 18 лет')
    def test_doc_birthdate_less_then_18(self, login_doctor):
        """Негативная проверка ввода даты рождения при которой врач младше 18 лет"""
        birthdate_to_test = (login_doctor.get_date_18_years_ago() + timedelta(days=1)).strftime("%d/%m/%Y")
        login_doctor.fill_the_field('DBIRTH_FLD_NM', birthdate_to_test, 'NAME')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_DBIRTH_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('DBIRTH_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе даты рождения, при которой юзер младше 18 лет, ошибки не возникает '
        assert err_mess != '' and err_mess == 'Нельзя зарегистрироваться на сайте, если Вам меньше 18 лет', \
            (f'Текст ошибки не соответсвует требованиям, expected mess: "Нельзя зарегистрироваться на сайте, если Вам'
             f' меньше 18 лет", fact mess: "{err_mess}"')

# Проверки поля имейла закомментированы, так как теперь имейл введен по умолчанию и поле залочено
# @allure.feature('Проверки валидации поля Email врача')
# class TestEmailFieldDoctor:
#     @allure.story('Позитивные проверки валидации email врача по кол-ву симовлов')
#     @pytest.mark.parametrize('params',
#                             dtp.EMAIL_FLD_LEN[0],
#                             ids=dtp.EMAIL_FLD_LEN[1])
#     def test_doc_email_len_valid_possit(self, login_doctor, params):
#         """Позитивные проверки валидации поля Email врача по кол-ву символов"""
#         login_doctor.fill_the_field('EMAIL_FLD_NM', params['INPUT'], 'NAME')
#         err_mess = str(
#                 login_doctor.get_elem_obj_or_ex('ER_MESS_EMAIL_XPATH', 'XPATH').get_attribute('textContent'))
#         login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').send_keys(Keys.COMMAND + 'a')
#         login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').send_keys(Keys.BACKSPACE)
#         assert err_mess == '', 'При вводе валидного кол-ва символов появляется ошибка'
#
#     @allure.story('Позитивные проверки валидации email врача по типу вводимых симовлов')
#     @pytest.mark.parametrize('params',
#                              dtp.EMAIL_FLD_SYMB[0],
#                              ids=dtp.EMAIL_FLD_SYMB[1])
#     def test_doc_email_symb_valid_possit(self, login_doctor, params):
#         """Позитивные проверки валидации поля Email врача по типу вводимых символов"""
#         login_doctor.fill_the_field('EMAIL_FLD_NM', params['INPUT'], 'NAME')
#         err_mess = str(
#             login_doctor.get_elem_obj_or_ex('ER_MESS_EMAIL_XPATH', 'XPATH').get_attribute('textContent'))
#         login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').send_keys(Keys.COMMAND + 'a')
#         login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').send_keys(Keys.BACKSPACE)
#         assert err_mess == '', 'При вводе валидных типов символов появляется ошибка'
#
#     @allure.story('Негативные проверки валидации email врача по минимальному кол-ву символов')
#     @pytest.mark.parametrize('params',
#                              dtn.EMAIL_FLD_MIN_LEN[0],
#                              ids=dtn.EMAIL_FLD_MIN_LEN[1])
#     def test_doc_email_len_valid_negot(self, login_doctor, params):
#         """Негативные проверки валидации поля Email врача по минимальному кол-ву символов"""
#         login_doctor.fill_the_field('EMAIL_FLD_NM', params['INPUT'], 'NAME')
#         err_mess = str(
#             login_doctor.get_elem_obj_or_ex('ER_MESS_EMAIL_XPATH', 'XPATH').get_attribute('textContent'))
#         login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').send_keys(Keys.COMMAND + 'a')
#         login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').send_keys(Keys.BACKSPACE)
#         assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
#         assert err_mess != '' and err_mess == 'В поле должно быть минимум 6 символов', \
#             (f'Текст ошибки не соответсвует требованиям, expected mess: "В поле должно быть минимум 6 символов",'
#              f'fact mess: "{err_mess}"')
#
#     @allure.story('Негативные проверки валидации email врача по максимальному кол-ву символов')
#     @pytest.mark.parametrize('params',
#                              dtn.EMAIL_FLD_MAX_LEN[0],
#                              ids=dtn.EMAIL_FLD_MAX_LEN[1])
#     def test_doc_email_len_valid_negot(self, login_doctor, params):
#         """Негативные проверки валидации поля Email врача по максимальному кол-ву символов"""
#         login_doctor.fill_the_field('EMAIL_FLD_NM', params['INPUT'], 'NAME')
#         err_mess = str(
#             login_doctor.get_elem_obj_or_ex('ER_MESS_EMAIL_XPATH', 'XPATH').get_attribute('textContent'))
#         login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').send_keys(Keys.COMMAND + 'a')
#         login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').send_keys(Keys.BACKSPACE)
#         assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
#         assert err_mess != '' and err_mess == 'В поле должно быть максимум 70 символов', \
#             (f'Текст ошибки не соответствует требованиям, expected mess: "В поле должно быть максимум 70 символов",'
#              f'fact mess: "{err_mess}"')
#
#     @allure.story('Негативные проверки валидации email врача по маске')
#     @pytest.mark.parametrize('params',
#                              dtn.EMAIL_FLD_MASK[0],
#                              ids=dtn.EMAIL_FLD_MASK[1])
#     def test_doc_email_mask_valid_negot(self, login_doctor, params):
#         """Негативные проверки валидации поля Email врача по маске"""
#         login_doctor.fill_the_field('EMAIL_FLD_NM', params['INPUT'], 'NAME')
#         err_mess = str(
#             login_doctor.get_elem_obj_or_ex('ER_MESS_EMAIL_XPATH', 'XPATH').get_attribute('textContent'))
#         login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').send_keys(Keys.COMMAND + 'a')
#         login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').send_keys(Keys.BACKSPACE)
#         assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
#         assert err_mess != '' and err_mess == 'Допустимый формат почты: test@test.ru', \
#             (f'Текст ошибки не соответствует требованиям, expected mess: Допустимый формат почты: test@test.ru, '
#                                                                                f'fact mess: {err_mess}')
#
#     @allure.story('Позитивные проверки удаления пробелов в начале и в конце email врача')
#     @pytest.mark.parametrize('params',
#                              dtp.EMAIL_FLD_SPACE_DELETE[0],
#                              ids=dtp.EMAIL_FLD_SPACE_DELETE[1])
#     def test_doc_email_space_del_possit(self, login_doctor, params):
#         """Позитивные проверки удаления пробела в начале и в конце email врача"""
#         login_doctor.fill_the_field('EMAIL_FLD_NM', params['INPUT'], 'NAME')
#         login_doctor.click_element('LEFT_PAGE_AREA_XPATH', 'XPATH')
#         field_fact_data = str(login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').get_attribute('value'))
#         login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').send_keys(Keys.COMMAND + 'a')
#         login_doctor.get_elem_obj_or_ex('EMAIL_FLD_NM', 'NAME').send_keys(Keys.BACKSPACE)
#         assert field_fact_data == str(params['INPUT']).strip(), 'При вводе пробелы не удаляются'


@allure.feature('Проверки валидации поля Учебное заведение врача')
class TestEduInstitField:
    @allure.story('Позитивные проверки валидации поля Учебное заведение врача по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.EDU_INSTIT_FLD_LEN[0],
                            ids=dtp.EDU_INSTIT_FLD_LEN[1])
    def test_doc_edu_instit_len_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации поля Учебное заведение врача по кол-ву символов"""
        login_doctor.fill_the_field('UDU_INSTIT_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('UDU_INSTIT_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_EDU_INSTIT_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('UDU_INSTIT_FLD_NM', 'NAME')
        assert err_mess == '', 'при вводе валидного кол-ва символов появл ошибка'

    @allure.story('Негативные проверки валидации поля Учебное заведение врача по min кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.EDU_INSTIT_FLD_MIN_LEN[0],
                             ids=dtn.EDU_INSTIT_FLD_MIN_LEN[1])
    def test_doc_edu_instit_min_len_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Учеюное заведение врача по min кол-ву символов"""
        login_doctor.fill_the_field('UDU_INSTIT_FLD_NM', params['INPUT'], 'NAME')
        allergen_inserted = login_doctor.get_elem_obj_or_ex('UDU_INSTIT_FLD_NM', 'NAME').get_attribute('value')
        assert allergen_inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {allergen_inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_EDU_INSTIT_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('UDU_INSTIT_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Минимальная длина: 2 символа', \
            f'Текст ошибки не соответствует требованиям. Expect: "Минимальная длина: 2 символа", fact: "{err_mess}" '

    @allure.story('Негативные проверки валидации поля Учебное заведение врача по max кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.EDU_INSTIT_FLD_MAX_LEN[0],
                             ids=dtn.EDU_INSTIT_FLD_MAX_LEN[1])
    def test_doc_edu_instit_max_len_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Учебное заведение врача по max кол-ву символов"""
        login_doctor.fill_the_field('UDU_INSTIT_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('UDU_INSTIT_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                      f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_EDU_INSTIT_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('UDU_INSTIT_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Максимальная длина: 150 символов', \
            (f'Текст ошибки не соответсвует требованиям. Expected: "Максимальная длина: 150 символов", fact:'
             f'"{err_mess}" ')

    @allure.story('Позитивные проверки валидации поля Учебное заведение врача по типам символов')
    @pytest.mark.parametrize('params',
                             dtp.EDU_INSTIT_FLD_SYMB[0],
                             ids=dtp.EDU_INSTIT_FLD_SYMB[1])
    def test_doc_edu_instit_symb_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации поля Учебное заведение врача по типам символов"""
        login_doctor.fill_the_field('UDU_INSTIT_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('UDU_INSTIT_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (
            f'введенный текст отображается не так как ожидалось, expected input: {params["INPUT"]}, '
            f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_EDU_INSTIT_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('UDU_INSTIT_FLD_NM', 'NAME')
        assert err_mess == '', 'при вводе валидных типов символов появл ошибка'

    @allure.story('Негативные проверки валидации поля Учебное заведение врача по типам символов')
    @pytest.mark.parametrize('params',
                             dtn.EDU_INSTIT_FLD_SYMB[0],
                             ids=dtn.EDU_INSTIT_FLD_SYMB[1])
    def test_doc_edu_instit_symb_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Учебное заведение врача по типам символов"""
        login_doctor.fill_the_field('UDU_INSTIT_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('UDU_INSTIT_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (
            f'введенный текст отображается не так как ожидалось, expected input: {params["INPUT"]}, '
            f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_EDU_INSTIT_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('UDU_INSTIT_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидных типов символов ошибки не возникает '
        assert err_mess != '' and err_mess == ('Значение может содержать символы алфавита, пробел, '
                                               'дефис, цифры, символы ()№""'), \
            (f'Текст ошибки не соответсвует требованиям. Expected: "Значение может содержать символы алфавита, '
             f'пробел, дефис, цифры, символы ()№""", fact: "{err_mess}" ')


@allure.feature('Проверки валидации поля Специальность врача')
class TestSpecialField:
    @allure.story('Позитивные проверки валидации поля Специальность врача по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.SPECIAL_FLD_LEN[0],
                            ids=dtp.SPECIAL_FLD_LEN[1])
    def test_doc_special_len_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации поля Специальность врача по кол-ву символов"""
        login_doctor.fill_the_field('SPECIAL_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('SPECIAL_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_SPECIAL_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('SPECIAL_FLD_NM', 'NAME')
        assert err_mess == '', 'при вводе валидного кол-ва символов появл ошибка'

    @allure.story('Негативные проверки валидации поля Специальность врача по min кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.SPECIAL_FLD_MIN_LEN[0],
                             ids=dtn.SPECIAL_FLD_MIN_LEN[1])
    def test_doc_special_min_len_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Специальность врача по min кол-ву символов"""
        login_doctor.fill_the_field('SPECIAL_FLD_NM', params['INPUT'], 'NAME')
        allergen_inserted = login_doctor.get_elem_obj_or_ex('SPECIAL_FLD_NM', 'NAME').get_attribute('value')
        assert allergen_inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {allergen_inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_SPECIAL_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('SPECIAL_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Минимальная длина: 2 символа', \
            f'Текст ошибки не соответствует требованиям. Expect: "Минимальная длина: 2 символа", fact: "{err_mess}" '

    @allure.story('Негативные проверки валидации поля Специальность врача по max кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.SPECIAL_FLD_MAX_LEN[0],
                             ids=dtn.SPECIAL_FLD_MAX_LEN[1])
    def test_doc_special_max_len_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Специальность врача по max кол-ву символов"""
        login_doctor.fill_the_field('SPECIAL_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('SPECIAL_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                      f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_SPECIAL_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('SPECIAL_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Максимальная длина: 50 символов', \
            (f'Текст ошибки не соответсвует требованиям. Expected: "Максимальная длина: 50 символов", fact:'
             f'"{err_mess}" ')

    @allure.story('Позитивные проверки валидации поля Специальность врача по типам символов')
    @pytest.mark.parametrize('params',
                             dtp.SPECIAL_FLD_SYMB[0],
                             ids=dtp.SPECIAL_FLD_SYMB[1])
    def test_doc_special_symb_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации поля Специальность врача по типам символов"""
        login_doctor.fill_the_field('SPECIAL_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('SPECIAL_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (
            f'введенный текст отображается не так как ожидалось, expected input: {params["INPUT"]}, '
            f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_SPECIAL_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('SPECIAL_FLD_NM', 'NAME')
        assert err_mess == '', 'при вводе валидных типов символов появл ошибка'

    @allure.story('Негативные проверки валидации поля Специальность врача по типам символов')
    @pytest.mark.parametrize('params',
                             dtn.SPECIAL_FLD_SYMB[0],
                             ids=dtn.SPECIAL_FLD_SYMB[1])
    def test_doc_special_symb_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Специальность врача по типам символов"""
        login_doctor.fill_the_field('SPECIAL_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('SPECIAL_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (
            f'введенный текст отображается не так как ожидалось, expected input: {params["INPUT"]}, '
            f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_SPECIAL_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('SPECIAL_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидных типов символов ошибки не возникает '
        assert err_mess != '' and err_mess == ('Значение может содержать символы алфавита, пробел, '
                                               'дефис'), \
            (f'Текст ошибки не соответствует требованиям. Expected: "Значение может содержать символы алфавита, '
             f'пробел, дефис", fact: "{err_mess}" ')


@allure.feature('Проверки валидации поля Год окончания (образования)')
class TestEndOfEducField:
    @allure.story('Позитивные проверки валидации поля Год окончания (образования)')
    @pytest.mark.parametrize('params',
                            dtp.END_OF_EDUC_YEAR_FLD[0],
                            ids=dtp.END_OF_EDUC_YEAR_FLD[1])
    def test_end_of_educ_year_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации поля Год окончания (образования) по кол-ву символов"""
        login_doctor.fill_the_field('END_OF_EDUCATION_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('END_OF_EDUCATION_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_END_OF_EDUCATION_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('END_OF_EDUCATION_FLD_NM', 'NAME')
        assert err_mess == '', 'при вводе валидного года проведения операции появл ошибка'

    @allure.story('Негативные проверки валидации поля Год окончания (образования) при вводе менее 4 цифр')
    @pytest.mark.parametrize('params',
                            dtn.END_OF_EDUC_LEN_LESS_THEN_FOUR_DGT[0],
                            ids=dtn.END_OF_EDUC_LEN_LESS_THEN_FOUR_DGT[1])
    def test_end_of_educ_len_less_then_4_dig_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Год окончания (образования) при вводе менее 4 цифр"""
        login_doctor.fill_the_field('END_OF_EDUCATION_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('END_OF_EDUCATION_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_END_OF_EDUCATION_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('END_OF_EDUCATION_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидного кол-ва цифр ошибки не возникает '
        assert err_mess != '' and err_mess == 'Некорректная дата', (f'Текст ошибки не соответствует требованиям, '
                                                                    f'expected: "Некорректная дата", fact:{err_mess}')

    @allure.story('Негативные проверки валидации поля Год окончания (образования) на невозможность ввести символы, '
                  'отличные от цифр')
    @pytest.mark.parametrize('params',
                             dtn.END_OF_EDUC_CANT_INPUT[0],
                             ids=dtn.END_OF_EDUC_CANT_INPUT[1])
    def test_end_of_educ_cant_input_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Год окончания (образования) на невозможность ввести символы,
        отличные от цифр"""
        login_doctor.fill_the_field('END_OF_EDUCATION_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('END_OF_EDUCATION_FLD_NM', 'NAME').get_attribute('value')
        login_doctor.clear_field('END_OF_EDUCATION_FLD_NM', 'NAME')
        assert inserted == '', 'в поле можно ввести символы, отличные от цифр'

    @allure.story('Негативные проверки валидации поля Год окончания (образования) на невозможность ввести более 4 цифр')
    @pytest.mark.parametrize('params',
                             dtn.END_OF_EDUC_LEN_MORE_THEN_FOUR_DGT[0],
                             ids=dtn.END_OF_EDUC_LEN_MORE_THEN_FOUR_DGT[1])
    def test_end_of_educ_len_more_than_4_dig_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Год окончания (образования) на невозможность ввести более 4 цифр"""
        login_doctor.fill_the_field('END_OF_EDUCATION_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('END_OF_EDUCATION_FLD_NM', 'NAME').get_attribute('value')
        login_doctor.clear_field('END_OF_EDUCATION_FLD_NM', 'NAME')
        assert inserted == params['INPUT'][0:4], (f'Можно ввести более 4 цифр, expected {params["INPUT"][0:4]},'
                                                  f'fact: {inserted}')

    @allure.story('Негативные проверки валидации поля Год окончания (образования) ранее 1950 года')
    @pytest.mark.parametrize('params',
                             dtn.END_OF_EDUC_1950[0],
                             ids=dtn.END_OF_EDUC_1950[1])
    def test_end_of_educ_earlier_then_1950_negotive(self, login_doctor, params):
        """Негативные проверки валидации поля Год окончания (образования) ранее 1950 года"""
        login_doctor.fill_the_field('END_OF_EDUCATION_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('END_OF_EDUCATION_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], 'ввод не сохраняется в том виде, как ввел пользователь'

        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_END_OF_EDUCATION_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('END_OF_EDUCATION_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Дата не может быть ранее 1950 года', (
            f'Текст ошибки не соответсвует требованиям, '
            f'expected: "Дата не может быть ранее 1950 года", fact:{err_mess}')


@allure.feature('Проверки валидации поля Организация (повыш квалификации врача)')
class TestQualOrganizField:
    @allure.story('Позитивные проверки валидации поля Организация (повыш квалификации врача) по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.QUAL_ORGANIZATION_FLD_LEN[0],
                            ids=dtp.QUAL_ORGANIZATION_FLD_LEN[1])
    def test_doc_qual_organiz_len_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации поля Организация (повыш квалификации врача) по кол-ву символов"""
        login_doctor.fill_the_field('QUAL_ORGANIZATION_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('QUAL_ORGANIZATION_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_QUAL_ORGANIZ_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('QUAL_ORGANIZATION_FLD_NM', 'NAME')
        assert err_mess == '', f'при вводе валидного кол-ва символов появляется ошибка: "{err_mess}"'

    @allure.story('Негативные проверки валидации поля Организация (повыш квалификации врача) по min кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.QUAL_ORGANIZ_FLD_MIN_LEN[0],
                             ids=dtn.QUAL_ORGANIZ_FLD_MIN_LEN[1])
    def test_doc_qual_organiz_min_len_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Организация (повыш квалификации врача) по min кол-ву символов"""
        login_doctor.fill_the_field('QUAL_ORGANIZATION_FLD_NM', params['INPUT'], 'NAME')
        allergen_inserted = login_doctor.get_elem_obj_or_ex('QUAL_ORGANIZATION_FLD_NM', 'NAME').get_attribute('value')
        assert allergen_inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {allergen_inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_QUAL_ORGANIZ_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('QUAL_ORGANIZATION_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Минимальная длина: 2 символа', \
            f'Текст ошибки не соответствует требованиям. Expect: "Минимальная длина: 2 символа", fact: "{err_mess}" '

    @allure.story('Негативные проверки валидации поля Организация (повыш квалификации врача) по max кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.QUAL_ORGANIZ_FLD_MAX_LEN[0],
                             ids=dtn.QUAL_ORGANIZ_FLD_MAX_LEN[1])
    def test_doc_qual_organiz_max_len_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Организация (повыш квалификации врача) по max кол-ву символов"""
        login_doctor.fill_the_field('QUAL_ORGANIZATION_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('QUAL_ORGANIZATION_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                      f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_QUAL_ORGANIZ_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('QUAL_ORGANIZATION_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Максимальная длина: 150 символов', \
            (f'Текст ошибки не соответствует требованиям. Expected: "Максимальная длина: 150 символов", fact:'
             f'"{err_mess}" ')

    @allure.story('Позитивные проверки валидации поля Организация (повыш квалификации врача) по типам символов')
    @pytest.mark.parametrize('params',
                             dtp.QUAL_ORGANIZATION_FLD_SYMB[0],
                             ids=dtp.QUAL_ORGANIZATION_FLD_SYMB[1])
    def test_doc_qual_organiz_symb_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации поля Организация (повыш квалификации врача) по типам символов"""
        login_doctor.fill_the_field('QUAL_ORGANIZATION_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('QUAL_ORGANIZATION_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (
            f'введенный текст отображается не так как ожидалось, expected input: {params["INPUT"]}, '
            f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_QUAL_ORGANIZ_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('QUAL_ORGANIZATION_FLD_NM', 'NAME')
        assert err_mess == '', f'при вводе валидных типов символов появл ошибка: {err_mess}'

    @allure.story('Негативные проверки валидации поля Организация (повыш квалификации врача) по типам символов')
    @pytest.mark.parametrize('params',
                             dtn.QUAL_ORGANIZ_FLD_SYMB[0],
                             ids=dtn.QUAL_ORGANIZ_FLD_SYMB[1])
    def test_doc_qual_organiz_symb_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Организация (повыш квалификации врача) по типам символов"""
        login_doctor.fill_the_field('QUAL_ORGANIZATION_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('QUAL_ORGANIZATION_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (
            f'введенный текст отображается не так как ожидалось, expected input: {params["INPUT"]}, '
            f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_QUAL_ORGANIZ_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('QUAL_ORGANIZATION_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидных типов символов ошибки не возникает '
        assert err_mess != '' and err_mess == ('Значение может содержать символы алфавита, пробел, '
                                               'дефис, цифры, символы ()№""'), \
            (f'Текст ошибки не соответствует требованиям. Expected: "Значение может содержать символы алфавита, '
             f'пробел, дефис, цифры, символы ()№""", fact: "{err_mess}" ')

    @allure.story('Позитивные проверки сохранения ввода в том регистре, как ввел юзер')
    @pytest.mark.parametrize('params',
                         dtp.QUAL_ORGANIZATION_FLD_TEXT_REGISTR[0],
                         ids=dtp.QUAL_ORGANIZATION_FLD_TEXT_REGISTR[1])
    def test_doc_qual_organiz_text_registr_possit(self, login_doctor, params):
        """Позитивные проверки сохранения текста в том регистре, в каком его ввел юзер"""
        login_doctor.fill_the_field('QUAL_ORGANIZATION_FLD_NM', params['INPUT'], 'NAME')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH', 'XPATH')
        field_fact_data = str(login_doctor.get_elem_obj_or_ex('QUAL_ORGANIZATION_FLD_NM', 'NAME').get_attribute('value'))
        login_doctor.clear_field('QUAL_ORGANIZATION_FLD_NM', 'NAME')
        assert field_fact_data == str(params['INPUT']), (f"Введенные данные сохраняются не том регистре, в каком ввел"
                                                            f'юзер, expected: "{str(params["INPUT"])}", '
                                                            f'fact: "{field_fact_data}"')

    @allure.story('Позитивные проверки удаления пробелов в начале и в конце')
    @pytest.mark.parametrize('params',
                         dtp.QUAL_ORGANIZ_FLD_SPACE_DELETE[0],
                         ids=dtp.QUAL_ORGANIZ_FLD_SPACE_DELETE[1])
    def test_doc_qual_organiz_space_del_possit(self, login_doctor, params):
        """Позитивные проверки удаления пробела в начале и в конце"""
        login_doctor.fill_the_field('QUAL_ORGANIZATION_FLD_NM', params['INPUT'], 'NAME')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH', 'XPATH')
        field_fact_data = str(login_doctor.get_elem_obj_or_ex('QUAL_ORGANIZATION_FLD_NM', 'NAME').get_attribute('value'))
        login_doctor.clear_field('QUAL_ORGANIZATION_FLD_NM', 'NAME')
        assert field_fact_data == str(params['INPUT']).strip(), 'Пробелы не удаляются'


@allure.feature('Проверки валидации поля Название программы')
class TestProgNameField:
    @allure.story('Позитивные проверки валидации поля Название программы по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.PROG_NAME_FLD_LEN[0],
                            ids=dtp.PROG_NAME_FLD_LEN[1])
    def test_doc_prog_name_len_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации поля Название программы по кол-ву символов"""
        login_doctor.fill_the_field('PROG_NAME_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('PROG_NAME_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_PROG_NAME_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('PROG_NAME_FLD_NM', 'NAME')
        assert err_mess == '', f'при вводе валидного кол-ва символов появляется ошибка "{err_mess}"'

    @allure.story('Негативные проверки валидации поля Название программы по min кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.PROG_NAME_FLD_MIN_LEN[0],
                             ids=dtn.PROG_NAME_FLD_MIN_LEN[1])
    def test_doc_prog_name_min_len_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Название программы по min кол-ву символов"""
        login_doctor.fill_the_field('PROG_NAME_FLD_NM', params['INPUT'], 'NAME')
        allergen_inserted = login_doctor.get_elem_obj_or_ex('PROG_NAME_FLD_NM', 'NAME').get_attribute('value')
        assert allergen_inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {allergen_inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_PROG_NAME_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('PROG_NAME_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Минимальная длина: 2 символа', \
            f'Текст ошибки не соответствует требованиям. Expect: "Минимальная длина: 2 символа", fact: "{err_mess}" '

    @allure.story('Негативные проверки валидации поля Название программы по max кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.PROG_NAME_FLD_MAX_LEN[0],
                             ids=dtn.PROG_NAME_FLD_MAX_LEN[1])
    def test_doc_prog_name_max_len_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Название программы по max кол-ву символов"""
        login_doctor.fill_the_field('PROG_NAME_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('PROG_NAME_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                      f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_PROG_NAME_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('PROG_NAME_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Максимальная длина: 150 символов', \
            (f'Текст ошибки не соответствует требованиям. Expected: "Максимальная длина: 150 символов", fact:'
             f'"{err_mess}" ')

    @allure.story('Позитивные проверки валидации поля Название программы по типам символов')
    @pytest.mark.parametrize('params',
                             dtp.PROG_NAME_FLD_SYMB[0],
                             ids=dtp.PROG_NAME_FLD_SYMB[1])
    def test_doc_prog_name_symb_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации поля Название программы по типам символов"""
        login_doctor.fill_the_field('PROG_NAME_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('PROG_NAME_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (
            f'введенный текст отображается не так как ожидалось, expected input: {params["INPUT"]}, '
            f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_PROG_NAME_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('PROG_NAME_FLD_NM', 'NAME')
        assert err_mess == '', f'при вводе валидных типов символов появляется ошибка "{err_mess}"'

    @allure.story('Негативные проверки валидации поля Название программы по типам символов')
    @pytest.mark.parametrize('params',
                             dtn.PROG_NAME_FLD_SYMB[0],
                             ids=dtn.PROG_NAME_FLD_SYMB[1])
    def test_doc_prog_name_symb_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Название программы по типам символов"""
        login_doctor.fill_the_field('PROG_NAME_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('PROG_NAME_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (
            f'введенный текст отображается не так как ожидалось, expected input: {params["INPUT"]}, '
            f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_PROG_NAME_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('PROG_NAME_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидных типов символов ошибки не возникает '
        assert err_mess != '' and err_mess == ('Значение может содержать символы алфавита, пробел, '
                                               'дефис, цифры, символы ()№""'), \
            (f'Текст ошибки не соответсвует требованиям. Expected: "Значение может содержать символы алфавита, '
             f'пробел, дефис, цифры, символы ()№""", fact: "{err_mess}" ')

    @allure.story('Позитивные проверки сохранения ввода в том регистре, как ввел юзер')
    @pytest.mark.parametrize('params',
                         dtp.PROG_NAME_FLD_TEXT_REGISTR[0],
                         ids=dtp.PROG_NAME_FLD_TEXT_REGISTR[1])
    def test_doc_prog_name_text_registr_possit(self, login_doctor, params):
        """Позитивные проверки сохранения текста в том регистре, в каком его ввел юзер"""
        login_doctor.fill_the_field('PROG_NAME_FLD_NM', params['INPUT'], 'NAME')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH', 'XPATH')
        field_fact_data = str(login_doctor.get_elem_obj_or_ex('PROG_NAME_FLD_NM', 'NAME').get_attribute('value'))
        login_doctor.clear_field('PROG_NAME_FLD_NM', 'NAME')
        assert field_fact_data == str(params['INPUT']), (f"Введенные данные сохраняются не том регистре, в каком ввел"
                                                            f'юзер, expected: "{str(params["INPUT"])}", '
                                                            f'fact: "{field_fact_data}"')

    @allure.story('Позитивные проверки удаления пробелов в начале и в конце')
    @pytest.mark.parametrize('params',
                         dtp.PROG_NAME_FLD_SPACE_DELETE[0],
                         ids=dtp.PROG_NAME_FLD_SPACE_DELETE[1])
    def test_doc_prog_name_space_del_possit(self, login_doctor, params):
        """Позитивные проверки удаления пробела в начале и в конце"""
        login_doctor.fill_the_field('PROG_NAME_FLD_NM', params['INPUT'], 'NAME')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH', 'XPATH')
        field_fact_data = str(login_doctor.get_elem_obj_or_ex('PROG_NAME_FLD_NM', 'NAME').get_attribute('value'))
        login_doctor.clear_field('PROG_NAME_FLD_NM', 'NAME')
        assert field_fact_data == str(params['INPUT']).strip(), 'Пробелы не удаляются'


@allure.feature('Проверки валидации поля Год окончания (повыш квалификации)')
class TestEndOfQualField:
    @allure.story('Позитивные проверки валидации поля Год окончания (повыш квалификации)')
    @pytest.mark.parametrize('params',
                            dtp.END_OF_QUAL_YEAR_FLD[0],
                            ids=dtp.END_OF_QUAL_YEAR_FLD[1])
    def test_doc_end_of_qual_year_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации поля Год окончания (повыш квалификации) при вводе валидной даты"""
        login_doctor.fill_the_field('END_OF_QUAL_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('END_OF_QUAL_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_END_OF_QUAL_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('END_OF_QUAL_FLD_NM', 'NAME')
        assert err_mess == '', f'при вводе валидного года проведения операции появл ошибка "{err_mess}"'

    @allure.story('Негативные проверки валидации поля Год окончания (повыш квалификации) при вводе менее 4 цифр')
    @pytest.mark.parametrize('params',
                            dtn.END_OF_QUAL_LEN_LESS_THEN_FOUR_DGT[0],
                            ids=dtn.END_OF_QUAL_LEN_LESS_THEN_FOUR_DGT[1])
    def test_doc_end_of_qual_len_less_then_4_dig_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Год окончания (повыш квалификации) при вводе менее 4 цифр"""
        login_doctor.fill_the_field('END_OF_QUAL_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('END_OF_QUAL_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_END_OF_QUAL_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('END_OF_QUAL_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидного кол-ва цифр ошибки не возникает '
        assert err_mess != '' and err_mess == 'Некорректная дата', (f'Текст ошибки не соответствует требованиям, '
                                                                    f'expected: "Некорректная дата", fact:{err_mess}')

    @allure.story('Негативные проверки валидации поля Год окончания (повыш квалификации) на невозможность '
                  'ввести символы отличные от цифр')
    @pytest.mark.parametrize('params',
                             dtn.END_OF_QUAL_CANT_INPUT[0],
                             ids=dtn.END_OF_QUAL_CANT_INPUT[1])
    def test_doc_end_of_qual_cant_input_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Год окончания (повыш квалификации) на невозможность ввести символы,
        отличные от цифр"""
        login_doctor.fill_the_field('END_OF_QUAL_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('END_OF_QUAL_FLD_NM', 'NAME').get_attribute('value')
        login_doctor.clear_field('END_OF_QUAL_FLD_NM', 'NAME')
        assert inserted == '', 'в поле можно ввести символы, отличные от цифр'

    @allure.story('Негативные проверки валидации поля Год окончания (повыш квалификации) на невозможность '
                  'ввести более 4 цифр')
    @pytest.mark.parametrize('params',
                             dtn.END_OF_QUAL_LEN_MORE_THEN_FOUR_DGT[0],
                             ids=dtn.END_OF_QUAL_LEN_MORE_THEN_FOUR_DGT[1])
    def test_doc_end_of_qual_len_more_than_4_dig_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Год окончания (повыш квалификации) на невозможность ввести более 4 цифр"""
        login_doctor.fill_the_field('END_OF_QUAL_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('END_OF_QUAL_FLD_NM', 'NAME').get_attribute('value')
        login_doctor.clear_field('END_OF_QUAL_FLD_NM', 'NAME')
        assert inserted == params['INPUT'][0:4], (f'Можно ввести более 4 цифр, expected {params["INPUT"][0:4]},'
                                                  f'fact: {inserted}')

    @allure.story('Негативные проверки валидации поля Год окончания (повыш квалификации) ранее 1950 года')
    @pytest.mark.parametrize('params',
                             dtn.END_OF_QUAL_1950[0],
                             ids=dtn.END_OF_QUAL_1950[1])
    def test_doc_end_of_qual_earlier_then_1950_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Год окончания (повыш квалификации) ранее 1950 года"""
        login_doctor.fill_the_field('END_OF_QUAL_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('END_OF_QUAL_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], 'ввод не сохраняется в том виде, как ввел пользователь'

        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_END_OF_QUAL_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('END_OF_QUAL_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Дата не может быть ранее 1950 года', (
            f'Текст ошибки не соответствует требованиям, '
            f'expected: "Дата не может быть ранее 1950 года", fact:{err_mess}')


@allure.feature('Проверки валидации поля Организация (опыт работы)')
class TestJobOrgField:
    @allure.story('Позитивные проверки валидации поля Организация (опыт работы) по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.JOB_ORG_FLD_LEN[0],
                            ids=dtp.JOB_ORG_FLD_LEN[1])
    def test_doc_job_org_len_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации поля Организация (опыт работы) по кол-ву символов"""
        # Заполняем поле
        login_doctor.fill_the_field('JOB_ORG_FLD_NM', params['INPUT'], 'NAME')
        # Получаем текст, сохраненный в поле ввода
        inserted = login_doctor.get_elem_obj_or_ex('JOB_ORG_FLD_NM', 'NAME').get_attribute('value')
        # Проверяем, что сохраненный в поле текст = тому, что мы ввели
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        # Получаем текст сообщения об ошибке или пустую строку, если ошибки нет
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_JOB_ORG_XPATH', 'XPATH').get_attribute('textContent'))
        # Удаляем заполненный блок
        login_doctor.click_element('JOB_ORG_X_BTN_SEL', 'SELECTOR')
        # Проверяем, что текст сообщения об ошибке = пустой строке
        assert err_mess == '', f'при вводе валидного кол-ва символов появляется ошибка: "{err_mess}"'

    @allure.story('Негативные проверки валидации поля Организация (опыт работы) по min кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.JOB_ORG_FLD_MIN_LEN[0],
                             ids=dtn.JOB_ORG_FLD_MIN_LEN[1])
    def test_doc_job_org_min_len_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Организация (опыт работы) по min кол-ву символов"""
        login_doctor.fill_the_field('JOB_ORG_FLD_NM', params['INPUT'], 'NAME')
        allergen_inserted = login_doctor.get_elem_obj_or_ex('JOB_ORG_FLD_NM', 'NAME').get_attribute('value')
        assert allergen_inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {allergen_inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_JOB_ORG_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.click_element('JOB_ORG_X_BTN_SEL', 'SELECTOR')
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Минимальная длина: 2 символа', \
            f'Текст ошибки не соответствует требованиям. Expect: "Минимальная длина: 2 символа", fact: "{err_mess}" '

    @allure.story('Негативные проверки валидации поля Организация (опыт работы) по max кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.JOB_ORG_FLD_MAX_LEN[0],
                             ids=dtn.JOB_ORG_FLD_MAX_LEN[1])
    def test_doc_job_org_max_len_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Организация (опыт работы) по max кол-ву символов"""
        login_doctor.fill_the_field('JOB_ORG_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('JOB_ORG_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                      f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_JOB_ORG_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.click_element('JOB_ORG_X_BTN_SEL', 'SELECTOR')
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Максимальная длина: 150 символов', \
            (f'Текст ошибки не соответствует требованиям. Expected: "Максимальная длина: 150 символов", fact:'
             f'"{err_mess}" ')

    @allure.story('Позитивные проверки валидации поля Организация (опыт работы) по типам символов')
    @pytest.mark.parametrize('params',
                             dtp.JOB_ORG_FLD_SYMB[0],
                             ids=dtp.JOB_ORG_FLD_SYMB[1])
    def test_doc_job_org_symb_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации поля Организация (опыт работы) по типам символов"""
        login_doctor.fill_the_field('JOB_ORG_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('JOB_ORG_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (
            f'введенный текст отображается не так как ожидалось, expected input: {params["INPUT"]}, '
            f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_JOB_ORG_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.click_element('JOB_ORG_X_BTN_SEL', 'SELECTOR')
        assert err_mess == '', f'при вводе валидных типов символов появл ошибка: {err_mess}'

    @allure.story('Негативные проверки валидации поля Организация (опыт работы) по типам символов')
    @pytest.mark.parametrize('params',
                             dtn.JOB_ORG_FLD_SYMB[0],
                             ids=dtn.JOB_ORG_FLD_SYMB[1])
    def test_doc_job_org_symb_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Организация (опыт работы) по типам символов"""
        login_doctor.fill_the_field('JOB_ORG_FLD_NM',
                                    params['INPUT'],
                                    'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('JOB_ORG_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (
            f'введенный текст отображается не так как ожидалось, expected input: {params["INPUT"]}, '
            f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_JOB_ORG_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.click_element('JOB_ORG_X_BTN_SEL', 'SELECTOR')
        assert err_mess != '', 'При вводе невалидных типов символов ошибки не возникает '
        assert err_mess != '' and err_mess == ('Значение может содержать символы алфавита, пробел, '
                                               'дефис, цифры, символы ()№""'), \
            (f'Текст ошибки не соответствует требованиям. Expected: "Значение может содержать символы алфавита, '
             f'пробел, дефис, цифры, символы ()№""", fact: "{err_mess}" ')

    @allure.story('Позитивные проверки сохранения ввода в том регистре, как ввел юзер')
    @pytest.mark.parametrize('params',
                         dtp.JOB_ORG_FLD_TEXT_REGISTR[0],
                         ids=dtp.JOB_ORG_FLD_TEXT_REGISTR[1])
    def test_doc_job_org_text_registr_possit(self, login_doctor, params):
        """Позитивные проверки сохранения текста в том регистре, в каком его ввел юзер"""
        login_doctor.fill_the_field('JOB_ORG_FLD_NM',
                            params['INPUT'],
                            'NAME')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH',
                        'XPATH')
        field_fact_data = str(login_doctor.get_elem_obj_or_ex('JOB_ORG_FLD_NM', 'NAME').get_attribute('value'))
        login_doctor.click_element('JOB_ORG_X_BTN_SEL', 'SELECTOR')
        assert field_fact_data == str(params['INPUT']), (f"Введенные данные сохраняются не том регистре, в каком ввел"
                                                            f'юзер, expected: "{str(params["INPUT"])}", '
                                                            f'fact: "{field_fact_data}"')

    @allure.story('Позитивные проверки удаления пробелов в начале и в конце')
    @pytest.mark.parametrize('params',
                         dtp.JOB_ORG_FLD_SPACE_DELETE[0],
                         ids=dtp.JOB_ORG_FLD_SPACE_DELETE[1])
    def test_doc_job_org_space_del_possit(self, login_doctor, params):
        """Позитивные проверки удаления пробела в начале и в конце"""
        login_doctor.fill_the_field('JOB_ORG_FLD_NM',
                            params['INPUT'],
                            'NAME')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH',
                                    'XPATH')
        field_fact_data = str(login_doctor.get_elem_obj_or_ex('JOB_ORG_FLD_NM', 'NAME').get_attribute('value'))
        login_doctor.click_element('JOB_ORG_X_BTN_SEL', 'SELECTOR')
        assert field_fact_data == str(params['INPUT']).strip(), 'Пробелы не удаляются'


@allure.feature('Проверки валидации поля Должность (опыт работы врача)')
class TestPositionField:
    @allure.story('Позитивные проверки валидации поля Должность (опыт работы врача) по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.POSITION_FLD_LEN[0],
                            ids=dtp.POSITION_FLD_LEN[1])
    def test_doc_position_len_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации поля Должность (опыт работы врача) по кол-ву символов"""
        login_doctor.fill_the_field('POSITION_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('POSITION_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_POSITION_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.click_element('POSITION_X_BTN_SEL', 'SELECTOR')
        assert err_mess == '', f'при вводе валидного кол-ва символов появляется ошибка: "{err_mess}"'

    @allure.story('Негативные проверки валидации поля Должность (опыт работы врача) по min кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.POSITION_FLD_MIN_LEN[0],
                             ids=dtn.POSITION_FLD_MIN_LEN[1])
    def test_do_position_min_len_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Должность (опыт работы врача) по min кол-ву символов"""
        login_doctor.fill_the_field('POSITION_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        allergen_inserted = login_doctor.get_elem_obj_or_ex('POSITION_FLD_NM', 'NAME').get_attribute('value')
        assert allergen_inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {allergen_inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_POSITION_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.click_element('POSITION_X_BTN_SEL', 'SELECTOR')
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Минимальная длина: 2 символа', \
            f'Текст ошибки не соответствует требованиям. Expect: "Минимальная длина: 2 символа", fact: "{err_mess}" '

    @allure.story('Негативные проверки валидации поля Должность (опыт работы врача) по max кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.POSITION_FLD_MAX_LEN[0],
                             ids=dtn.POSITION_FLD_MAX_LEN[1])
    def test_doc_position_max_len_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Должность (опыт работы врача) по max кол-ву символов"""
        login_doctor.fill_the_field('POSITION_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('POSITION_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                      f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_POSITION_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.click_element('POSITION_X_BTN_SEL', 'SELECTOR')
        assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
        assert err_mess != '' and err_mess == 'Максимальная длина: 50 символов', \
            (f'Текст ошибки не соответствует требованиям. Expected: "Максимальная длина: 50 символов", fact:'
             f'"{err_mess}" ')

    @allure.story('Позитивные проверки валидации поля Должность (опыт работы врача) по типам символов')
    @pytest.mark.parametrize('params',
                             dtp.POSITION_FLD_SYMB[0],
                             ids=dtp.POSITION_FLD_SYMB[1])
    def test_doc_position_symb_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации поля Должность (опыт работы врача) по типам символов"""
        login_doctor.fill_the_field('POSITION_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('POSITION_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (
            f'введенный текст отображается не так как ожидалось, expected input: {params["INPUT"]}, '
            f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_POSITION_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.click_element('POSITION_X_BTN_SEL', 'SELECTOR')
        assert err_mess == '', f'при вводе валидных типов символов появл ошибка: {err_mess}'

    @allure.story('Негативные проверки валидации поля Должность (опыт работы врача) по типам символов')
    @pytest.mark.parametrize('params',
                             dtn.POSITION_FLD_SYMB[0],
                             ids=dtn.POSITION_FLD_SYMB[1])
    def test_doc_position_symb_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Должность (опыт работы врача) по типам символов"""
        login_doctor.fill_the_field('POSITION_FLD_NM',
                                    params['INPUT'],
                                    'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('POSITION_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (
            f'введенный текст отображается не так как ожидалось, expected input: {params["INPUT"]}, '
            f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_POSITION_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.click_element('POSITION_X_BTN_SEL', 'SELECTOR')
        assert err_mess != '', 'При вводе невалидных типов символов ошибки не возникает '
        assert err_mess != '' and err_mess == ('Значение может содержать символы алфавита, пробел, '
                                               'дефис, цифры, символы ()№""'), \
            (f'Текст ошибки не соответствует требованиям. Expected: "Значение может содержать символы алфавита, '
             f'пробел, дефис, цифры, символы ()№""", fact: "{err_mess}" ')

    @allure.story('Позитивные проверки сохранения ввода в том регистре, как ввел юзер')
    @pytest.mark.parametrize('params',
                         dtp.POSITION_FLD_TEXT_REGISTR[0],
                         ids=dtp.POSITION_FLD_TEXT_REGISTR[1])
    def test_doc_position_text_registr_possit(self, login_doctor, params):
        """Позитивные проверки сохранения текста в том регистре, в каком его ввел юзер"""
        login_doctor.fill_the_field('POSITION_FLD_NM',
                            params['INPUT'],
                            'NAME')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH',
                        'XPATH')
        field_fact_data = str(login_doctor.get_elem_obj_or_ex('POSITION_FLD_NM', 'NAME').get_attribute('value'))
        login_doctor.click_element('POSITION_X_BTN_SEL', 'SELECTOR')
        assert field_fact_data == str(params['INPUT']), (f"Введенные данные сохраняются не том регистре, в каком ввел"
                                                            f'юзер, expected: "{str(params["INPUT"])}", '
                                                            f'fact: "{field_fact_data}"')

    @allure.story('Позитивные проверки удаления пробелов в начале и в конце')
    @pytest.mark.parametrize('params',
                         dtp.POSITION_FLD_SPACE_DELETE[0],
                         ids=dtp.POSITION_FLD_SPACE_DELETE[1])
    def test_doc_position_space_del_possit(self, login_doctor, params):
        """Позитивные проверки удаления пробела в начале и в конце"""
        login_doctor.fill_the_field('POSITION_FLD_NM',
                            params['INPUT'],
                            'NAME')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH',
                                    'XPATH')
        field_fact_data = str(login_doctor.get_elem_obj_or_ex('POSITION_FLD_NM', 'NAME').get_attribute('value'))
        login_doctor.click_element('POSITION_X_BTN_SEL', 'SELECTOR')
        assert field_fact_data == str(params['INPUT']).strip(), 'Пробелы не удаляются'


@allure.feature('Проверки валидации поля "Период работы - с"')
class TestJobStartDateField:
    @allure.story('Позитивные проверки валидации поля "Период работы - с"')
    @pytest.mark.parametrize('params',
                            dtp.JOB_START_DATE_FLD[0],
                            ids=dtp.JOB_START_DATE_FLD[1])
    def test_doc_job_start_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации поля "Период работы - с" при вводе валидной даты"""
        login_doctor.fill_the_field('JOB_START_DATE_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('JOB_START_DATE_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_JOB_START_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('JOB_START_DATE_FLD_NM', 'NAME')
        assert err_mess == '', f'при вводе валидного года проведения операции появл ошибка "{err_mess}"'

    @allure.story('Негативные проверки валидации поля "Период работы - с" при вводе менее 6 цифр')
    @pytest.mark.parametrize('params',
                            dtn.JOB_START_DATE_LEN_LESS_THEN_SIX_DGT[0],
                            ids=dtn.JOB_START_DATE_LEN_LESS_THEN_SIX_DGT[1])
    def test_doc_job_start_len_less_then_6_dig_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля "Период работы - с" при вводе менее 6 цифр"""
        login_doctor.fill_the_field('JOB_START_DATE_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('JOB_START_DATE_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_JOB_START_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('JOB_START_DATE_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидного кол-ва цифр ошибки не возникает '
        assert err_mess != '' and err_mess == 'Некорректная дата', (f'Текст ошибки не соответствует требованиям, '
                                                                    f'expected: "Некорректная дата", '
                                                                         f'fact:{err_mess}')

    @allure.story('Негативные проверки ввода невалидной даты в поле "Период работы - с"')
    @pytest.mark.parametrize('params',
                             dtn.JOB_START_DATE_UNVALID[0],
                             ids=dtn.JOB_START_DATE_UNVALID[1])
    def test_doc_job_start_valid_negot(self, login_doctor, params):
        """Негативные проверки ввода невалидной даты в поле Период работы - с"""
        login_doctor.fill_the_field('JOB_START_DATE_FLD_NM',
                                    params['INPUT'],
                                    'NAME')
        date_inserted = login_doctor.get_elem_obj_or_ex('JOB_START_DATE_FLD_NM', 'NAME').get_attribute('value')
        assert date_inserted == params['INPUT'], 'Ввод сохраняется не так, как ввел пользователь'

        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_JOB_START_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('JOB_START_DATE_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидной даты ошибки не возникает '
        assert err_mess != '' and err_mess == 'Некорректная дата', (f'Текст ошибки не соответствует '
                                                                    f'требованиям, expected mess: '
                                                                    f'"Некорректная дата", '
                                                                    f'fact mess: "{err_mess}"')

    @allure.story('Негативные проверки ввода невалидной даты (ранее 1950) в поле "Период работы - с"')
    @pytest.mark.parametrize('params',
                             dtn.JOB_START_LESS_1950_UNVALID[0],
                             ids=dtn.JOB_START_LESS_1950_UNVALID[1])
    def test_doc_job_start_earlier_valid_negot(self, login_doctor, params):
        """Негативные проверки ввода невалидной даты (ранее 1950) в поле Период работы - с"""
        login_doctor.fill_the_field('JOB_START_DATE_FLD_NM',
                                    params['INPUT'],
                                    'NAME')
        date_inserted = login_doctor.get_elem_obj_or_ex('JOB_START_DATE_FLD_NM', 'NAME').get_attribute('value')
        assert date_inserted == params['INPUT'], 'Ввод сохраняется не так, как ввел пользователь'

        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_JOB_START_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('JOB_START_DATE_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидной даты ошибки не возникает '
        assert err_mess != '' and err_mess == 'Дата не может быть ранее 1950 года', (f'Текст ошибки не соответствует '
                                                                                     f'требованиям, expected mess: '
                                                                                     f'"Дата не может быть ранее '
                                                                                     f'1950 года", '
                                                                                     f'fact mess: "{err_mess}"')

    @allure.story('Негативные проверки валидации поля "Период работы - с" на невозможность ввести символы '
                  'отличные от цифр')
    @pytest.mark.parametrize('params',
                             dtn.JOB_START_CANT_INPUT[0],
                             ids=dtn.JOB_START_CANT_INPUT[1])
    def test_doc_job_start_cant_input_negot(self, login_doctor, params):
        """Негативные проверки валидации поля 'Период работы - с' на невозможность ввести символы отличные от цифр"""
        login_doctor.fill_the_field('JOB_START_DATE_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('JOB_START_DATE_FLD_NM', 'NAME').get_attribute('value')
        login_doctor.clear_field('JOB_START_DATE_FLD_NM', 'NAME')
        assert inserted == '', 'в поле можно ввести символы, отличные от цифр'

    @allure.story('Негативные проверки валидации поля "Период работы - с" на невозможность '
                  'ввести более 6 цифр')
    @pytest.mark.parametrize('params',
                             dtn.JOB_STRT_MORE_THEN_SIX_DGT[0],
                             ids=dtn.JOB_STRT_MORE_THEN_SIX_DGT[1])
    def test_doc_job_start_more_than_6_dig_negot(self, login_doctor, params):
        """Негативные проверки валидации поля 'Период работы - с' на невозможность ввести более 6 цифр"""
        login_doctor.fill_the_field('JOB_START_DATE_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('JOB_START_DATE_FLD_NM', 'NAME').get_attribute('value')
        login_doctor.clear_field('JOB_START_DATE_FLD_NM', 'NAME')
        assert inserted == params['INPUT'][0:7], (f'Можно ввести более 6 цифр, expected {params["INPUT"][0:7]},'
                                                  f'fact: {inserted}')


@allure.feature('Проверки валидации поля "Период работы - по"')
class TestJobEndDateField:
    @allure.story('Позитивные проверки валидации поля "Период работы - по"')
    @pytest.mark.parametrize('params',
                            dtp.JOB_END_DATE_FLD[0],
                            ids=dtp.JOB_END_DATE_FLD[1])
    def test_doc_job_end_valid_possit(self, login_doctor, params):
        """Позитивные проверки валидации поля 'Период работы - по' при вводе валидной даты"""
        login_doctor.fill_the_field('JOB_END_DATE_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('JOB_END_DATE_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_JOB_END_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('JOB_END_DATE_FLD_NM', 'NAME')
        assert err_mess == '', f'при вводе валидного года проведения операции появл ошибка "{err_mess}"'

    @allure.story('Негативные проверки валидации поля "Период работы - по" при вводе менее 6 цифр')
    @pytest.mark.parametrize('params',
                            dtn.JOB_END_DATE_LEN_LESS_THEN_SIX_DGT[0],
                            ids=dtn.JOB_END_DATE_LEN_LESS_THEN_SIX_DGT[1])
    def test_doc_job_end_len_less_then_6_dig_valid_negot(self, login_doctor, params):
        """Негативные проверки валидации поля "Период работы - по" при вводе менее 6 цифр"""
        login_doctor.fill_the_field('JOB_END_DATE_FLD_NM',
                                         params['INPUT'],
                                         'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('JOB_END_DATE_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_JOB_END_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('JOB_END_DATE_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидного кол-ва цифр ошибки не возникает '
        assert err_mess != '' and err_mess == 'Некорректная дата', (f'Текст ошибки не соответствует требованиям, '
                                                                    f'expected: "Некорректная дата", '
                                                                         f'fact:{err_mess}')

    @allure.story('Негативные проверки ввода невалидной даты в поле "Период работы - по"')
    @pytest.mark.parametrize('params',
                             dtn.JOB_END_DATE_UNVALID[0],
                             ids=dtn.JOB_END_DATE_UNVALID[1])
    def test_doc_job_end_valid_negot(self, login_doctor, params):
        """Негативные проверки ввода невалидной даты в поле Период работы - по"""
        login_doctor.fill_the_field('JOB_END_DATE_FLD_NM',
                                    params['INPUT'],
                                    'NAME')
        date_inserted = login_doctor.get_elem_obj_or_ex('JOB_END_DATE_FLD_NM', 'NAME').get_attribute('value')
        assert date_inserted == params['INPUT'], 'Ввод сохраняется не так, как ввел пользователь'
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_JOB_END_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('JOB_END_DATE_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидной даты ошибки не возникает '
        assert err_mess != '' and err_mess == 'Некорректная дата', (f'Текст ошибки не соответствует '
                                                                    f'требованиям, expected mess: '
                                                                    f'"Некорректная дата", '
                                                                    f'fact mess: "{err_mess}"')

    @allure.story('Негативные проверки ввода невалидной даты (ранее 1950) в поле "Период работы - по"')
    @pytest.mark.parametrize('params',
                             dtn.JOB_END_LESS_1950_UNVALID[0],
                             ids=dtn.JOB_END_LESS_1950_UNVALID[1])
    def test_doc_job_end_earlier_valid_negot(self, login_doctor, params):
        """Негативные проверки ввода невалидной даты (ранее 1950) в поле Период работы - по"""
        login_doctor.fill_the_field('JOB_END_DATE_FLD_NM',
                                    params['INPUT'],
                                    'NAME')
        date_inserted = login_doctor.get_elem_obj_or_ex('JOB_END_DATE_FLD_NM', 'NAME').get_attribute('value')
        assert date_inserted == params['INPUT'], 'Ввод сохраняется не так, как ввел пользователь'

        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_JOB_END_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('JOB_END_DATE_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидной даты ошибки не возникает '
        assert err_mess != '' and err_mess == 'Дата не может быть ранее 1950 года', (f'Текст ошибки не соответствует '
                                                                                     f'требованиям, expected mess: '
                                                                                     f'"Дата не может быть ранее '
                                                                                     f'1950 года", '
                                                                                     f'fact mess: "{err_mess}"')

    @allure.story('Негативные проверки валидации поля "Период работы - по" на невозможность ввести символы '
                  'отличные от цифр')
    @pytest.mark.parametrize('params',
                             dtn.JOB_END_CANT_INPUT[0],
                             ids=dtn.JOB_END_CANT_INPUT[1])
    def test_doc_job_end_cant_input_negot(self, login_doctor, params):
        """Негативные проверки валидации поля 'Период работы - по' на невозможность ввести символы отличные от цифр"""
        login_doctor.fill_the_field('JOB_END_DATE_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('JOB_END_DATE_FLD_NM', 'NAME').get_attribute('value')
        login_doctor.clear_field('JOB_END_DATE_FLD_NM', 'NAME')
        assert inserted == '', 'в поле можно ввести символы, отличные от цифр'

    @allure.story('Негативные проверки валидации поля "Период работы - по" на невозможность '
                  'ввести более 6 цифр')
    @pytest.mark.parametrize('params',
                             dtn.JOB_END_MORE_THEN_SIX_DGT[0],
                             ids=dtn.JOB_END_MORE_THEN_SIX_DGT[1])
    def test_doc_job_start_more_than_6_dig_negot(self, login_doctor, params):
        """Негативные проверки валидации поля 'Период работы - по' на невозможность ввести более 6 цифр"""
        login_doctor.fill_the_field('JOB_END_DATE_FLD_NM',
                                     params['INPUT'],
                                     'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('JOB_END_DATE_FLD_NM', 'NAME').get_attribute('value')
        login_doctor.clear_field('JOB_END_DATE_FLD_NM', 'NAME')
        assert inserted == params['INPUT'][0:7], (f'Можно ввести более 6 цифр, expected {params["INPUT"][0:7]},'
                                                  f'fact: {inserted}')


@allure.feature('Проверки валидации поля Диагностика и лечение ')
class TestDiagnosticField:
    # @allure.story('Позитивные проверки валидации поля Диагностика и лечение по кол-ву символов')
    # @pytest.mark.parametrize('params',
    #                         dtp.DIAGNOSTIC_FLD_LEN[0],
    #                         ids=dtp.DIAGNOSTIC_FLD_LEN[1])
    # def test_doc_diagnostic_len_possit(self, login_doctor, params):
    #     """Позитивные проверки валидации поля Диагностика и лечение по кол-ву символов"""
    #     login_doctor.fill_the_field('DIAGNOSTC_FLD_XP',
    #                                      params['INPUT'],
    #                                      'XPATH')
    #     inserted = login_doctor.get_elem_obj_or_ex('DIAGNOSTC_FLD_XP', 'XPATH').text
    #     assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
    #                                                     f'fact input: {inserted}')
    #     err_mess = str(
    #         login_doctor.get_elem_obj_or_ex('ER_MESS_POSITION_XPATH', 'XPATH').get_attribute('textContent'))
    #     login_doctor.clear_field('DIAGNOSTC_FLD_XP', 'XPATH')
    #     assert err_mess == '', f'при вводе валидного кол-ва символов появляется ошибка: "{err_mess}"'

    # @allure.story('Негативные проверки валидации поля Диагностика и лечение по min кол-ву символов')
    # @pytest.mark.parametrize('params',
    #                          dtn.DIAGNOSTIC_FLD_MIN_LEN[0],
    #                          ids=dtn.DIAGNOSTIC_FLD_MIN_LEN[1])
    # def test_doc_diagnostic_min_len_negot(self, login_doctor, params):
    #     """Негативные проверки валидации поля Диагностика и лечение по min кол-ву символов"""
    #     login_doctor.fill_the_field('DIAGNOSTC_FLD_XP', params['INPUT'], 'XPATH')
    #     inserted = login_doctor.get_elem_obj_or_ex('DIAGNOSTC_FLD_XP', 'XPATH').text
    #     assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
    #                                                     f'fact input: {inserted}')
    #     err_mess = str(
    #         login_doctor.get_elem_obj_or_ex('ER_MESS_POSITION_XPATH', 'XPATH').get_attribute('textContent'))
    #     login_doctor.get_elem_obj_or_ex('DIAGNOSTC_FLD_XP', 'XPATH').send_keys(Keys.COMMAND + 'a')
    #     login_doctor.get_elem_obj_or_ex('DIAGNOSTC_FLD_XP', 'XPATH').send_keys(Keys.BACKSPACE)
    #     assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
    #     assert err_mess != '' and err_mess == 'Минимальная длина: 2 символа', \
    #         f'Текст ошибки не соответствует требованиям. Expect: "Минимальная длина: 2 символа", fact: "{err_mess}" '

    # @allure.story('Негативные проверки валидации поля Диагностика и лечение по max кол-ву символов')
    # @pytest.mark.parametrize('params',
    #                          dtn.DIAGNOSTIC_FLD_MAX_LEN[0],
    #                          ids=dtn.DIAGNOSTIC_FLD_MAX_LEN[1])
    # def test_doc_diagnostic_max_len_negot(self, login_doctor, params):
    #     """Негативные проверки валидации поля Диагностика и лечение по max кол-ву символов"""
    #     login_doctor.fill_the_field('DIAGNOSTC_FLD_XP', params['INPUT'], 'XPATH')
    #     inserted = login_doctor.get_elem_obj_or_ex('DIAGNOSTC_FLD_XP', 'XPATH').text
    #     assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
    #                                                   f'fact input: {inserted}')
    #     err_mess = str(
    #         login_doctor.get_elem_obj_or_ex('ER_MESS_POSITION_XPATH', 'XPATH').get_attribute('textContent'))
    #     login_doctor.get_elem_obj_or_ex('DIAGNOSTC_FLD_XP', 'XPATH').send_keys(Keys.COMMAND + 'a')
    #     login_doctor.get_elem_obj_or_ex('DIAGNOSTC_FLD_XP', 'XPATH').send_keys(Keys.BACKSPACE)
    #     assert err_mess != '', 'При вводе невалидного кол-ва символов ошибки не возникает '
    #     assert err_mess != '' and err_mess == 'Максимальная длина: 2000 символов', \
    #         (f'Текст ошибки не соответствует требованиям. Expected: "Максимальная длина: 2000 символов", fact:'
    #          f'"{err_mess}" ')
    #
    # @allure.story('Позитивные проверки валидации поля Диагностика и лечение по типам символов')
    # @pytest.mark.parametrize('params',
    #                          dtp.DIAGNOSTIC_FLD_SYMB[0],
    #                          ids=dtp.DIAGNOSTIC_FLD_SYMB[1])
    # def test_doc_diagnostic_symb_possit(self, login_doctor, params):
    #     """Позитивные проверки валидации поля Диагностика и лечение по типам символов"""
    #     login_doctor.fill_the_field('DIAGNOSTC_FLD_XP', params['INPUT'], 'XPATH')
    #     inserted = login_doctor.get_elem_obj_or_ex('DIAGNOSTC_FLD_XP', 'XPATH').text
    #     assert inserted == params['INPUT'], (
    #         f'введенный текст отображается не так как ожидалось, expected input: {params["INPUT"]}, '
    #         f'fact input: {inserted}')
    #     err_mess = str(
    #         login_doctor.get_elem_obj_or_ex('ER_MESS_POSITION_XPATH', 'XPATH').get_attribute('textContent'))
    #     login_doctor.clear_field('DIAGNOSTC_FLD_XP', 'XPATH')
    #     assert err_mess == '', f'при вводе валидных типов символов появл ошибка: {err_mess}'

    @allure.story('Позитивные проверки сохранения ввода в том регистре, как ввел юзер')
    @pytest.mark.parametrize('params',
                         dtp.DIAGNOSTIC_FLD_TEXT_REGISTR[0],
                         ids=dtp.DIAGNOSTIC_FLD_TEXT_REGISTR[1])
    def test_doc_diagnostic_txt_registr_possit(self, login_doctor, params):
        """Позитивные проверки сохранения текста в том регистре, в каком его ввел юзер"""
        login_doctor.fill_the_field('DIAGNOSTC_FLD_XP', params['INPUT'], 'XPATH')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH','XPATH')
        field_fact_data = login_doctor.get_elem_obj_or_ex('DIAGNOSTC_FLD_XP', 'XPATH').text
        login_doctor.clear_field('DIAGNOSTC_FLD_XP', 'XPATH')
        assert field_fact_data == str(params['INPUT']), (f"Введенные данные сохраняются не том регистре, в каком ввел"
                                                            f'юзер, expected: "{str(params["INPUT"])}", '
                                                            f'fact: "{field_fact_data}"')

    # @allure.story('Позитивные проверки удаления пробелов в начале и в конце')
    # @pytest.mark.parametrize('params',
    #                      dtp.DIAGNOSTIC_FLD_SPACE_DELETE[0],
    #                      ids=dtp.DIAGNOSTIC_FLD_SPACE_DELETE[1])
    # def test_doc_diagnstc_space_del_possit(self, login_doctor, params):
    #     """Позитивные проверки удаления пробела в начале и в конце"""
    #     login_doctor.fill_the_field('DIAGNOSTC_FLD_XP', params['INPUT'], 'XPATH')
    #     login_doctor.click_element('LEFT_PAGE_AREA_XPATH', 'XPATH')
    #     field_fact_data = login_doctor.get_elem_obj_or_ex('DIAGNOSTC_FLD_XP', 'XPATH').text
    #     login_doctor.get_elem_obj_or_ex('DIAGNOSTC_FLD_XP', 'XPATH').send_keys(Keys.COMMAND + 'a')
    #     login_doctor.get_elem_obj_or_ex('DIAGNOSTC_FLD_XP', 'XPATH').send_keys(Keys.BACKSPACE)
    #     assert field_fact_data == str(params['INPUT']).strip(), 'Пробелы не удаляются'


@allure.feature('Проверки валидации поля Стоимость консультации ')
class TestPriceField:
    @allure.story('Позитивные проверки валидации поля Стоимость консультации по величине')
    @pytest.mark.parametrize('params',
                            dtp.PRICE_FLD_LEN[0],
                            ids=dtp.PRICE_FLD_LEN[1])
    def test_doc_price_len_possit(self, login_doctor, params):
        """Позитивные проверки валидации поля Стоимость консультации по величине"""
        login_doctor.fill_the_field('PRICE_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('PRICE_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (f'текст в поле не соответствует вводимому, expected input: {params["INPUT"]}, '
                                                        f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_PRICE_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('PRICE_FLD_NM', 'NAME')
        assert err_mess == '', f'при вводе валидного числа появляется ошибка: "{err_mess}"'

    @allure.story('Негативные проверки валидации поля Стоимость консультации на ввод нуля')
    @pytest.mark.parametrize('params',
                             dtn.PRICE_FLD_ZERO[0],
                             ids=dtn.PRICE_FLD_ZERO[1])
    def test_doc_price_zero_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Стоимость консультации на ввод нуля"""
        login_doctor.fill_the_field('PRICE_FLD_NM', params['INPUT'], 'NAME')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH', 'XPATH')
        inserted = login_doctor.get_elem_obj_or_ex('PRICE_FLD_NM', 'NAME').get_attribute('value')
        login_doctor.clear_field('PRICE_FLD_NM', 'NAME')
        assert inserted == params['INPUT'], (f'введенный текст обрезается, expected input: {params["INPUT"]}, '
                                                      f'fact input: {inserted}')
        assert inserted == '', 'можно ввести нулевое значение'

    @allure.story('Негативные проверки валидации поля Стоимость консультации на ввод отрицат значения')
    @pytest.mark.parametrize('params',
                             dtn.PRICE_FLD_LESS_THEN_ZERO[0],
                             ids=dtn.PRICE_FLD_LESS_THEN_ZERO[1])
    def test_doc_price_less_zero_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Стоимость консультации на ввод отрицат значения"""
        login_doctor.fill_the_field('PRICE_FLD_NM', params['INPUT'], 'NAME')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH', 'XPATH')
        inserted = login_doctor.get_elem_obj_or_ex('PRICE_FLD_NM', 'NAME').get_attribute('value')
        login_doctor.clear_field('PRICE_FLD_NM', 'NAME')
        assert inserted == params['INPUT'].strip('-'), 'можно ввести отрицат значение'

    @allure.story('Негативные проверки валидации поля Стоимость консультации на ввод числа больше допустимого значения')
    @pytest.mark.parametrize('params',
                             dtn.PRICE_FLD_MAX_LEN[0],
                             ids=dtn.PRICE_FLD_MAX_LEN[1])
    def test_doc_price_max_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Стоимость консультации на ввод числа больше допустимого значения"""
        login_doctor.fill_the_field('PRICE_FLD_NM', params['INPUT'], 'NAME')
        inserted = login_doctor.get_elem_obj_or_ex('PRICE_FLD_NM', 'NAME').get_attribute('value')
        assert inserted == params['INPUT'], (
            f'текст в поле не соответствует вводимому, expected input: {params["INPUT"]}, '
            f'fact input: {inserted}')
        err_mess = str(
            login_doctor.get_elem_obj_or_ex('ER_MESS_PRICE_XPATH', 'XPATH').get_attribute('textContent'))
        login_doctor.clear_field('PRICE_FLD_NM', 'NAME')
        assert err_mess != '', 'При вводе невалидного числа ошибки не возникает '
        assert err_mess != '' and err_mess == 'Максимальная длина: 5 символов', \
            (f'Текст ошибки не соответствует требованиям. Expected: "Максимальная длина: 5 символов", fact:'
             f'"{err_mess}" ')

    @allure.story('Негативные проверки валидации поля Стоимость консультации на ввод НЕ цифр')
    @pytest.mark.parametrize('params',
                             dtn.PRICE_FLD_NOT_DGTS[0],
                             ids=dtn.PRICE_FLD_NOT_DGTS[1])
    def test_doc_price_not_dgts_negot(self, login_doctor, params):
        """Негативные проверки валидации поля Стоимость консультации на ввод НЕ цифр"""
        login_doctor.fill_the_field('PRICE_FLD_NM', params['INPUT'], 'NAME')
        login_doctor.click_element('LEFT_PAGE_AREA_XPATH', 'XPATH')
        allergen_inserted = login_doctor.get_elem_obj_or_ex('PRICE_FLD_NM', 'NAME').get_attribute('value')
        login_doctor.clear_field('PRICE_FLD_NM', 'NAME')
        assert allergen_inserted == '', 'можно ввести символы, отличные от цифр'


