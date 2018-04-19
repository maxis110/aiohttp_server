from sendify.alembic_models.base_alembic_class import BaseAlembic


class HeadersEntryData(BaseAlembic):
    def __init__(self, request):
        self._origin_city = request.headers.get("origin_city")
        self._destination_city = request.headers.get("destination_city")
        self._product_type = request.headers.get("product_type")
        self._weight = request.headers.get("weight")
        self._width = request.headers.get("width")
        self._height = request.headers.get("height")
        self._length = request.headers.get("length")

    @property
    def origin_city(self):
        """Gets the origin_city from headers.

        :return: The origin_city.
        :rtype: str
        """
        return self._origin_city

    @origin_city.setter
    def origin_city(self, origin_city: str):
        """Sets the origin_city of this HeadersEntryData.

        Identifier of job type  # noqa: E501

        :param reports_type: The origin_city.
        :type reports_type: str
        """

        self._origin_city = origin_city

    @property
    def destination_city(self):
        """Gets the destination_city from headers.

        :return: The destination_city.
        :rtype: str
        """
        return self._destination_city

    @destination_city.setter
    def destination_city(self, destination_city: str):
        """Sets the destination_city of this HeadersEntryData.

        Identifier of job type  # noqa: E501

        :param reports_type: The destination_city.
        :type reports_type: str
        """

        self._destination_city = destination_city

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
    def weight(self):
        """Gets the weight from headers.

        :return: The destination_city.
        :rtype: str
        """
        return self._weight

    @weight.setter
    def weight(self, weight: str):
        """Sets the weight of this HeadersEntryData.

        Identifier of job type  # noqa: E501

        :param reports_type: The weight.
        :type reports_type: str
        """

        self._weight = weight

    @property
    def width(self):
        """Gets the width from headers.

        :return: The destination_city.
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width: str):
        """Sets the width of this HeadersEntryData.

        Identifier of job type  # noqa: E501

        :param reports_type: The width.
        :type reports_type: str
        """

        self._width = width

    @property
    def height(self):
        """Gets the height from headers.

        :return: The height.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height: str):
        """Sets the height of this HeadersEntryData.

        Identifier of job type  # noqa: E501

        :param reports_type: The height.
        :type reports_type: str
        """

        self._height = height

    @property
    def length(self):
        """Gets the length from headers.

        :return: The length.
        :rtype: str
        """
        return self._length

    @length.setter
    def length(self, length: str):
        """Sets the length of this HeadersEntryData.

        Identifier of job type  # noqa: E501

        :param reports_type: The length.
        :type reports_type: str
        """

        self._length = length
