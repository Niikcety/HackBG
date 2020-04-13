from contextlib import contextmanager
import time


class measure_performance():
    def __init__(self):
        self.time_start = time.time()
        self.last_time = time.time()
        self.benchmark_number = 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f'Finished for: {time.time() - self.time_start}')

    def benchmark(self, text=None, restart=False):
        if restart is False and text is not None:
            print(f'{text}: {time.time() - self.last_time}')
        elif restart is True and text is not None:
            print(f'{text}: {time.time() - self.last_time}')
            self.last_time = time.time()
        elif restart is True and text is None:
            print(f'Benchmark #{self.benchmark_number}: {time.time() - self.last_time}')
            self.last_time = time.time()
        else:
            print(f'Benchmark #{self.benchmark_number} : {time.time() - self.last_time}')
        self.benchmark_number += 1
