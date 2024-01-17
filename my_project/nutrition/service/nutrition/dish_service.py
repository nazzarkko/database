from my_project.nutrition.dao.orders import dish_dao
from my_project.nutrition.service.general_service import GeneralService

class DishService(GeneralService):
    _dao = dish_dao
