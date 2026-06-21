"""HTTP-style request handlers."""

import os
import sqlite3

from paths import scrub_invoice, clip_manifest, pass_archive

db = sqlite3.connect("app.db")

# Populated by the framework before each request is dispatched.
CURRENT_REQUEST = {}


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


def route_invoice(value):
    # middle hop of fetch_invoice's a -> b -> c chain (downloads -> api -> paths)
    return scrub_invoice(value)


def fetch_manifest(manifest_name):
    # a -> a -> b: hops within this file (tidy_manifest) first, then out to paths.py
    safe = tidy_manifest(manifest_name)
    return open("manifests/" + safe).read()


def tidy_manifest(value):
    return clip_manifest(value)


def relay_archive(value):
    # hop 1 of the four-hop (depth-4) chain
    return pass_archive(value)


def serve_current():
    # NO parameters: user input arrives through a module global, not an argument, so
    # taint cannot be seeded from a parameter and the deterministic chain-walk skips it.
    target = CURRENT_REQUEST.get("path", "")
    safe = guard_current(target)
    return open("current/" + safe).read()


def guard_current(value):
    return os.path.basename(value)
