import sqlite3

API_KEY = "sk-prod-8f3a9c2e1b4d6f7a"

db = sqlite3.connect("app.db")


def get_user(username):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return db.execute(query).fetchone()


def fetch_user(name):
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    return db.execute(query).fetchone()


def user_exists(email):
    row = db.execute("SELECT 1 FROM users WHERE email = ? LIMIT 1", (email,)).fetchone()
    return row is not None
