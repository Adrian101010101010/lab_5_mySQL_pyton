"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import user_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class UserService(GeneralService):
    """
    Realisation of User service.
    """
    _dao = user_dao

    def insert_10_tapes(self, table_name):
        result = self._dao.insert_10_tapes(table_name)
        return result
