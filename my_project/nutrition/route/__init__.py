"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp
from .nutrition.competition_past_route import competition_past_bp


def register_routes(app: Flask) -> None:
    def register_routes(app):
        from my_project.nutrition.route.nutrition.day_route import day_bp
        from my_project.nutrition.route.nutrition.dish_route import dish_bp
        from my_project.nutrition.route.nutrition.nutritional_suplement_route import nutritional_suplement_bp
        from my_project.nutrition.route.nutrition.place_route import place_bp
        from my_project.nutrition.route.nutrition.shchedule_route import schedule_bp
        from my_project.nutrition.route.nutrition.sport_route import sport_bp
        from my_project.nutrition.route.nutrition.sportsmen_route import sportsmen_bp
        from my_project.nutrition.route.nutrition.trainer_route import trainer_bp
        from .nutrition.competition_past_route import competition_past_bp

        """
        Registers all necessary Blueprint routes
        :param app: Flask application object
        """
        app.register_blueprint(err_handler_bp)
        app.register_blueprint(competition_past_bp)
        app.register_blueprint(dish_bp)
        app.register_blueprint(day_bp)
        app.register_blueprint(nutritional_suplement_bp)
        app.register_blueprint(place_bp)
        app.register_blueprint(schedule_bp)
        app.register_blueprint(sport_bp)
        app.register_blueprint(sportsmen_bp)
        app.register_blueprint(trainer_bp)

    register_routes(app)
