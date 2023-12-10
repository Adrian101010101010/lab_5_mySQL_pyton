from flask import Blueprint, jsonify, request

from t08_flask_mysql.app.my_project.auth.controller import post_office_controller
from t08_flask_mysql.app.my_project.auth.domain import PostOffice

post_office_bp = Blueprint('post_offices', __name__, url_prefix='/post_offices')

@post_office_bp.get('')
def get_all_post_offices():
    post_offices = post_office_controller.find_all()
    return jsonify([post_office.put_into_dto() for post_office in post_offices])

@post_office_bp.post('')
def create_post_office():
    content = request.get_json()
    post_office = Post_office.create_from_dto(content)
    post_office_controller.create(post_office)
    return jsonify(post_office.put_into_dto()), 201

@post_office_bp.get('/<int:post_office_id>')
def get_post_office(post_office_id):
    post_office = post_office_controller.find_by_id(post_office_id)
    return jsonify(post_office.put_into_dto()) if post_office else '', 404

@post_office_bp.put('/<int:post_office_id>')
def update_post_office(post_office_id):
    content = request.get_json()
    post_office = Post_office.create_from_dto(content)
    post_office_controller.update(post_office_id, post_office)
    return 'Post office updated', 200

@post_office_bp.patch('/<int:post_office_id>')
def patch_post_office(post_office_id):
    content = request.get_json()
    post_office_controller.patch(post_office_id, content)
    return 'Post office updated', 200

@post_office_bp.delete('/<int:post_office_id>')
def delete_post_office(post_office_id):
    post_office_controller.delete(post_office_id)
    return 'Post office deleted', 200
