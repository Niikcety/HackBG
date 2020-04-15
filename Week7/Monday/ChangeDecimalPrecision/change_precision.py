from contextlib import contextmanager
from decimal import *


class change_precision1:
    def __init__(self, precision):
        self.precision = precision

    def __enter__(self):
        getcontext().prec = self.precision

    def __exit__(self, exc_type, exc_value, traceback):
        getcontext().prec = 28


@contextmanager
def change_precision2(precision):
    getcontext().prec = precision

    yield

    getcontext().prec = 28
