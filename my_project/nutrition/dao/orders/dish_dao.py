from my_project.nutrition.dao.general_dao import GeneralDAO
from my_project.nutrition.domain import Dish


class DishDAO(GeneralDAO):
    _domain_type = Dish

    def find_by_name(self, name: str) -> list[Dish]:
        session = self.get_session()
        dishes = session.query(Dish).filter(Dish.name == name).order_by(Dish.name).all()
        return [dish.put_into_dto() for dish in dishes]

    def get_dishes_by_calories(self, calories: int) -> list[Dish]:
        session = self.get_session()
        dishes = session.query(Dish).filter(Dish.calories == calories).order_by(Dish.name).all()
        return [dish.put_into_dto() for dish in dishes]
