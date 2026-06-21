"""File-download request handlers. Each builds a path from user input through a
helper that lives in another file (paths.py), two hops from the actual fix."""

from paths import build_safe_path, to_relative
from api import route_invoice, relay_archive


def fetch_report(report_name):
    path = build_safe_path(report_name)
    return open(path).read()


def fetch_avatar(avatar_name):
    path = to_relative(avatar_name)
    return open("avatars/" + path).read()


def fetch_invoice(invoice_name):
    # a -> b -> c across three files: the fix (basename) sits three hops deep in paths.py
    safe = route_invoice(invoice_name)
    return open("invoices/" + safe).read()


def fetch_archive(archive_name):
    # four-hop chain: the fix sits one hop BEYOND the triage depth bound, so it stays flagged
    safe = relay_archive(archive_name)
    return open("archive/" + safe).read()
