"""Payment and receipt helpers."""

import hashlib
import os

import requests


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def export_receipt(order_id):
    os.system(f"cp /receipts/{order_id}.pdf /tmp/export/")


def charge(amount, token):
    resp = requests.post(
        "https://payments.internal/charge",
        json={"amount": amount, "token": token},
        verify=False,
    )
    return resp.status_code == 200


def hash_password_secure(password, salt):
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100_000).hex()
