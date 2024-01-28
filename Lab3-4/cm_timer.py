from time import time, sleep
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.start_time = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.res_time = time() - self.start_time
        print("time: {:.3}".format(self.res_time))


@contextmanager
def cm_timer_2():
    start_time = time()
    try:
        yield
    finally:
        delta_time = time() - start_time
        print("time: {:.3}".format(delta_time))


if __name__ == '__main__':
    with cm_timer_1():
        sleep(2.1)

    with cm_timer_2():
        sleep(2.1)