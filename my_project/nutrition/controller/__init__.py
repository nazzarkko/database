"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.competition_past_controller import CompetitionPastController
from .orders.day_controller import DayController
from .orders.dish_controller import DishController
from .orders.nutritional_suplement_controller import NutritionalSuplementController
from .orders.place_controller import PlaceController
from .orders.schedule_controller import ShcheduleController
from .orders.sport_controller import SportController
from .orders.sportsmen_controller import SportsmenController
from .orders.trainer_controller import TrainerController

competition_past_controller = CompetitionPastController()
day_controller = DayController()
dish_controller = DishController()
nutritional_suplement_controller = NutritionalSuplementController()
place_controller = PlaceController()
schedule_controller = ShcheduleController()
sport_controller = SportController()
sportsmen_controller = SportsmenController()
trainer_controller = TrainerController()
