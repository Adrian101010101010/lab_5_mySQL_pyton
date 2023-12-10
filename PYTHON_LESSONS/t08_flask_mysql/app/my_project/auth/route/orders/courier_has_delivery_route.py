"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import courier_has_delivery_controller
from t08_flask_mysql.app.my_project.auth.domain import CourierHasDelivery

courier_has_delivery_bp = Blueprint('courier_has_delivery', __name__, url_prefix='/courier_has_delivery')

@courier_has_delivery_bp.get('')
def get_all() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(courier_has_delivery_controller.find_all()), HTTPStatus.OK)

@courier_has_delivery_bp.post('')
def create_courier_has_delivery() -> Response:
    """
    Creates a new association between a courier and a delivery.
    :return: Response object
    """
    content = request.get_json()
    courier_has_delivery = CourierHasDelivery.create_from_dto(content)
    courier_has_delivery_controller.create(courier_has_delivery)
    return make_response(jsonify(courier_has_delivery.put_into_dto()), HTTPStatus.CREATED)

@courier_has_delivery_bp.get('/courier/<int:courier_id>')
def get_deliveries_by_courier(courier_id: int) -> Response:
    """
    Gets all deliveries associated with a specific courier.
    :return: Response object
    """
    return make_response(jsonify(courier_has_delivery_controller.find_deliveries_by_courier(courier_id)), HTTPStatus.OK)

@courier_has_delivery_bp.get('/delivery/<int:delivery_id>')
def get_couriers_by_delivery(delivery_id: int) -> Response:
    """
    Gets all couriers associated with a specific delivery.
    :return: Response object
    """
    return make_response(jsonify(courier_has_delivery_controller.find_couriers_by_delivery(delivery_id)), HTTPStatus.OK)

@courier_has_delivery_bp.delete('/courier/<int:courier_id>/delivery/<int:delivery_id>')
def delete_courier_has_delivery(courier_id: int, delivery_id: int) -> Response:
    """
    Deletes the association between a specific courier and delivery.
    :return: Response object
    """
    courier_has_delivery_controller.delete(courier_id, delivery_id)
    return make_response("Courier has delivery association deleted", HTTPStatus.OK)

@courier_has_delivery_bp.post('/insert_into_docking_table_courier_has_delivery')
def insert_into_docking_table_courier_has_delivery() -> Response:
    content = request.get_json()
    corier_name = content.get('corier_name')
    corier_phone = content.get('corier_phone')
    delivery_recipient = content.get('delivery_recipient')

    result = courier_has_delivery_controller.insert_into_docking_table_courier_has_delivery(corier_name, corier_phone, delivery_recipient)
    return make_response(jsonify({'message': result}), HTTPStatus.OK)
