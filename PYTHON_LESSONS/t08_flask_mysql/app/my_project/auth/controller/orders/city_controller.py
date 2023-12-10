"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import city_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class CityController(GeneralController):
    """
    Realisation of City controller.
    """
    _service = city_service

    def insert_noname_records(self) -> None:
        """
        Inserts 10 records in the format <Noname+№> into the City table using Service layer.
        """
        self._service.insert_noname_records()
