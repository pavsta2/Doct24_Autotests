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
                            'Unvalid date in january',
                            'Unvalid date in april',
                            'Unvalid date in july',
                            'Unvalid 13th mounth',
                            'Unvalid year less than 1930',
                            'Unvalid date from future'
                         ]
                        )

# Данные для поля E-mail
EMAIL_FLD_LEN = (
                        [
                            {'INPUT': 'i@f.r'},
                            {'INPUT': 'ivanofffffivanofffffivanofffffivanofffffivanofffffivanofffffi@infoo.com'},
                            {'INPUT': 'ivanofffffivanofffffivanofffffivanofffffivanofffffivanofffffivanofffff@infoo.com'}
                        ],
                        [
                            '5 symbols',
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

# Данные для поля Рост
HEIGHT_FLD_LEN = (
                        [
                            {'INPUT': '1991'}
                        ],
                        [
                            '4 symbols'
                         ],
                        )

HEIGHT_FLD_SYMB = (
                        [
                            {'INPUT': 'not-digits'}
                        ],
                        [
                            'not didgits as height'
                         ],
                        )

# Данные для поля Вес
WEIGHT_FLD_LEN = (
                        [
                            {'INPUT': '1234'}
                        ],
                        [
                            '4 symbols'
                         ],
                        )

WEIGHT_FLD_SYMB = (
                        [
                            {'INPUT': 'not-digits'}
                        ],
                        [
                            'not didgits as weight'
                         ],
                        )

# Данные для поля Аллерген
ALLERGEN_FLD_MIN_LEN = (
                        [
                            {'INPUT': '1'}
                        ],
                        [
                            '1 symbol'
                         ],
                        )

ALLERGEN_FLD_MAX_LEN = (
                        [
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert1'},
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'}
                        ],
                        [
                            '51 symbols',
                            '60 symbols'
                         ],
                        )

# Данные для поля Реакция
REACTION_FLD_MIN_LEN = (
                        [
                            {'INPUT': '1'}

                        ],
                        [
                            '1 symbol'
                         ],
                        )

REACTION_FLD_MAX_LEN = (
                        [
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwert1'},
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'}
                        ],
                        [
                            '201 symbols',
                            '240 symbols'
                         ],
                        )

# Данные для поля Операция
SURGERIES_FLD_MIN_LEN = (
                        [
                            {'INPUT': '1'}

                        ],
                        [
                            '1 symbol'
                         ],
                        )

SURGERIES_FLD_MAX_LEN = (
                        [
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwert1'},
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'}
                        ],
                        [
                            '201 symbols',
                            '240 symbols'
                         ],
                        )

# Данные для поля Год операции
SURGERIE_YEAR_LEN_LESS_THEN_FOUR_DGT_FLD = (
                        [
                            {'INPUT': '1'},
                            {'INPUT': '19'},
                            {'INPUT': '202'}
                        ],
                        [
                            'One digit',
                            'Two digits',
                            'Three digits'
                         ],
                        )

SURGERIE_YEAR_LEN_MORE_THEN_FOUR_DGT_FLD = (
                        [
                            {'INPUT': '19823'}
                        ],
                        [
                            'Five digit'
                         ],
                        )

SURGERIE_YEAR_FLD_CANT_INPUT = (
                        [
                            {'INPUT': 'engl'},
                            {'INPUT': 'русс'},
                            {'INPUT': '-.,:'},
                            {'INPUT': '    '}
                        ],
                        [
                            'english letters',
                            'russian letters',
                            'service symbols',
                            'spaces'
                         ],
                        )

# Данные для поля Препарат
MEDICATION_FLD_MIN_LEN = (
                        [
                            {'INPUT': '1'}

                        ],
                        [
                            '1 symbol'
                         ],
                        )

MEDICATION_FLD_MAX_LEN = (
                        [
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345'
                                      'qwert12345qwert12345qwert1'},
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'}
                        ],
                        [
                            '101 symbols',
                            '240 symbols'
                         ],
                        )

# Данные для поля Дозировка
DASAGE_FLD_MIN_LEN = (
                        [
                            {'INPUT': '1'}

                        ],
                        [
                            '1 symbol'
                         ],
                        )

DOSAGE_FLD_MAX_LEN = (
                        [
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345'
                                      'qwert12345qwert12345qwert1'},
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'}
                        ],
                        [
                            '101 symbols',
                            '240 symbols'
                         ],
                        )

# Данные для поля Периодичность приема
FREQ_OF_TKNG_FLD_MIN_LEN = (
                        [
                            {'INPUT': '1'}

                        ],
                        [
                            '1 symbol'
                         ],
                        )

FREQ_OF_TKNG_FLD_MAX_LEN = (
                        [
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345'
                                      'qwert12345qwert12345qwert1'},
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'}
                        ],
                        [
                            '101 symbols',
                            '240 symbols'
                         ],
                        )

# Данные для поля Хронические заболевания
CHRON_DES_FLD_MIN_LEN = (
                        [
                            {'INPUT': '1'}

                        ],
                        [
                            '1 symbol'
                         ],
                        )

CHRON_DES_FLD_MAX_LEN = (
                        [
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345'
                                      'qwert12345qwert12345qwert1'},
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'}
                        ],
                        [
                            '101 symbols',
                            '240 symbols'
                         ],
                        )

# Данные для поля Год обнаружения
CHRON_DISC_YEAR_LEN_LESS_THEN_FOUR_DGT_FLD = (
                        [
                            {'INPUT': '1'},
                            {'INPUT': '19'},
                            {'INPUT': '202'}
                        ],
                        [
                            'One digit',
                            'Two digits',
                            'Three digits'
                         ],
                        )

CHRON_DISC_YEAR_LEN_MORE_THEN_FOUR_DGT_FLD = (
                        [
                            {'INPUT': '19823'}
                        ],
                        [
                            'Five digit'
                         ],
                        )

CHRON_DISC_YEAR_FLD_CANT_INPUT = (
                        [
                            {'INPUT': 'engl'},
                            {'INPUT': 'русс'},
                            {'INPUT': '-.,:'},
                            {'INPUT': '    '}
                        ],
                        [
                            'english letters',
                            'русские буквы',
                            'service symbols',
                            'spaces'
                         ],
                        )