from sendify.alembic_models.base_alembic_class import BaseAlembic


class DbParameters(BaseAlembic):
    def __init__(self, conf):
        self._db = conf.get("postgres")
        self._host_db = self._db.get("host")
        self._user_db = self._db.get("user")
        self._password_db = self._db.get("password")
        self._database = self._db.get("database")

    @property
    def db(self):
        """Gets the db.

        :return: The db.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db: str):
        """Sets the db.

        :param reports_type: The db.
        :type reports_type: str
        """

        self._db = db

    @property
    def host_db(self):
        """Gets the host_db.

        :return: The host_db.
        :rtype: str
        """
        return self._host_db

    @host_db.setter
    def host_db(self, host_db: str):
        """Sets the host_db.

        :param reports_type: The host_db.
        :type reports_type: str
        """

        self._host_db = host_db

    @property
    def user_db(self):
        """Gets the user_db.

        :return: The user_db.
        :rtype: str
        """
        return self._user_db

    @user_db.setter
    def user_db(self, user_db: str):
        """Sets the user_db.

        :param reports_type: The user_db.
        :type reports_type: str
        """

        self._user_db = user_db

    @property
    def password_db(self):
        """Gets the password_db.

        :return: The password_db.
        :rtype: str
        """
        return self._password_db

    @password_db.setter
    def password_db(self, password_db: str):
        """Sets the password_db.

        :param reports_type: The password_db.
        :type reports_type: str
        """

        self._password_db = password_db

    @property
    def database(self):
        """Gets the database.

        :return: The database.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database: str):
        """Sets the database.

        :param reports_type: The database.
        :type reports_type: str
        """

        self._database = database
