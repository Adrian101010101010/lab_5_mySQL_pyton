"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import User
from sqlalchemy import text

class UserDAO(GeneralDAO):
    """
    Realisation of User data access layer.
    """
    _domain_type = User

    def find_by_name(self, name: str) -> List[object]:
        """
        Gets User objects from the database table by field 'name'.
        :param name: name value
        :return: search objects
        """
        return self._session.query(User).filter(User.name == name).order_by(User.name).all()

    def find_by_surname(self, surname: str) -> List[object]:
        """
        Gets User objects from the database table by field 'surname'.
        :param surname: surname value
        :return: search objects
        """
        return self._session.query(User).filter(User.surname == surname).order_by(User.surname).all()

    def find_by_phone(self, phone: str) -> List[object]:
        """
        Gets User objects from the database table by field 'phone'.
        :param phone: phone value
        :return: search objects
        """
        return self._session.query(User).filter(User.phone == phone).order_by(User.phone).all()

    def insert_10_tapes(self, user_table_name):
        try:
            self._session.execute(text(
                f"CALL insert_10_tapes('{user_table_name}')",
            ))
            self._session.commit()
            return "insert_10_tapes OK"
        except Exception as e:
            self._session.rollback()
            return f"Error: {str(e)}"
