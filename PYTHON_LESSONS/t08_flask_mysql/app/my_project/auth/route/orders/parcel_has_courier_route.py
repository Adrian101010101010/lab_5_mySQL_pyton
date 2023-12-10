"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import parcel_has_courier_controller
from t08_flask_mysql.app.my_project.auth.domain import ParcelHasCourier

parcel_has_courier_bp = Blueprint('parcel_has_courier', __name__, url_prefix='/parcel_has_courier')
@parcel_has_courier_bp.get('')
def get_all() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(parcel_has_courier_controller.find_all()), HTTPStatus.OK)

@parcel_has_courier_bp.post('')
def create_parcel_has_courier() -> Response:
    """
    Creates a new association between a parcel and a courier.
    :return: Response object
    """
    content = request.get_json()
    parcel_has_courier = ParcelHasCourier.create_from_dto(content)
    parcel_has_courier_controller.create(parcel_has_courier)
    return make_response(jsonify(parcel_has_courier.put_into_dto()), HTTPStatus.CREATED)

@parcel_has_courier_bp.get('/courier/<int:courier_id>')
def get_parcels_by_courier(courier_id: int) -> Response:
    """
    Gets all parcels associated with a specific courier.
    :return: Response object
    """

    return make_response(jsonify(parcel_has_courier_controller.find_parcels_by_courier(courier_id)), HTTPStatus.OK)

@parcel_has_courier_bp.get('/parcel/<int:parcel_id>')
def get_couriers_by_parcel(parcel_id: int) -> Response:
    """
    Gets all couriers associated with a specific parcel.
    :return: Response object
    """
    return make_response(jsonify(parcel_has_courier_controller.find_couriers_by_parcel(parcel_id)), HTTPStatus.OK)

@parcel_has_courier_bp.delete('/courier/<int:courier_id>/parcel/<int:parcel_id>')
def delete_parcel_has_courier(courier_id: int, parcel_id: int) -> Response:
    """
    Deletes the association between a specific courier and parcel.
    :return: Response object
    """
    parcel_has_courier_controller.delete(courier_id, parcel_id)
    return make_response("Parcel has courier association deleted", HTTPStatus.OK)