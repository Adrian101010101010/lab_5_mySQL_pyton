"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import department_controller
from t08_flask_mysql.app.my_project.auth.domain import Department

department_bp = Blueprint('departments', __name__, url_prefix='/departments')

@department_bp.get('')
def get_all_departments() -> Response:
    """
    Gets all department objects using the Department Controller.
    :return: Response object
    """
    return make_response(jsonify(department_controller.find_all()), HTTPStatus.OK)

@department_bp.post('')
def create_department() -> Response:
    """
    Creates a new department.
    :return: Response object
    """
    content = request.get_json()
    department = Department.create_from_dto(content)
    department_controller.create(department)
    return make_response(jsonify(department.put_into_dto()), HTTPStatus.CREATED)

@department_bp.get('/<int:department_id>')
def get_department(department_id: int) -> Response:
    """
    Gets a department by ID.
    :return: Response object
    """
    return make_response(jsonify(department_controller.find_by_id(department_id)), HTTPStatus.OK)

@department_bp.put('/<int:department_id>')
def update_department(department_id: int) -> Response:
    """
    Updates a department by ID.
    :return: Response object
    """
    content = request.get_json()
    department = Department.create_from_dto(content)
    department_controller.update(department_id, department)
    return make_response("Department updated", HTTPStatus.OK)

@department_bp.patch('/<int:department_id>')
def patch_department(department_id: int) -> Response:
    """
    Patches a department by ID.
    :return: Response object
    """
    content = request.get_json()
    department_controller.patch(department_id, content)
    return make_response("Department updated", HTTPStatus.OK)

@department_bp.delete('/<int:department_id>')
def delete_department(department_id: int) -> Response:
    """
    Deletes a department by ID.
    :return: Response object
    """
    department_controller.delete(department_id)
    return make_response("Department deleted", HTTPStatus.OK)