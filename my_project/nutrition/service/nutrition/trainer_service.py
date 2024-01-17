from my_project.nutrition.dao.orders import trainer_dao
from my_project.nutrition.service.general_service import GeneralService

class TrainerService(GeneralService):
    _dao = trainer_dao

    def find_by_sportsmen(self, sportsmen_id: int):
        return self._dao.find_by_sportsmen(sportsmen_id)
