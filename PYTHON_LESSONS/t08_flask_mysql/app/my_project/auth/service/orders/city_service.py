"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import city_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class CityService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = city_dao

    def insert_noname_records(self):
        """
        Inserts 10 records in the format <Noname+№> into the City table using DAO.
        """
        self._dao.insert_noname_records()
