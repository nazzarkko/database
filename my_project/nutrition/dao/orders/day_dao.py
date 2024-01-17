from my_project.nutrition.dao.general_dao import GeneralDAO
from my_project.nutrition.domain import Day


class DayDAO(GeneralDAO):
    _domain_type = Day

    def find_by_name(self, name: str) -> list[Day]:
        session = self.get_session()
        days = session.query(Day).filter(Day.name == name).order_by(Day.name).all()
        return [day.put_into_dto() for day in days]

    def get_days_by_dish(self, dish_id: int) -> list[Day]:
        session = self.get_session()
        days = session.query(Day).filter(Day.dish == dish_id).order_by(Day.name).all()
        return [day.put_into_dto() for day in days]
