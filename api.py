"""HTTP-style request handlers."""

import sqlite3

import requests

db = sqlite3.connect("app.db")


def delete_account(user_id):
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
