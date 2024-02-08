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


    # чекбоксы
    # чекбокс выбора категории пользователя - врач
    'DOCTOR_CHK_BX_SEL': '#root > div > div > div > div > div > label:nth-child(3) > img',
    # чекбокс принятия соглашения
    'AGRMT_CHK_BX_ID': 'agreement',
    'AGRMT_CHK_BX_XPATH': '//*[@id="agreement"]',

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
    # поле ввода учебного заведения врача
    'UDU_INSTIT_FLD_NM': 'higher_education.0.university',


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


    # прочие элементы
    # задний блок на странице профиля (для клика, что снять фокус с полей)
    'BLOCK_PRFL_SEL': 'rightBlock',
    # нейтральная область страницы (для клика, чтоб снять фокус)
    'LEFT_PAGE_AREA_XPATH': '//*[@id="root"]/section/div/div[2]/nav',
}