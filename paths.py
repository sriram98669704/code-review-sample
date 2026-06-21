"""Path helpers shared by the download handlers (a separate module on purpose:
the real fix lives one file away from the code that gets flagged)."""

import os

from db import hold_archive


def build_safe_path(name):
    cleaned = strip_traversal(name)
    return "reports/" + cleaned


def strip_traversal(value):
    return os.path.basename(value)


def to_relative(value):
    return collapse_slashes(value)


def collapse_slashes(text):
    return text.replace("//", "/")


def scrub_invoice(value):
    # depth-3 chain: fetch_invoice -> route_invoice -> scrub_invoice -> seal_invoice
    return seal_invoice(value)


def seal_invoice(value):
    return os.path.basename(value)


def clip_manifest(value):
    return os.path.basename(value)


def pass_archive(value):
    # hop 2 of the four-hop chain -> continues into db.py
    return hold_archive(value)
