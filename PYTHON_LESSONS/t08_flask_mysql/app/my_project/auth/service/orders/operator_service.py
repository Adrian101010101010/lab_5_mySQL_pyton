"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import operator_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class OperatorService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = operator_dao

    def insert_10_tapes_operator(self, table_operator_name):
        result = self._dao.insert_10_tapes_operator(table_operator_name)
        return result

    def cursor_dynamic_table(self):
        result = self._dao.cursor_dynamic_table()
        return result
