from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.nutrition.controller import competition_past_controller

competition_past_bp = Blueprint('competition_past', __name__, url_prefix='/competition_past')


@competition_past_bp.get('/<int:competition_past_id>')
def get_competition_past(competition_past_id: int) -> Response:
    return make_response(jsonify(competition_past_controller.find_by_id(competition_past_id)), HTTPStatus.OK)


@competition_past_bp.get('')
def get_all_competition_past() -> Response:
    return make_response(jsonify(competition_past_controller.find_all()), HTTPStatus.OK)


@competition_past_bp.post('')
def create_competition_past() -> Response:
    content = request.get_json()
    obj = competition_past_controller.create(content)
    return make_response(jsonify(obj), HTTPStatus.CREATED)


@competition_past_bp.put('/<int:competition_past_id>')
def update_competition_past(competition_past_id: int) -> Response:
    content = request.get_json()
    obj = competition_past_controller.update(competition_past_id, content)
    return make_response(jsonify(obj), HTTPStatus.OK)


@competition_past_bp.patch('/<int:competition_past_id>')
def patch_competition_past(competition_past_id: int) -> Response:
    content = request.get_json()
    obj = competition_past_controller.patch(competition_past_id, content)
    return make_response(jsonify(obj), HTTPStatus.OK)


@competition_past_bp.delete('/<int:competition_past_id>')
def delete_competition_past(competition_past_id: int) -> Response:
    competition_past_controller.delete(competition_past_id)
    return make_response("Competition Past deleted", HTTPStatus.OK)
