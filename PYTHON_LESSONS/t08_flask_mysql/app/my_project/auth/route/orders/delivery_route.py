"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import delivery_controller
from t08_flask_mysql.app.my_project.auth.domain import Delivery

delivery_bp = Blueprint('deliveries', __name__, url_prefix='/deliveries')

@delivery_bp.get('')
def get_all_deliveries() -> Response:
    """
    Gets all delivery objects using the Delivery Controller.
    :return: Response object
    """
    return make_response(jsonify(delivery_controller.find_all()), HTTPStatus.OK)

@delivery_bp.post('')
def create_delivery() -> Response:
    """
    Creates a new delivery.
    :return: Response object
    """
    content = request.get_json()
    delivery = Delivery.create_from_dto(content)
    delivery_controller.create(delivery)
    return make_response(jsonify(delivery.put_into_dto()), HTTPStatus.CREATED)

@delivery_bp.get('/<int:delivery_id>')
def get_delivery(delivery_id: int) -> Response:
    """
    Gets a delivery by ID.
    :return: Response object
    """
    return make_response(jsonify(delivery_controller.find_by_id(delivery_id)), HTTPStatus.OK)

@delivery_bp.put('/<int:delivery_id>')
def update_delivery(delivery_id: int) -> Response:
    """
    Updates a delivery by ID.
    :return: Response object
    """
    content = request.get_json()
    delivery = Delivery.create_from_dto(content)
    delivery_controller.update(delivery_id, delivery)
    return make_response("Delivery updated", HTTPStatus.OK)

@delivery_bp.patch('/<int:delivery_id>')
def patch_delivery(delivery_id: int) -> Response:
    """
    Patches a delivery by ID.
    :return: Response object
    """
    content = request.get_json()
    delivery_controller.patch(delivery_id, content)
    return make_response("Delivery updated", HTTPStatus.OK)

@delivery_bp.delete('/<int:delivery_id>')
def delete_delivery(delivery_id: int) -> Response:
    """
    Deletes a delivery by ID.
    :return: Response object
    """
    delivery_controller.delete(delivery_id)
    return make_response("Delivery deleted", HTTPStatus.OK)

@delivery_bp.get('/callGetMaxCargo')
def callGetMaxCargo() -> Response:
    result = delivery_controller.callGetMaxCargo()
    return make_response(jsonify(result), HTTPStatus.OK)
