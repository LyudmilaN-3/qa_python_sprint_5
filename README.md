# Автотесты для сервиса Stellar Burgers

## UI-тестирование через Selenium WebDriver

### Реализованы тесты по функциональности:

#### Регистрация в файле _test_registration.py:_
`test_registration_success`

`test_registration_not_valid_len_password_error`

#### Вход в аккаунт в файле _test_entry_in_acc.py:_
`test_entry_in_acc_by_button_on_main_page_entry_success`

`test_entry_in_acc_by_button_on_header_entry_success`

`test_entry_in_acc_by_button_on_reg_page_success`

`test_entry_in_acc_by_button_on_recov_pass_page_success`

#### Переходы в файле _test_moving.py:_

##### - в личный кабинет
`test_moving_in_acc_by_button_on_header_success`

##### - из личного кабинета в конструктор
`test_moving_on_main_page_by_button_on_header_success`

`test_moving_on_main_page_by_logo_on_header_success`

#### Выход из аккаунта в файле _test_log_out.py:_
`test_log_out_by_button_on_acc_page_success`

#### Переходы по разделам в конструкторе в файле _test_constr_move_div.py:_
`test_moving_to_buns_by_label_in_constr_success`

`test_moving_to_fillings_by_label_in_constr_success`

`test_moving_to_sauces_by_label_in_constr_success`

### Тесты можно запустить из терминала командой:

`pytest`
#   q a _ p y t h o n _ s p r i n t _ 5  
 