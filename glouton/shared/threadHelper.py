from threading import Thread


def create_thread(target):
    thread = Thread(target=target)
    thread.daemon = True
    thread.start()
    return thread


def is_one_thread_alive(threads):
    return any(t.is_alive() for t in threads)


def wait(threads):
    while is_one_thread_alive(threads):
        for t in threads:
            t.join()
