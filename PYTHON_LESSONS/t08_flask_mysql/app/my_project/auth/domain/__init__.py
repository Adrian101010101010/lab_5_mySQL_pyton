"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# Import here Domain Class that are needed for ORM
# orders DB
from t08_flask_mysql.app.my_project.auth.domain.orders.client import Client
from t08_flask_mysql.app.my_project.auth.domain.orders.client_type import ClientType
from t08_flask_mysql.app.my_project.auth.domain.orders.city import City
from t08_flask_mysql.app.my_project.auth.domain.orders.courier import Courier
from t08_flask_mysql.app.my_project.auth.domain.orders.courier_has_delivery import CourierHasDelivery
from t08_flask_mysql.app.my_project.auth.domain.orders.delivery import Delivery
from t08_flask_mysql.app.my_project.auth.domain.orders.department import Department
from t08_flask_mysql.app.my_project.auth.domain.orders.operator import Operator
from t08_flask_mysql.app.my_project.auth.domain.orders.parcel import Parcel
from t08_flask_mysql.app.my_project.auth.domain.orders.parcel_has_courier import ParcelHasCourier
from t08_flask_mysql.app.my_project.auth.domain.orders.regione import Regione
from t08_flask_mysql.app.my_project.auth.domain.orders.user import User
from t08_flask_mysql.app.my_project.auth.domain.orders.post_office import PostOffice

