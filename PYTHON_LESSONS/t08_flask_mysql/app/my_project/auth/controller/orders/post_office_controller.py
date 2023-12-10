"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""
from typing import List, Dict

from t08_flask_mysql.app.my_project.auth.service import post_office_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class PostOfficeController(GeneralController):
    """
    Realisation of  ParcelHasCourier controller.
    """
    _service = post_office_service


