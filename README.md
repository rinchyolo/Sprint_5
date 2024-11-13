# Sprint_5
Реализованы автотесты для сервиса Stellar Burgers:
- Успешная регистрация (Тест test_registration_success)
- Неуспешная регистрация - отображение ошибки для некорректного пароля (Тест test_registration_wrong_password)
1) По кнопке "Личный кабинет" (Тест test_authorization_via_personal_account_and_main_button)
2) По кнопке "Войти в аккаунт" (Тест test_authorization_via_personal_account_and_main_button)
3) Вход через кнопку на форме регистрации (Тест test_authorization_via_registration_and_password_recovery)
4) Вход через кнопку на форме восстановление пароля (Тест test_authorization_via_registration_and_password_recovery)
- Переход в личный кабинет (Тест test_constructor_navigation_personal_account)
- Переход из личного кабинета в конструктор по тексту (Тест test_navigation_personal_account_navigation_constructor)
- Переход из личного кабинета в конструктор по логотипу Stellar Burgers (Тест test_navigation_personal_account_navigation_constructor)
- Выход из аккаунта (Тест test_logout_after_successful_login)
- Работа переходов к разделам "Булки", "Соусы", "Начинки" (Тест test_constructor_navigation_tabs)