from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.nutrition.controller import trainer_controller

trainer_bp = Blueprint('trainer', __name__, url_prefix='/trainer')


@trainer_bp.get('/<int:trainer_id>')
def get_trainer(trainer_id: int) -> Response:
    return make_response(jsonify(trainer_controller.find_by_id(trainer_id)), HTTPStatus.OK)


@trainer_bp.get('')
def get_all_trainers() -> Response:
    return make_response(jsonify(trainer_controller.find_all()), HTTPStatus.OK)


@trainer_bp.post('')
def create_trainer() -> Response:
    content = request.get_json()
    obj = trainer_controller.create(content)
    return make_response(jsonify(obj), HTTPStatus.CREATED)


@trainer_bp.put('/<int:trainer_id>')
def update_trainer(trainer_id: int) -> Response:
    content = request.get_json()
    obj = trainer_controller.update(trainer_id, content)
    return make_response(jsonify(obj), HTTPStatus.OK)


@trainer_bp.patch('/<int:trainer_id>')
def patch_trainer(trainer_id: int) -> Response:
    content = request.get_json()
    obj = trainer_controller.patch(trainer_id, content)
    return make_response(jsonify(obj), HTTPStatus.OK)


@trainer_bp.delete('/<int:trainer_id>')
def delete_trainer(trainer_id: int) -> Response:
    trainer_controller.delete(trainer_id)
    return make_response("Trainer deleted", HTTPStatus.OK)
