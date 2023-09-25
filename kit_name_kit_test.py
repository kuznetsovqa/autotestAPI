#связываю с файлами
import sender_stand_requests
import data

#Функция на создание пользователя и вытаскивание токена
def get_new_user_token():
    response = sender_stand_requests.post_new_user(data.user_body)
    return response.json()["authToken"]


#Функция на изменение тела запроса
def get_kit_body(name):
    current_body = data.kit_body.copy()
    #Меняем значение в поле name
    current_body["name"] = name
    return current_body

#Функция для позитивной проверки
def positive_assert(name):
    kit_body = get_kit_body(name)
    response = sender_stand_requests.post_new_user_kit(kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == name

#Функция для негативнаой проверки
def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    response = sender_stand_requests.post_new_user_kit(kit_body)
    assert response.status_code == 400

data.headers["Authorization"]= f"Bearer {get_new_user_token()}"

# Тест 1 количество символов, name состоит из 1 символа
def test_1_symbol_in_name_positive():
    positive_assert("a")

# Тест 2 количество символов меньше допустимого 511
def test_511_symbols_in_name_positive():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3 количество символов меньше допустимого пустое , ошибка приходит 201 код
def test_0_symbols_in_name_negative():
    negative_assert_code_400("")

# Тест 4  количество символов больше допустимого 512 , ошибка приходит 201 код
def test_512_symbols_in_name_negative():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 5 Разрешены английские буквы
def test_english_letter_in_name_positive():
    positive_assert("QWErty")

#Тест 6 Разрашены русские буквы
def test_russian_letter_in_name_positive():
    positive_assert("Мария")

#Тест 7 Разрашены спец.символы
def test_specsymbol_in_name_positive():
    positive_assert("\"№%@\",")

#Тест 8 Разрашены пробелы
def test_probely_in_name_positive():
    positive_assert("Человек и КО")

#Тест 9 Разрешены цифры
def test_cyfry_in_name_positive():
    positive_assert("123")

#Тест 10 Параметр не передан в запросе , ошибка, приходит 201 код создается,вместо 400
def test_parametr_ne_peredan_negative():
    #Копирую словарь
    body = data.kit_body.copy()
    # Удаляю параметр из name с помощью функции pop, другого варианта и не представляю...
    body.pop("name")
    response = sender_stand_requests.post_new_user_kit(body)
    assert response.status_code == 400

#Тест 11 Передаем другой тип параметра, ошибка приходит 201 год, вместо 400.
def test_drugoi_tip_parametra_negative():
    negative_assert_code_400(123)





