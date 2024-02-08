# Данные для негативных проверок

# Данные для полей Имя и Фамилия
ALLNAME_FLD_MIN_LEN = (
                        [
                            {'INPUT': 's'}
                        ],
                        [
                            '1 letter'
                        ]
                       )

ALLNAME_FLD_MAX_LEN = (
                        [
                            {'INPUT': 'ИвановскийИвановскийИвановскийИвановскийИвановскийN'},
                            {'INPUT': 'ИвановскийИвановскийИвановскийИвановскийИвановскийИвановский'}
                        ],
                        [
                            '51 letters',
                            '60 letters'
                        ]
                       )

# Данные для поля Дата рождения
DBIRTH_FLD_UNVALID = (
                        [
                            {'INPUT': '32/01/1981'},
                            {'INPUT': '55/04/2010'},
                            {'INPUT': '32/07/2009'},
                            {'INPUT': '05/13/2010'},
                            {'INPUT': '05/10/1929'},
                            {'INPUT': '05/10/2030'}

                        ],
                        [
                            'Unvalid day in january',
                            'Unvalid day in april',
                            'Unvalid day in july',
                            'Unvalid 13th mounth',
                            'Unvalid year less than 1930',
                            'Unvalid date from future'
                         ]
                        )

# Данные для поля E-mail
EMAIL_FLD_MIN_LEN = (
                        [
                            {'INPUT': 'i@f.r'}
                        ],
                        [
                            '5 symbols'
                         ]
                        )

EMAIL_FLD_MAX_LEN = (
                        [
                            {'INPUT': 'ivanofffffivanofffffivanofffffivanofffffivanofffffivanofffffi@infoo.com'},
                            {'INPUT': 'ivanofffffivanofffffivanofffffivanofffffivanofffffivanofffffivanofffff@infoo.com'}
                        ],
                        [
                            '71 symbols',
                            '80 symbols'
                         ]
                        )

EMAIL_FLD_MASK = (
                        [
                            {'INPUT': 'ivanov@ivanov@mail.ru'},
                            {'INPUT': 'ivanov@mail.r'},
                            {'INPUT': '@mail.com'},
                            {'INPUT': 'ivanov.mail.ru'},
                            {'INPUT': 'ivanov@.ru'},
                            {'INPUT': 'ivanov@mail'}
                        ],
                        [
                            'two ats(@) in email',
                            'one symbol in domain of highest level',
                            'no username before at(@) in enail',
                            'no at(@) in email',
                            'no second level damain after at(@) in email',
                            'no domain of highest level in email'
                         ]
                        )

# Данные для поля Учебное заведение
EDU_INSTIT_FLD_MIN_LEN = (
                        [
                            {'INPUT': 'И'}
                        ],
                        [
                            '1 symbol'
                         ],
                        )

EDU_INSTIT_FLD_MAX_LEN = (
                        [
                            {'INPUT': 'УниверситеУниверситеУниверситеУниверситеУниверситеУниверситеУниверситеУниверсите'
                                      'УниверситеУниверситеУниверситеУниверситеУниверситеУниверситеУниверситет'},
                            {'INPUT': 'УниверситеУниверситеУниверситеУниверситеУниверситеУниверситеУниверситеУниверсите'
                                      'УниверситеУниверситеУниверситеУниверситеУниверситеУниверситеУниверсите'
                                      'Университе'},
                        ],
                        [
                            '151 symbols',
                            '160 symbols'
                         ],
                        )

EDU_INSTIT_FLD_SYMB = (
                        [
                            {'INPUT': ".,:;!?\|/{}[]'`#&$%@^*+_< >"}
                        ],
                        [
                            'spec symbols'
                         ],
                        )