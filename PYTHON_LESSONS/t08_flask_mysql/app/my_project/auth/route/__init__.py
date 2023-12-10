"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.client_route import client_bp
    from .orders.client_type_route import client_type_bp
    from .orders.city_route import city_bp
    from .orders.courier_route import courier_bp
    from .orders.courier_has_delivery_route import courier_has_delivery_bp
    from .orders.delivery_route import delivery_bp
    from .orders.department_route import department_bp
    from .orders.operator_route import operator_bp
    from .orders.parcel_has_courier_route import parcel_has_courier_bp
    from .orders.parcel_route import parcel_bp
    from .orders.regione_route import regione_bp
    from .orders.user_route import user_bp
    from .orders.post_office_route import post_office_bp

    app.register_blueprint(client_bp)
    app.register_blueprint(client_type_bp)
    app.register_blueprint(city_bp)
    app.register_blueprint(courier_has_delivery_bp)
    app.register_blueprint(courier_bp)
    app.register_blueprint(delivery_bp)
    app.register_blueprint(department_bp)
    app.register_blueprint(operator_bp)
    app.register_blueprint(parcel_has_courier_bp)
    app.register_blueprint(parcel_bp)
    app.register_blueprint(regione_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(post_office_bp)
