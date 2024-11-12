# Ултанбаева Светлана, 23-я когорта — Финальный проект. Инженер по тестированию плюс

import requests
import configuration
import data

# запрос на создание нового заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json = data.order_body)

# запрос на получение номера отслеживания
def get_order_details(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_DETAILS,
                         params={"t": track_number})