from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.nutrition.controller import place_controller

place_bp = Blueprint('place', __name__, url_prefix='/place')


@place_bp.get('/<int:place_id>')
def get_place(place_id: int) -> Response:
    return make_response(jsonify(place_controller.find_by_id(place_id)), HTTPStatus.OK)


@place_bp.get('')
def get_all_places() -> Response:
    return make_response(jsonify(place_controller.find_all()), HTTPStatus.OK)


@place_bp.post('')
def create_place() -> Response:
    content = request.get_json()
    obj = place_controller.create(content)
    return make_response(jsonify(obj), HTTPStatus.CREATED)


@place_bp.put('/<int:place_id>')
def update_place(place_id: int) -> Response:
    content = request.get_json()
    obj = place_controller.update(place_id, content)
    return make_response(jsonify(obj), HTTPStatus.OK)


@place_bp.patch('/<int:place_id>')
def patch_place(place_id: int) -> Response:
    content = request.get_json()
    obj = place_controller.patch(place_id, content)
    return make_response(jsonify(obj), HTTPStatus.OK)


@place_bp.delete('/<int:place_id>')
def delete_place(place_id: int) -> Response:
    place_controller.delete(place_id)
    return make_response("Place deleted", HTTPStatus.OK)
