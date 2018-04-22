from sendify.alembic_models.base_alembic_class import BaseAlembic


class TransitTimeDbResult(BaseAlembic):
    def __init__(self, origin_city=None, destination_city=None, transit_time=None, carrier_id=None, distance=None):
        self._origin_city = origin_city
        self._destination_city = destination_city
        self._transit_time = transit_time
        self._carrier_id = carrier_id
        self._distance = distance


    @property
    def origin_city(self):
        """Gets the origin_city.

        :return: The origin_city.
        :rtype: str
        """
        return self._origin_city

    @origin_city.setter
    def origin_city(self, origin_city: str):
        """Sets the origin_city.

        :param reports_type: The origin_city.
        :type reports_type: str
        """

        self._origin_city = origin_city

    @property
    def destination_city(self):
        """Gets the destination_city.

        :return: The destination_city.
        :rtype: str
        """
        return self._destination_city

    @destination_city.setter
    def destination_city(self, destination_city: str):
        """Sets the destination_city.

        :param reports_type: The destination_city.
        :type reports_type: str
        """

        self._destination_city = destination_city

    @property
    def transit_time(self):
        """Gets the transit_time.

        :return: The transit_time.
        :rtype: str
        """
        return self._transit_time

    @transit_time.setter
    def transit_time(self, transit_time: str):
        """Sets the transit_time.

        :param reports_type: The transit_time.
        :type reports_type: str
        """

        self._transit_time = transit_time

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
    def distance(self):
        """Gets the distance.

        :return: The distance.
        :rtype: str
        """
        return self._distance

    @distance.setter
    def distance(self, distance: str):
        """Sets the distance.

        :param reports_type: The distance.
        :type reports_type: str
        """

        self._distance = distance
