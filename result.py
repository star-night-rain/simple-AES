from flask import jsonify

from models import Result


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


def flask_response(result, response_type='success'):
    result = serialize(result)
    if result is None or isinstance(result, (list, dict)):
        if response_type == 'success':
            result = Result.success(result)
        else:
            result = Result.error(result)
    if isinstance(result, Result):
        result = jsonify(result.__dict__)

    return result
