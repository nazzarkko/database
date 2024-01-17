from my_project.nutrition.dao.general_dao import GeneralDAO
from my_project.nutrition.domain import Shchedule


class ScheduleDAO(GeneralDAO):
    _domain_type = Shchedule

    def find_by_id(self, schedule_id: int) -> Shchedule:
        return self._session.query(Shchedule).filter(Shchedule.id == schedule_id).first()

    def get_schedules_by_day(self, day_id: int) -> list[Shchedule]:
        schedules = (
            self._session.query(Shchedule)
            .filter(Shchedule.day == day_id)
            .order_by(Shchedule.sportsman, Shchedule.day)
            .all()
        )
        return [schedule.put_into_dto() for schedule in schedules]
