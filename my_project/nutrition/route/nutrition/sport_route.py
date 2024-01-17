from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.nutrition.controller import sport_controller

sport_bp = Blueprint('sport', __name__, url_prefix='/sport')


@sport_bp.get('/<int:sport_id>')
def get_sport(sport_id: int) -> Response:
    return make_response(jsonify(sport_controller.find_by_id(sport_id)), HTTPStatus.OK)


@sport_bp.get('')
def get_all_sports() -> Response:
    return make_response(jsonify(sport_controller.find_all()), HTTPStatus.OK)


@sport_bp.post('')
def create_sport() -> Response:
    content = request.get_json()
    obj = sport_controller.create(content)
    return make_response(jsonify(obj), HTTPStatus.CREATED)


@sport_bp.put('/<int:sport_id>')
def update_sport(sport_id: int) -> Response:
    content = request.get_json()
    obj = sport_controller.update(sport_id, content)
    return make_response(jsonify(obj), HTTPStatus.OK)


@sport_bp.patch('/<int:sport_id>')
def patch_sport(sport_id: int) -> Response:
    content = request.get_json()
    obj = sport_controller.patch(sport_id, content)
    return make_response(jsonify(obj), HTTPStatus.OK)


@sport_bp.delete('/<int:sport_id>')
def delete_sport(sport_id: int) -> Response:
    sport_controller.delete(sport_id)
    return make_response("Sport deleted", HTTPStatus.OK)
