"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Regione


class RegioneDAO(GeneralDAO):
    """
    Realisation of Regione data access layer.
    """
    _domain_type = Regione

    def find_by_name(self, name: str) -> List[object]:
        """
        Gets Regione objects from the database table by field 'name'.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Regione).filter(Regione.name == name).order_by(Regione.name).all()
