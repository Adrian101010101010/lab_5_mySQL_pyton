"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# orders DB
from .orders.client_dao import ClientDAO
from .orders.client_type_dao import ClientTypeDAO
from .orders.city_dao import CityDAO
from .orders.courier_dao import CourierDAO
from .orders.courier_has_delivery_dao import CourierHasDeliveryDAO
from .orders.department_dao import DepartmentDAO
from .orders.operator_dao import OperatorDAO
from .orders.parcel_dao import ParcelDAO
from .orders.parcel_has_courier_dao import ParcelHasCourierDAO
from .orders.regione_dao import RegioneDAO
from .orders.user_dao import UserDAO
from .orders.delivery_dao import DeliveryDAO
from .orders.post_office_dao import PostOfficeDAO

client_dao = ClientDAO()
client_type_dao = ClientTypeDAO()
city_dao = CityDAO()
courier_dao = CourierDAO()
courier_has_delivery_dao = CourierHasDeliveryDAO()
department_dao = DepartmentDAO()
operator_dao = OperatorDAO()
parcel_dao = ParcelDAO()
parcel_has_courier_dao = ParcelHasCourierDAO()
regione_dao = RegioneDAO()
user_dao = UserDAO()
delivery_dao = DeliveryDAO()
post_office_dao = PostOfficeDAO()
