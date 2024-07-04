# Размечаем элементы страницы:
locators = {
    # кнопки
    # кнопка авторизации
    'LOGIN_BTN_CLS': 'header__signin-link',
    'LOGIN_BTN_XPATH': '//*[@id="root"]/header/div/div/a',
    # кнопки далее(при авторизации)
    "NXT_BTN_CLS": 'btn',
    'NXT_BTN_XPATH1': '//*[@id="root"]/div/div/div/div/form/button',
    'NXT_BTN_XPATH2': '/html/body/div[1]/div/div/div/div/form/div[3]/button',
    'NXT_BTN_XPATH3': '//*[@id="root"]/div/div/div/div/form/button',
    'NXT_BTN_XPATH4': '//*[@id="root"]/div/div/div/div/form/div[3]/button',
    # кнопка входя в личный кабинет
    'PROFL_BTN_XP': '//*[@id="root"]/header/div/div/a/img',
    # х-кнопка поля Организация (опыт работы врача)
    'JOB_ORG_X_BTN_SEL': '#root > section > div > div.content > div > div > div.data > div > form > div:nth-child(4)'
                           ' > div > label:nth-child(1) > svg',
    # х-кнопка поля Должность (опыт работы врача)
    'POSITION_X_BTN_SEL': '#root > section > div > div.content > div > div > div.data > div > form > div:nth-child(4)'
                          ' > div > label:nth-child(2) > svg',

    # чекбоксы
    # чекбокс выбора категории пользователя - врач
    'DOCTOR_CHK_BX_XP': '//*[@id="root"]/div/div/div/div/div/label[2]/div',
    # чекбокс принятия соглашения
    'AGRMT_CHK_BX_ID': 'agreement',
    'AGRMT_CHK_BX_XPATH': '//*[@id="agreement"]',

    # поля ввода
    # поле ввода адреса эл почты при авторизации
    "AUTH_EMAIL_FLD_ID": "email",
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
    'LNAME_NM': 'user.last_name',
    # поле ввода имени
    'FNAME_XP': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[1]/label[2]/input',
    # поле ввода отчества
    'PATRONYMIC_XP': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[1]/label[3]/input',
    # поле ввода email
    'EMAIL_FLD_NM': 'user.email',
    # поле ввода даты рождения
    'DBIRTH_FLD_NM': 'user.birthday',
    # поле ввода учебного заведения врача
    'UDU_INSTIT_FLD_NM': 'higher_education.0.university',
    # поле ввода Специализации врача
    'SPECIAL_FLD_NM': 'higher_education.0.specialization',
    # поле ввода Года окончания (образования врача)
    'END_OF_EDUCATION_FLD_NM': 'higher_education.0.end_date',
    # поле ввода Организация (повышения квалификации врача)
    'QUAL_ORGANIZATION_FLD_NM': 'advanced_training.0.organization',
    # поле ввода "Название программы"
    'PROG_NAME_FLD_NM': 'advanced_training.0.position',
    # поле ввода Год окончания (повыш квалификации)
    'END_OF_QUAL_FLD_NM': 'advanced_training.0.end_date',
    # поле ввода Орагнизации (опыт работы врача)
    'JOB_ORG_FLD_NM': 'work.0.organization',
    # поле ввода Должности (опыт работы врача)
    'POSITION_FLD_NM': 'work.0.position',
    # поле ввода даты начала работы врача в должности
    'JOB_START_DATE_FLD_NM': 'work.0.start_date',
    # поле ввода даты окончания работы врача в должности
    'JOB_END_DATE_FLD_NM': 'work.0.end_date',
    # поле ввода инфо о диагностике и лечении
    # 'DIAGNOSTC_FLD_XP': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[6]/div/div[2]/div[1]',
    'DIAGNOSTC_FLD_XP': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[6]/div/div[2]/div[1]/p',
    'DIAGNOSTC_FLD_CSS': '.ql-editor p',
    'DIAGNOSTC_FLD_SEL': '#root > section > div > div.content > div > div > div.data > div > form > div:nth-child(6) '
                          '> div > div.ql-container.ql-snow > div.ql-editor > p',
    # поле ввода Стоимости консультации врача
    'PRICE_FLD_NM': 'price.price',

    # сообщения об ошибках
    # сообщение об ошибке валидации поля фамилия
    'ER_MESS_LNAME_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[1]/label[1]/p',
    # сообщение об ошибке валидации поля имя
    'ER_MESS_FNAME_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[1]/label[2]/p',
    # сообщение об ошибке валидации поля отчество
    'ER_MESS_PATRON_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[1]/label[3]/p',
    # сообщение об ошибке валидации поля Дата рождения
    'ER_MESS_DBIRTH_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[1]/div[1]/label/p',
    # сообщение об ошибке валидации поля Email
    'ER_MESS_EMAIL_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[1]/label[5]/p',
    # сообщение об ошибке валидации поля Учебное заведение
    'ER_MESS_EDU_INSTIT_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[2]/div/label[1]/p',
    # сообщение об ошибке валидации поля Специальность (врача)
    'ER_MESS_SPECIAL_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[2]/div/label[2]/p',
    # сообщение об ошибке валидации поля Год окончания (образования врача)
    'ER_MESS_END_OF_EDUCATION_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[2]/div/div/label/p',
    # сообщение об ошибке валидации поля Организация (повышения квалификации врача)
    'ER_MESS_QUAL_ORGANIZ_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[3]/div/label[1]/p',
    # сообщение об ошибке валидации поля "Название программы"
    'ER_MESS_PROG_NAME_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[3]/div/label[2]/p',
    # сообщение об ошибке поля "Год окончания" (повыш квалификации)
    'ER_MESS_END_OF_QUAL_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[3]/div/div[1]/label/p',
    # сообщение об ошибке валидации поля Организация (опыт работы врача)
    'ER_MESS_JOB_ORG_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[4]/div/label[1]/p',
    # сообщение об ошибке валидации поля Должность (опыт работы врача)
    'ER_MESS_POSITION_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[4]/div/label[2]/p',
    # сообщение об ошибке валидации поля "Период работы С"
    'ER_MESS_JOB_START_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[4]/div/div[1]/div[1]/label/p',
    # сообщение об ошибке валидации поля "Период работы ПО"
    'ER_MESS_JOB_END_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[4]/div/div[1]/div[2]/label/p',
    # сообщение об ошибке валидации поля "Стомиость консультации"
    'ER_MESS_PRICE_XPATH': '//*[@id="root"]/section/div/div[2]/div/div/div[2]/div/form/div[7]/div/label/p',

    # прочие элементы
    # нейтральная область страницы (для клика, чтоб снять фокус)
    'LEFT_PAGE_AREA_XPATH': '//*[@id="root"]/section/div/div[2]/nav'
}