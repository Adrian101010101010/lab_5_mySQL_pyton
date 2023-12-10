"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import city_controller
from t08_flask_mysql.app.my_project.auth.domain import City

city_bp = Blueprint('cities', __name__, url_prefix='/cities')

@city_bp.get('')
def get_all_cities() -> Response:
    """
    Gets all objects from the city table using the City Controller.
    :return: Response object
    """
    return make_response(jsonify(city_controller.find_all()), HTTPStatus.OK)

@city_bp.post('')
def create_city() -> Response:
    """
    Creates a new city.
    :return: Response object
    """
    content = request.get_json()
    city = City.create_from_dto(content)
    city_controller.create(city)
    return make_response(jsonify(city.put_into_dto()), HTTPStatus.CREATED)

@city_bp.get('/<int:city_id>')
def get_city(city_id: int) -> Response:
    """
    Gets a city by ID.
    :return: Response object
    """
    return make_response(jsonify(city_controller.find_by_id(city_id)), HTTPStatus.OK)

@city_bp.put('/<int:city_id>')
def update_city(city_id: int) -> Response:
    """
    Updates a city by ID.
    :return: Response object
    """
    content = request.get_json()
    city = City.create_from_dto(content)
    city_controller.update(city_id, city)
    return make_response("City updated", HTTPStatus.OK)

@city_bp.patch('/<int:city_id>')
def patch_city(city_id: int) -> Response:
    """
    Patches a city by ID.
    :return: Response object
    """
    content = request.get_json()
    city_controller.patch(city_id, content)
    return make_response("City updated", HTTPStatus.OK)

@city_bp.delete('/<int:city_id>')
def delete_city(city_id: int) -> Response:
    """
    Deletes a city by ID.
    :return: Response object
    """
    city_controller.delete(city_id)
    return make_response("City deleted", HTTPStatus.OK)

@city_bp.post('/insert_noname_records')
def insert_noname_records() -> Response:
    """
    Inserts 10 records in the format <Noname+№> into the City table using Service layer.
    :return: Response object
    """
    city_service = CityService()
    city_service.insert_noname_records()
    return make_response("Noname records inserted", 200)
