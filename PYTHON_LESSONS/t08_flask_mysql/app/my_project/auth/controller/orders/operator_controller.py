"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import operator_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class OperatorController(GeneralController):
    """
    Realisation of Operator controller.
    """
    _service = operator_service

    def insert_10_tapes_operator(self, table_operator_name):
        result = self._service.insert_10_tapes_operator(table_operator_name)
        return result

    def cursor_dynamic_table(self):
        result = self._service.cursor_dynamic_table()
        return result
