from models import Result
from flask import Flask, jsonify


def serialize(data):
    if data is None:
        return None
    if isinstance(data, (list, dict)):
        return data
    if hasattr(data, '__dict__'):
        return data.__dict__
    if isinstance(data, (int, float, str, bool)):
        return data
    return None


class JsonFlask(Flask):
    def make_response(self, response):
        response = serialize(response)
        if response is None or isinstance(response, (list, dict)):
            response = Result.success(response)

        if isinstance(response, Result):
            response = jsonify(response.to_dict())

        return super().make_response(response)
