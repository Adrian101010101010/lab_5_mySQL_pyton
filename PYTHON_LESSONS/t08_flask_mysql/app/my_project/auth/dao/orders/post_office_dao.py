"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import PostOffice


class PostOfficeDAO(GeneralDAO):
    """
    Realisation of Post_office data access layer.
    """
    _domain_type = PostOffice

    def find_by_number(self, number: str) -> List[object]:
        """
        Gets Post_office objects from the database table by field 'number'.
        :param number: number value
        :return: search objects
        """
        return self._session.query(PostOffice).filter(PostOffice.number == number).all()
