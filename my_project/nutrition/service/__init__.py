"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .nutrition.competition_past_service import CompetitionPastService
from .nutrition.day_service import DayService
from .nutrition.dish_service import DishService
from .nutrition.nutritional_suplement_service import NutritionalSuplementService
from .nutrition.place_service import PlaceService
from .nutrition.shchedule_service import ShcheduleService
from .nutrition.sport_service import SportService
from .nutrition.sportsmen_service import SportsmenService
from .nutrition.trainer_service import TrainerService

competition_past_service = CompetitionPastService()
day_service = DayService()
dish_service = DishService()
nutritional_suplement_service = NutritionalSuplementService()
place_service = PlaceService()
shchedule_service = ShcheduleService()
sport_service = SportService()
sportsmen_service = SportsmenService()
trainer_service = TrainerService()
