# Данные для позитивных проверок валидации полей

# Данные для полей Имя и Фамилия

ALLNAME_FLD_LEN_POSSITIVE = (
                        [
                            {'INPUT': 'ива'},
                            {'INPUT': 'ив'},
                            {'INPUT': 'ИвановскийИвановскийИвановскийИвановскийИвановски'},
                            {'INPUT': 'ИвановскийИвановскийИвановскийИвановскийИвановский'}
                        ],
                        [
                            '3 letters',
                            '2 letters',
                            '49 letters',
                            '50 letters',
                        ]
                       )
ALLNAME_FLD_SYMB_POSSITIVE = (
                        [
                            {'INPUT': 'Иванов'},
                            {'INPUT': 'Ivanov'},
                            {'INPUT': 'Иванов-Петров'},
                            {'INPUT': 'Ivanov-petrov'},
                            {'INPUT': 'Иванов Петров'},
                            {'INPUT': 'Ivanov Petrov'}],
                        [
                            'russian symbols',
                            'eng symbols',
                            'russian symbol and -',
                            'eng symbols and -',
                            'russian symbol and space',
                            'eng symbols and space'
                         ]
                        )
ALLNAME_FLD_SPACE_DELETE = (
                        [
                            {'INPUT': '  Иванов'},
                            {'INPUT': 'Иванов  '}
                        ],
                        [
                            'with left space',
                            'with right space'
                         ],
                        )

ALLNAME_FLD_TEXT_REGISTR = (
                        [
                            {'INPUT': 'ИвAнOв'}
                        ],
                        [
                            'wright textregistr field save'
                         ],
                        )

# Данные для поля Дата рождения
DBIRTH_FLD_POSSITIVE = (
                        [
                            {'INPUT': '26/02/1981'},
                            {'INPUT': '30/01/1985'},
                            {'INPUT': '28/02/1981'},
                            {'INPUT': '31/03/1981'},
                            {'INPUT': '30/06/1981'},
                            {'INPUT': '31/08/1999'},
                            {'INPUT': '30/11/1977'}
                        ],
                        [
                            'Valid date of birth',
                            'Last valid day in january',
                            'Last valid day in fabruary',
                            'Last valid day in march',
                            'Last valid day in june',
                            'Last valid day in august',
                            'Last valid day in november',
                         ]
                        )

# Данные для поля E-mail
EMAIL_FLD_LEN = (
                        [
                            {'INPUT': 'i@f.ru'},
                            {'INPUT': 'i@fo.ru'},
                            {'INPUT': 'ivanofffffivanofffffivanofffffivanofffffivanofffffivanofffff@info.com'},
                            {'INPUT': 'ivanofffffivanofffffivanofffffivanofffffivanofffffivanofffff@infoo.com'},
                            {'INPUT': 'ivanofffffivanofffff@infoo.com'}
                        ],
                        [
                            '6 symbols',
                            '7 symbols',
                            '69 symbols',
                            '70 symbols',
                            '30 symbols'
                         ]
                        )

EMAIL_FLD_SYMB = (
                        [
                            {'INPUT': 'eng@domain.ru'},
                            {'INPUT': '1234@domain.ru'},
                            {'INPUT': '12-34@domain.ru'},
                            {'INPUT': '12_34@domain.ru'}
                        ],
                        [
                            'eng symbols as username in email',
                            'digits as username in email',
                            'dash (-) in email',
                            'underlining (_) in email'
                         ]
                        )

EMAIL_FLD_SPACE_DELETE = (
                        [
                            {'INPUT': '  mail@mail.ru'},
                            {'INPUT': 'mail@mail.ru  '}
                        ],
                        [
                            'with left space',
                            'with right space'
                         ],
                        )

# Данные для поля "Учебное заведение"
EDU_INSTIT_FLD_LEN = (
                        [
                            {'INPUT': 'ин'},
                            {'INPUT': 'инс'},
                            {'INPUT': 'УниверситеУниверситеУниверситеУниверситеУниверситеУниверситеУниверситеУниверсите'
                                      'УниверситеУниверситеУниверситеУниверситеУниверситеУниверситеУниверсит'},
                            {'INPUT': 'УниверситеУниверситеУниверситеУниверситеУниверситеУниверситеУниверситеУниверсите'
                                      'УниверситеУниверситеУниверситеУниверситеУниверситеУниверситеУниверсите'},
                            {'INPUT': 'УниверситеУниверситеУниверситеУниверситеУниверсите'}
                        ],
                        [
                            '2 symbols',
                            '3 symbols',
                            '149 symbols',
                            '150 symbols',
                            '50 symbols'
                         ]
                        )

EDU_INSTIT_FLD_SYMB = (
                        [
                            {'INPUT': '12345'},
                            {'INPUT': 'Abcd'},
                            {'INPUT': 'Абвг'},
                            {'INPUT': '()№""'},
                            {'INPUT': 'с пробелом'},
                            {'INPUT': 'с-дефисом'}
                        ],
                        [
                            'digits',
                            'eng letters',
                            'rus letters',
                            'spec symbols',
                            'letters with space',
                            'letters with dash'
                         ],
                        )