from my_project.nutrition.dao.orders import day_dao
from my_project.nutrition.service.general_service import GeneralService

class DayService(GeneralService):
    _dao = day_dao

    def find_by_dish(self, dish_id: int):
        return self._dao.find_by_dish(dish_id)

    def find_by_nutritional_suplement(self, nutritional_suplement_id: int):
        return self._dao.find_by_nutritional_suplement(nutritional_suplement_id)
