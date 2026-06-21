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
    # NO parameters AND a PLAIN module global (not a recognised taint source like
    # os.environ/input()), so the walk has nothing to seed from and skips it -> the
    # finding is KEPT; the agent's read_function can still open guard_current itself.
    target = CURRENT_REQUEST.get("path", "")
    safe = guard_current(target)
    return open("current/" + safe).read()


def guard_current(value):
    return os.path.basename(value)


def read_env_file():
    # NO parameters: the path comes from an environment variable. os.environ is a
    # known taint SOURCE, so the walk seeds from it, follows the chain into guard_env,
    # reaches os.path.basename, and DROPS the finding.
    target = os.environ.get("EXPORT_PATH", "")
    safe = guard_env(target)
    return open("exports/" + safe).read()


def guard_env(value):
    return os.path.basename(value)


def read_stdin_file():
    # NO parameters: the path is read from stdin via input(), a known taint SOURCE, so
    # the walk seeds from it, follows guard_stdin to os.path.basename, and DROPS it.
    target = input("path? ")
    safe = guard_stdin(target)
    return open("inbox/" + safe).read()


def guard_stdin(value):
    return os.path.basename(value)
