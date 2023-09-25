#Хедер для создания пользователя
headers = {
    "Content-Type": "application/json",
    "Authorization":None
}
#Тело запроса для создания пользователя
user_body = {
    "firstName": "Анатолий",
    "phone": "+79995553322",
    "address": "г. Москва, ул. Пушкина, д. 10"
}
kit_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer a425eb14-d7cf-428e-8c11-8f84131a7eb9"
}
kit_body = {
    "name": "Мой"
}