"""Path helpers shared by the download handlers (a separate module on purpose:
the real fix lives one file away from the code that gets flagged)."""

import os


def build_safe_path(name):
    cleaned = strip_traversal(name)
    return "reports/" + cleaned


def strip_traversal(value):
    return os.path.basename(value)


def to_relative(value):
    return collapse_slashes(value)


def collapse_slashes(text):
    return text.replace("//", "/")
