"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Operator
from sqlalchemy import text


class OperatorDAO(GeneralDAO):
    """
    Realisation of Operator data access layer.
    """
    _domain_type = Operator

    def find_by_name(self, name: str) -> List[object]:
        """
        Gets Operator objects from the database table by field 'name'.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Operator).filter(Operator.name == name).order_by(Operator.name).all()

    def find_by_surname(self, surname: str) -> List[object]:
        """
        Gets Operator objects from the database table by field 'surname'.
        :param surname: surname value
        :return: search objects
        """
        return self._session.query(Operator).filter(Operator.surname == surname).order_by(Operator.surname).all()

    def find_by_phone(self, phone: str) -> List[object]:
        """
        Gets Operator objects from the database table by field 'phone'.
        :param phone: phone value
        :return: search objects
        """
        return self._session.query(Operator).filter(Operator.phone == phone).order_by(Operator.phone).all()

    def insert_10_tapes_operator(self, user_table_operator_name):
        try:
            self._session.execute(text(
                f"CALL insert_10_tapes_operator('{user_table_operator_name}')",
            ))
            self._session.commit()
            return "insert_10_tapes_operator OK"
        except Exception as e:
            self._session.rollback()
            return f"Error: {str(e)}"

    def cursor_dynamic_table(self):
        try:
            self._session.execute(text("CALL cursor_dynamic_table()"))
            self._session.commit()
            return "cursor_dynamic_table OK"
        except Exception as e:
            self._session.rollback()
            return f"Error: {str(e)}"
