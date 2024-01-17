from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.nutrition.controller import day_controller

day_bp = Blueprint('day', __name__, url_prefix='/day')


@day_bp.get('/<int:day_id>')
def get_day(day_id: int) -> Response:
    return make_response(jsonify(day_controller.find_by_id(day_id)), HTTPStatus.OK)


@day_bp.get('')
def get_all_days() -> Response:
    return make_response(jsonify(day_controller.find_all()), HTTPStatus.OK)


@day_bp.post('')
def create_day() -> Response:
    content = request.get_json()
    obj = day_controller.create(content)
    return make_response(jsonify(obj), HTTPStatus.CREATED)


@day_bp.put('/<int:day_id>')
def update_day(day_id: int) -> Response:
    content = request.get_json()
    obj = day_controller.update(day_id, content)
    return make_response(jsonify(obj), HTTPStatus.OK)


@day_bp.patch('/<int:day_id>')
def patch_day(day_id: int) -> Response:
    content = request.get_json()
    obj = day_controller.patch(day_id, content)
    return make_response(jsonify(obj), HTTPStatus.OK)


@day_bp.delete('/<int:day_id>')
def delete_day(day_id: int) -> Response:
    day_controller.delete(day_id)
    return make_response("Day deleted", HTTPStatus.OK)
