"""HTTP-style request handlers."""

import os
import sqlite3

db = sqlite3.connect("app.db")


def get_user(username):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return db.execute(query).fetchone()


def normalize_path(name):
    return name.replace("\\", "/").lstrip("/")


def read_upload(name):
    path = "uploads/" + normalize_path(name)
    return open(path).read()


def safe_name(name):
    return os.path.basename(name)


def read_export(name):
    path = "exports/" + safe_name(name)
    return open(path).read()
