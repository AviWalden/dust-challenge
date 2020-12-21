import json
import random
import uuid
from flask import Flask, request
from flask_cors import CORS
from csv import DictReader

from util import UserStorageNotFoundException, handle_auth, get_user_storage

app = Flask(__name__)
CORS(app)

@app.route("/catalogs")
def catalogs():
    """
    Gets all unique catalogs for a user.

    :returns: list<dict>
    """
    user_id = handle_auth(request)

    try:
        user_storage = get_user_storage(user_id)
        return user_storage.catalogs

    except UserStorageNotFoundException:
        return str(UserStorageNotFoundException)

@app.route("/things")
def things():
    """
    Gets all things for a user.

    :returns: list<dict>
    """
    user_id = handle_auth(request)

    try:
        user_storage = get_user_storage(user_id)
        return user_storage.things

    except UserStorageNotFoundException:
        return str(UserStorageNotFoundException)
