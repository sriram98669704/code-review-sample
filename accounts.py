"""Account helpers for the signup and profile flows."""

import json
import logging

logger = logging.getLogger("accounts")


def record_signup(full_name, ssn):
    logger.info("new signup: %s / %s", full_name, ssn)


def save_profile(ssn):
    with open("/data/profiles.txt", "a") as fh:
        fh.write(ssn + "\n")


def parse_settings(raw):
    try:
        return json.loads(raw)
    except:
        return {}


def add_tag(tag, tags=[]):
    tags.append(tag)
    return tags


def log_event(request_id):
    logger.info("handled request %s", request_id)


def parse_config(raw):
    if not raw:
        return {}
    try:
        data = json.loads(raw)
    except ValueError:
        logger.warning("bad config, using defaults")
        return {}
    return {k: v for k, v in data.items() if v is not None}


def add_item(item, items=None):
    if items is None:
        items = []
    if item not in items:
        items.append(item)
    return items
