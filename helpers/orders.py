import requests
from data import Requests


class OrderHelper:
    @staticmethod
    def get_token(email, password):
        response = requests.post(Requests.LOGIN, json={"email": email, "password": password})
        return response.json().get("accessToken")

    @staticmethod
    def create_order(token, ingredients):
        response = requests.post(
            Requests.ORDERS,
            headers={"Authorization": token},
            json={"ingredients": ingredients}
        )
        return response.json()

    @classmethod
    def create_order_with_login(cls, email, password, ingredients):
        token = cls.get_token(email, password)
        return cls.create_order(token, ingredients)
