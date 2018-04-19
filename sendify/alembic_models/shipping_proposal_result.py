from sendify.alembic_models.base_alembic_class import BaseAlembic


class ShippingProposalResult(BaseAlembic):
    def __init__(self, carrier_name=None, product_type=None, price=None, expected_transit_time=None):
        self._carrier_name = carrier_name
        self._product_type = product_type
        self._price = price
        self._expected_transit_time = expected_transit_time

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
    def product_type(self):
        """Gets the product_type from headers.

        :return: The product_type.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type: str):
        """Sets the product_type of this HeadersEntryData.

        Identifier of job type  # noqa: E501

        :param reports_type: The product_type.
        :type reports_type: str
        """

        self._product_type = product_type

    @property
    def price(self):
        """Gets the price from headers.

        :return: The price.
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price: str):
        """Sets the price of this HeadersEntryData.

        Identifier of job type  # noqa: E501

        :param reports_type: The price.
        :type reports_type: str
        """

        self._price = price

    @property
    def expected_transit_time(self):
        """Gets the expected_transit_time from headers.

        :return: The expected_transit_time.
        :rtype: str
        """
        return self._expected_transit_time

    @expected_transit_time.setter
    def expected_transit_time(self, expected_transit_time: str):
        """Sets the expected_transit_time of this HeadersEntryData.

        Identifier of job type  # noqa: E501

        :param reports_type: The expected_transit_time.
        :type reports_type: str
        """

        self._expected_transit_time = expected_transit_time
