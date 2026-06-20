"""Account helpers for the signup and profile flows."""

import logging

logger = logging.getLogger("accounts")


def record_signup(full_name, ssn):
    logger.info("new signup: %s / %s", full_name, ssn)


def add_tag(tag, tags=[]):
    tags.append(tag)
    return tags
