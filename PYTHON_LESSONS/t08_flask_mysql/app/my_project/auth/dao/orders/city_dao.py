"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import City


class CityDAO(GeneralDAO):
    """
    Realisation of City data access layer.
    """
    _domain_type = City

    def find_by_city_name(self, city_name: str) -> List[object]:
        """
        Gets City objects from the database table by field 'city_name'.
        :param city_name: city_name value
        :return: search objects
        """
        return self._session.query(City).filter(City.city_name == city_name).order_by(City.city_name).all()

    def insert_noname_records(self):
        """
        Inserts 10 records in the format <Noname+№> into the City table.
        """
        records_to_insert = [
            City(city_name=f'Noname{i}') for i in range(1, 11)
        ]

        for record in records_to_insert:
            self._session.add(record)

        self._session.commit()
