import os


def create_dir_if_not_exist(directory):
    os.makedirs(directory, exist_ok=True)
