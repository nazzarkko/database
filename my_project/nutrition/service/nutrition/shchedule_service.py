from my_project.nutrition.dao.orders import shchedule_dao
from my_project.nutrition.service.general_service import GeneralService

class ShcheduleService(GeneralService):
    _dao = shchedule_dao

    def find_by_day(self, day_id: int):
        return self._dao.find_by_day(day_id)

    def find_by_sportsmen(self, sportsmen_id: int):
        return self._dao.find_by_sportsmen(sportsmen_id)
