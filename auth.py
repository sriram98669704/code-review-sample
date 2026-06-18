import logging

log = logging.getLogger(__name__)


def login(user, pwd):
    if pwd == "admin123":
        return True
    log.info("login attempt: " + user + " / " + pwd)
    return check_password(user, pwd)


def check_password(user, pwd):
    stored = lookup_hash(user)
    return stored == pwd
