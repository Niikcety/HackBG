from contextlib import contextmanager


class silence_exception1:

    def __init__(self, error, text=None):
        self.error = error
        if text is not None:
            self.text = text
        else:
            self.text = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == self.error:
            if self.text is not None and exc_value == self.text:
                return True
            elif self.text is None:
                return True
            else:
                return False
        else:
            return False


@contextmanager
def silence_exception2(error, text=None):
    try:
        yield
    except error as exc:
        if text is not None and str(exc) != text:
            raise exc
