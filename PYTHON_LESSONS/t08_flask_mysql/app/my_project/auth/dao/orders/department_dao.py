"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Department


class DepartmentDAO(GeneralDAO):
    """
    Realisation of Department data access layer.
    """
    _domain_type = Department

    def find_by_name(self, name: str) -> List[object]:
        """
        Gets Department objects from the database table by field 'name'.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Department).filter(Department.name == name).order_by(Department.name).all()


