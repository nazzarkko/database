from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.nutrition.controller import nutritional_suplement_controller

nutritional_suplement_bp = Blueprint('nutritional_suplement', __name__, url_prefix='/nutritional_suplement')


@nutritional_suplement_bp.get('/<int:nutritional_suplement_id>')
def get_nutritional_suplement(nutritional_suplement_id: int) -> Response:
    return make_response(jsonify(nutritional_suplement_controller.find_by_id(nutritional_suplement_id)), HTTPStatus.OK)


@nutritional_suplement_bp.get('')
def get_all_nutritional_suplements() -> Response:
    return make_response(jsonify(nutritional_suplement_controller.find_all()), HTTPStatus.OK)


@nutritional_suplement_bp.post('')
def create_nutritional_suplement() -> Response:
    content = request.get_json()
    obj = nutritional_suplement_controller.create(content)
    return make_response(jsonify(obj), HTTPStatus.CREATED)


@nutritional_suplement_bp.put('/<int:nutritional_suplement_id>')
def update_nutritional_suplement(nutritional_suplement_id: int) -> Response:
    content = request.get_json()
    obj = nutritional_suplement_controller.update(nutritional_suplement_id, content)
    return make_response(jsonify(obj), HTTPStatus.OK)


@nutritional_suplement_bp.patch('/<int:nutritional_suplement_id>')
def patch_nutritional_supplement(nutritional_suplement_id: int) -> Response:
    content = request.get_json()
    obj = nutritional_suplement_controller.patch(nutritional_suplement_id, content)
    return make_response(jsonify(obj), HTTPStatus.OK)


@nutritional_suplement_bp.delete('/<int:nutritional_suplement_id>')
def delete_nutritional_supplement(nutritional_suplement_id: int) -> Response:
    nutritional_suplement_controller.delete(nutritional_suplement_id)
    return make_response("Nutritional Suplement deleted", HTTPStatus.OK)
