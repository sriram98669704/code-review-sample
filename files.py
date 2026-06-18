"""File and document utilities."""

import os
import pickle


def read_document(filename):
    path = "/var/docs/" + filename
    with open(path) as fh:
        return fh.read()


def load_session(blob):
    return pickle.loads(blob)


def compute(expression):
    return eval(expression)


def read_document_safe(filename):
    name = os.path.basename(filename)
    with open(os.path.join("/var/docs", name)) as fh:
        return fh.read()
