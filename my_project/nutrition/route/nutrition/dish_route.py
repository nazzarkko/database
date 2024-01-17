from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.nutrition.controller import dish_controller

dish_bp = Blueprint('dish', __name__, url_prefix='/dish')


@dish_bp.get('/<int:dish_id>')
def get_dish(dish_id: int) -> Response:
    return make_response(jsonify(dish_controller.find_by_id(dish_id)), HTTPStatus.OK)


@dish_bp.get('')
def get_all_dishes() -> Response:
    return make_response(jsonify(dish_controller.find_all()), HTTPStatus.OK)


@dish_bp.post('')
def create_dish() -> Response:
    content = request.get_json()
    obj = dish_controller.create(content)
    return make_response(jsonify(obj), HTTPStatus.CREATED)


@dish_bp.put('/<int:dish_id>')
def update_dish(dish_id: int) -> Response:
    content = request.get_json()
    obj = dish_controller.update(dish_id, content)
    return make_response(jsonify(obj), HTTPStatus.OK)


@dish_bp.patch('/<int:dish_id>')
def patch_dish(dish_id: int) -> Response:
    content = request.get_json()
    obj = dish_controller.patch(dish_id, content)
    return make_response(jsonify(obj), HTTPStatus.OK)


@dish_bp.delete('/<int:dish_id>')
def delete_dish(dish_id: int) -> Response:
    dish_controller.delete(dish_id)
    return make_response("Dish deleted", HTTPStatus.OK)
