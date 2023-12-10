"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import user_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class UserController(GeneralController):
    """
    Realisation of User controller.
    """
    _service = user_service

    def insert_10_tapes(self, table_name):
        result = self._service.insert_10_tapes(table_name)
        return result
