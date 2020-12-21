from csv import DictReader
from config import Config
from util.user_storage import UserStorage, CsvUserStorage

UUID_NIL = "00000000-0000-0000-0000-000000000000"

class UserStorageNotFoundException(Exception):
    def __str__(self):
        return "Could not find user storage config."

class UserStorageConfig:
    """
    Stub static class representing a set of types that user's storage configuration can take.
    """
    CSV = "CSV"
    RDB = "RDB"

def get_user_storage_config(user_id: str) -> str:
    """
    Stub method.

    Always returns "csv" for purposes of coding challenge.
    """
    return UserStorageConfig.CSV

def get_user_db_storage_secret(user_id: str):
    """
    Stub method.

    Invokes some API to get the config for accessing the user's remote RDB.
    """
    pass

def get_user_csv_storage_filepath(user_id: str) -> str:
    """
    Stub method.

    Always returns the preconfigured CSV filepath.
    """
    return Config.DB_CSV_FILEPATH

def get_user_storage(user_id: str) -> UserStorage:
    """
    Returns a UserStorage object for some user's user storage configuration, be it CSV or RDB.

    :raises: UserStorageNotFoundException
    """
    user_storage_config = get_user_storage_config(user_id)

    if user_storage_config == UserStorageConfig.CSV:
        csv_storage_filepath = get_user_csv_storage_filepath(user_id)
        return CsvUserStorage(csv_storage_filepath)

    elif user_storage_config == UserStorageConfig.RDB:
        db_config = get_user_db_storage_secret(user_id)
        return DbUserStorage(db_config)

    else:
        raise UserStorageNotFoundException

def handle_auth(request_obj) -> str:
    """
    Stub method.

    Sends auth info to auth server. Auth server will return the UUID of the user.

    :returns: str: UUID of authenticated user
    """
    return UUID_NIL
