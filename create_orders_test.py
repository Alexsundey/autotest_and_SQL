import requests

import config
import data


def create_courers():
    return requests.post(config.URL + config.CREATE_COURIER, json=data.courers_body)


def login_courers():
    return requests.post(config.URL + config.LOGIN_COURERS, json=data.login_body)


def create_orders():
    return requests.post(config.URL + config.CREATE_ORDERS, json=data.orders_body)


response_create_orders = create_orders()

def save_track():
    track_number = create_orders().json()['track']
    return track_number


def get_orders():
    return requests.get(config.URL + config.GET_ORDERS + "track_number")
