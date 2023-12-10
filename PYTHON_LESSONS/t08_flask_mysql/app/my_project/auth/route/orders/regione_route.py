"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import regione_controller
from t08_flask_mysql.app.my_project.auth.domain import Regione

regione_bp = Blueprint('regiones', __name__, url_prefix='/regiones')

@regione_bp.get('')
def get_all_regiones() -> Response:
    """
    Gets all regione objects using the Regione Controller.
    :return: Response object
    """
    return make_response(jsonify(regione_controller.find_all()), HTTPStatus.OK)

@regione_bp.post('')
def create_regione() -> Response:
    """
    Creates a new regione.
    :return: Response object
    """
    content = request.get_json()
    regione = Regione.create_from_dto(content)
    regione_controller.create(regione)
    return make_response(jsonify(regione.put_into_dto()), HTTPStatus.CREATED)

@regione_bp.get('/<string:regione_name>')
def get_regione(regione_name: str) -> Response:
    """
    Gets a regione by name.
    :return: Response object
    """
    return make_response(jsonify(regione_controller.find_by_name(regione_name)), HTTPStatus.OK)

@regione_bp.put('/<string:regione_name>')
def update_regione(regione_name: str) -> Response:
    """
    Updates a regione by name.
    :return: Response object
    """
    content = request.get_json()
    regione = Regione.create_from_dto(content)
    regione_controller.update(regione_name, regione)
    return make_response("Regione updated", HTTPStatus.OK)

@regione_bp.patch('/<string:regione_name>')
def patch_regione(regione_name: str) -> Response:
    """
    Patches a regione by name.
    :return: Response object
    """
    content = request.get_json()
    regione_controller.patch(regione_name, content)
    return make_response("Regione updated", HTTPStatus.OK)

@regione_bp.delete('/<string:regione_name>')
def delete_regione(regione_name: str) -> Response:
    """
    Deletes a regione by name.
    :return: Response object
    """
    regione_controller.delete(regione_name)
    return make_response("Regione deleted", HTTPStatus.OK)