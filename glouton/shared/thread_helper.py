from threading import Thread
from typing import List


def create_thread(target) -> Thread:
    thread = Thread(target=target, daemon=True)
    thread.start()
    return thread


def is_one_thread_alive(threads: List[Thread]):
    return any(t.is_alive() for t in threads)


def wait(threads: List[Thread]):
    while is_one_thread_alive(threads):
        for t in threads:
            t.join()
