from sendify.alembic_models.base_alembic_class import BaseAlembic


class ProductDbResult(BaseAlembic):
    def __init__(self, product_type=None, def_weight=None, def_width=None, def_height=None, def_length=None):
        self._product_type = product_type
        self._def_weight = def_weight
        self._def_width = def_width
        self._def_height = def_height
        self._def_length = def_length


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
    def def_weight(self):
        """Gets the def_weight from headers.

        :return: The def_weight.
        :rtype: str
        """
        return self._def_weight

    @def_weight.setter
    def def_weight(self, def_weight: str):
        """Sets the def_weight of this HeadersEntryData.

        Identifier of job type  # noqa: E501

        :param reports_type: The def_weight.
        :type reports_type: str
        """

        self._def_weight = def_weight

    @property
    def def_width(self):
        """Gets the def_width from headers.

        :return: The def_width.
        :rtype: str
        """
        return self._def_width

    @def_width.setter
    def def_width(self, def_width: str):
        """Sets the def_width of this HeadersEntryData.

        Identifier of job type  # noqa: E501

        :param reports_type: The def_width.
        :type reports_type: str
        """

        self._def_width = def_width

    @property
    def def_height(self):
        """Gets the def_height from headers.

        :return: The def_height.
        :rtype: str
        """
        return self._def_height

    @def_height.setter
    def def_height(self, def_height: str):
        """Sets the def_height of this HeadersEntryData.

        Identifier of job type  # noqa: E501

        :param reports_type: The def_height.
        :type reports_type: str
        """

        self._def_height = def_height

    @property
    def def_length(self):
        """Gets the def_length from headers.

        :return: The def_length.
        :rtype: str
        """
        return self._def_length

    @def_length.setter
    def def_length(self, def_length: str):
        """Sets the def_length of this HeadersEntryData.

        Identifier of job type  # noqa: E501

        :param reports_type: The def_length.
        :type reports_type: str
        """

        self._def_length = def_length
