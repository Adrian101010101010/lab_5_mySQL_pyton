"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import courier_controller
from t08_flask_mysql.app.my_project.auth.domain import Courier

courier_bp = Blueprint('couriers', __name__, url_prefix='/couriers')

@courier_bp.get('')
def get_all_couriers() -> Response:
    """
    Gets all courier objects using the Courier Controller.
    :return: Response object
    """
    return make_response(jsonify(courier_controller.find_all()), HTTPStatus.OK)

@courier_bp.post('')
def create_courier() -> Response:
    """
    Creates a new courier.
    :return: Response object
    """
    content = request.get_json()
    courier = Courier.create_from_dto(content)
    courier_controller.create(courier)
    return make_response(jsonify(courier.put_into_dto()), HTTPStatus.CREATED)

@courier_bp.get('/<int:courier_id>')
def get_courier(courier_id: int) -> Response:
    """
    Gets a courier by ID.
    :return: Response object
    """
    return make_response(jsonify(courier_controller.find_by_id(courier_id)), HTTPStatus.OK)

@courier_bp.put('/<int:courier_id>')
def update_courier(courier_id: int) -> Response:
    """
    Updates a courier by ID.
    :return: Response object
    """
    content = request.get_json()
    courier = Courier.create_from_dto(content)
    courier_controller.update(courier_id, courier)
    return make_response("Courier updated", HTTPStatus.OK)

@courier_bp.patch('/<int:courier_id>')
def patch_courier(courier_id: int) -> Response:
    """
    Patches a courier by ID.
    :return: Response object
    """
    content = request.get_json()
    courier_controller.patch(courier_id, content)
    return make_response("Courier updated", HTTPStatus.OK)

@courier_bp.delete('/<int:courier_id>')
def delete_courier(courier_id: int) -> Response:
    """
    Deletes a courier by ID.
    :return: Response object
    """
    courier_controller.delete(courier_id)
    return make_response("Courier deleted", HTTPStatus.OK)


@courier_bp.post('/data_insertion')
def data_insertion() -> Response:
    content = request.get_json()
    courier = content.get('courier')
    name = content.get('name')
    surname = content.get('surname')
    phone = content.get('phone')
    birthday = content.get('birthday')

    result = courier_controller.data_insertion(courier, name, surname, phone, birthday)
    return make_response(jsonify(result), HTTPStatus.OK)
