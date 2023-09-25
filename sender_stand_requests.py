import config
import requests
import data

#Делаю тестовый GET запрос для получения документации, проверяю что сервер работает и отдаёт мне код 200






# POST Запрос на создание  нового пользователя (получил код 201)
def post_new_user(body):
    return requests.post(config.URL_SERVICE + config.CREATE_USER_PATH,
                        json = body,
                        headers=data.headers)
response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

# POST Запрос на создание набора "Мой" для этого пользователя
def post_new_user_kit(kit_body):
    return requests.post(config.URL_SERVICE + config.CREATE_NEW_KIT,
                         json=kit_body,
                         headers=data.headers)



