from sendify.alembic_models.base_alembic_class import BaseAlembic


class CarrierDbResult(BaseAlembic):
    def __init__(self, carrier_id=None, carrier_name=None, price_per_km=None, price_per_kg=None):
        self._carrier_id = carrier_id
        self._carrier_name = carrier_name
        self._price_per_km = price_per_km
        self._price_per_kg = price_per_kg

    @property
    def carrier_id(self):
        """Gets the carrier_id.

        :return: The carrier_id.
        :rtype: str
        """
        return self._carrier_id

    @carrier_id.setter
    def carrier_id(self, carrier_id: str):
        """Sets the carrier_id.

        :param reports_type: The carrier_id.
        :type reports_type: str
        """

        self._carrier_id = carrier_id

    @property
    def carrier_name(self):
        """Gets the carrier_name.

        :return: The carrier_name.
        :rtype: str
        """
        return self._carrier_name

    @carrier_name.setter
    def carrier_name(self, carrier_name: str):
        """Sets the carrier_name.

        :param reports_type: The carrier_name.
        :type reports_type: str
        """

        self._carrier_name = carrier_name

    @property
    def price_per_km(self):
        """Gets the price_per_km.

        :return: The price_per_km.
        :rtype: str
        """
        return self._price_per_km

    @price_per_km.setter
    def price_per_km(self, price_per_km: str):
        """Sets the price_per_km.

        :param reports_type: The price_per_km.
        :type reports_type: str
        """

        self._price_per_km = price_per_km

    @property
    def price_per_kg(self):
        """Gets the product_type.

        :return: The product_type.
        :rtype: str
        """
        return self._price_per_kg

    @price_per_kg.setter
    def price_per_kg(self, price_per_kg: str):
        """Sets the price_per_kg.

        :param reports_type: The price_per_kg.
        :type reports_type: str
        """

        self._price_per_kg = price_per_kg
