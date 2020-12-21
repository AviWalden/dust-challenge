class UserStorage:
    """
    Represents some form of user data storage that provides access to a user's things.
    """
    @property
    def things(self):
        """
        Gets all things for a user.

        :returns: list<dict>
        """
        raise NotImplementedError

    @property
    def catalogs(self):
        """
        Gets all unique catalogs for a user.

        :returns: list<dict>
        """
        raise NotImplementedError

class CsvUserStorage(UserStorage):
    """
    UserStorage object for accessing a user's data if it is stored locally, on disk in a CSV.

    :param: csv_filepath: string: filepath of the CSV with user's data
    """
    def __init__(self, csv_filepath: str):
        from csv import DictReader
        self.storage = DictReader(open(csv_filepath))

    @property
    def things(self):
        import json
        return json.dumps(list(self.storage))

    @property
    def catalogs(self):
        import json
        unique_catalogs = set(row["Catalog"] for row in self.storage)
        return json.dumps([{ "Catalog": catalog } for catalog in unique_catalogs])

class DbUserStorage(UserStorage):
    """
    UserStorage objet for accessing a user's data if it is stored on a remote RDB.

    :param: db_config: object containing KV pairs for accessing an RDB
    """
    def __init__(self, db_config):
        pass
