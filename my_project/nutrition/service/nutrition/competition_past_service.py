from my_project.nutrition.dao.orders import competition_past_dao
from my_project.nutrition.service.general_service import GeneralService


class CompetitionPastService(GeneralService):
    _dao = competition_past_dao

    def find_by_place(self, place_id: int):
        return self._dao.find_by_place(place_id)
