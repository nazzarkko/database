from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.nutrition.controller import schedule_controller

schedule_bp = Blueprint('schedule', __name__, url_prefix='/schedule')


@schedule_bp.get('/<int:schedule_id>')
def get_schedule(schedule_id: int) -> Response:
    return make_response(jsonify(schedule_controller.find_by_id(schedule_id)), HTTPStatus.OK)


@schedule_bp.get('')
def get_all_schedules() -> Response:
    return make_response(jsonify(schedule_controller.find_all()), HTTPStatus.OK)


@schedule_bp.post('')
def create_schedule() -> Response:
    content = request.get_json()
    obj = schedule_controller.create(content)
    return make_response(jsonify(obj), HTTPStatus.CREATED)


@schedule_bp.put('/<int:schedule_id>')
def update_schedule(schedule_id: int) -> Response:
    content = request.get_json()
    obj = schedule_controller.update(schedule_id, content)
    return make_response(jsonify(obj), HTTPStatus.OK)


@schedule_bp.patch('/<int:schedule_id>')
def patch_schedule(schedule_id: int) -> Response:
    content = request.get_json()
    obj = schedule_controller.patch(schedule_id, content)
    return make_response(jsonify(obj), HTTPStatus.OK)


@schedule_bp.delete('/<int:schedule_id>')
def delete_schedule(schedule_id: int) -> Response:
    schedule_controller.delete(schedule_id)
    return make_response("Schedule deleted", HTTPStatus.OK)
