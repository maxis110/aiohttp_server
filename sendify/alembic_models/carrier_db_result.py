class CarrierDbResult(object):
    def __init__(self, carrier_name=None, price_per_km=None, price_per_kg=None):
        self._carrier_name = carrier_name
        self._price_per_km = price_per_km
        self._price_per_kg = price_per_kg


    @property
    def carrier_name(self):
        """Gets the carrier_name from headers.

        :return: The carrier_name.
        :rtype: str
        """
        return self._carrier_name

    @carrier_name.setter
    def carrier_name(self, carrier_name: str):
        """Sets the carrier_name of this HeadersEntryData.

        Identifier of job type  # noqa: E501

        :param reports_type: The carrier_name.
        :type reports_type: str
        """

        self._carrier_name = carrier_name

    @property
    def price_per_km(self):
        """Gets the price_per_km from headers.

        :return: The price_per_km.
        :rtype: str
        """
        return self._price_per_km

    @price_per_km.setter
    def price_per_km(self, price_per_km: str):
        """Sets the price_per_km of this HeadersEntryData.

        Identifier of job type  # noqa: E501

        :param reports_type: The price_per_km.
        :type reports_type: str
        """

        self._price_per_km = price_per_km

    @property
    def price_per_kg(self):
        """Gets the product_type from headers.

        :return: The product_type.
        :rtype: str
        """
        return self._price_per_kg

    @price_per_kg.setter
    def price_per_kg(self, price_per_kg: str):
        """Sets the price_per_kg of this HeadersEntryData.

        Identifier of job type  # noqa: E501

        :param reports_type: The price_per_kg.
        :type reports_type: str
        """

        self._price_per_kg = price_per_kg
