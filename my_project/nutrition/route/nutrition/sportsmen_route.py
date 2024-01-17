from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.nutrition.controller import sportsmen_controller

sportsmen_bp = Blueprint('sportsmen', __name__, url_prefix='/sportsmen')


@sportsmen_bp.get('/<int:sportsmen_id>')
def get_sportsmen(sportsmen_id: int) -> Response:
    return make_response(jsonify(sportsmen_controller.find_by_id(sportsmen_id)), HTTPStatus.OK)


@sportsmen_bp.get('')
def get_all_sportsmen() -> Response:
    return make_response(jsonify(sportsmen_controller.find_all()), HTTPStatus.OK)


@sportsmen_bp.post('')
def create_sportsmen() -> Response:
    content = request.get_json()
    obj = sportsmen_controller.create(content)
    return make_response(jsonify(obj), HTTPStatus.CREATED)


@sportsmen_bp.put('/<int:sportsmen_id>')
def update_sportsmen(sportsmen_id: int) -> Response:
    content = request.get_json()
    obj = sportsmen_controller.update(sportsmen_id, content)
    return make_response(jsonify(obj), HTTPStatus.OK)


@sportsmen_bp.patch('/<int:sportsmen_id>')
def patch_sportsmen(sportsmen_id: int) -> Response:
    content = request.get_json()
    obj = sportsmen_controller.patch(sportsmen_id, content)
    return make_response(jsonify(obj), HTTPStatus.OK)


@sportsmen_bp.delete('/<int:sportsmen_id>')
def delete_sportsmen(sportsmen_id: int) -> Response:
    sportsmen_controller.delete(sportsmen_id)
    return make_response("Sportsmen deleted", HTTPStatus.OK)
