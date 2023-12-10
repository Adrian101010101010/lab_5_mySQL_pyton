"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import post_office_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class PostOfficeService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = post_office_dao
