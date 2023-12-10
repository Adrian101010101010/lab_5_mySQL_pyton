"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import parcel_controller
from t08_flask_mysql.app.my_project.auth.domain import Parcel

parcel_bp = Blueprint('parcels', __name__, url_prefix='/parcels')

@parcel_bp.get('')
def get_all_parcels() -> Response:
    """
    Gets all parcel objects using the Parcel Controller.
    :return: Response object
    """
    return make_response(jsonify(parcel_controller.find_all()), HTTPStatus.OK)

@parcel_bp.post('')
def create_parcel() -> Response:
    """
    Creates a new parcel.
    :return: Response object
    """
    content = request.get_json()
    parcel = Parcel.create_from_dto(content)
    parcel_controller.create(parcel)
    return make_response(jsonify(parcel.put_into_dto()), HTTPStatus.CREATED)

@parcel_bp.get('/<int:parcel_id>')
def get_parcel(parcel_id: int) -> Response:
    """
    Gets a parcel by ID.
    :return: Response object
    """
    return make_response(jsonify(parcel_controller.find_by_id(parcel_id)), HTTPStatus.OK)

@parcel_bp.put('/<int:parcel_id>')
def update_parcel(parcel_id: int) -> Response:
    """
    Updates a parcel by ID.
    :return: Response object
    """
    content = request.get_json()
    parcel = Parcel.create_from_dto(content)
    parcel_controller.update(parcel_id, parcel)
    return make_response("Parcel updated", HTTPStatus.OK)

@parcel_bp.patch('/<int:parcel_id>')
def patch_parcel(parcel_id: int) -> Response:
    """
    Patches a parcel by ID.
    :return: Response object
    """
    content = request.get_json()
    parcel_controller.patch(parcel_id, content)
    return make_response("Parcel updated", HTTPStatus.OK)

@parcel_bp.delete('/<int:parcel_id>')
def delete_parcel(parcel_id: int) -> Response:
    """
    Deletes a parcel by ID.
    :return: Response object
    """
    parcel_controller.delete(parcel_id)
    return make_response("Parcel deleted", HTTPStatus.OK)