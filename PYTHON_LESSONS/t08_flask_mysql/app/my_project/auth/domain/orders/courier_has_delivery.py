"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class CourierHasDelivery(db.Model):
    """
    Model declaration for the relationship table between Courier and Delivery.
    """
    __tablename__ = "courier_has_delivery"

    courier_id = db.Column(db.BigInteger, db.ForeignKey('courier.id'), primary_key=True)
    delivery_id = db.Column(db.BigInteger, db.ForeignKey('delivery.id'), primary_key=True)

    def __repr__(self) -> str:
        return f"CourierHasDelivery({self.courier_id}, {self.delivery_id})"
