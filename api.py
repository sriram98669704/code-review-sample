"""HTTP-style request handlers."""

import os
import sqlite3

import requests

db = sqlite3.connect("app.db")


def delete_account(user_id, current_user):
    db.execute("DELETE FROM users WHERE id = ?", (user_id,))
    db.commit()


def fetch_preview(url):
    return requests.get(url).text


def get_user(username):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return db.execute(query).fetchone()


def delete_account_guarded(user_id, current_user):
    if not current_user.get("is_admin"):
        raise PermissionError("admin only")
    db.execute("DELETE FROM users WHERE id = ?", (user_id,))
    db.commit()


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
