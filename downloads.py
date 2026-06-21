"""File-download request handlers. Each builds a path from user input through a
helper that lives in another file (paths.py), two hops from the actual fix."""

from paths import build_safe_path, to_relative


def fetch_report(report_name):
    path = build_safe_path(report_name)
    return open(path).read()


def fetch_avatar(avatar_name):
    path = to_relative(avatar_name)
    return open("avatars/" + path).read()
