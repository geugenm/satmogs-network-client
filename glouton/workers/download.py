import logging
from queue import Queue

from glouton.commands.download.downloadCommand import DownloadCommand


class DownloadWorker:
    def __init__(self, queue, download_status, is_download_finished):
        self._commands = queue
        self.__download_status = download_status
        self.__is_download_finished = is_download_finished

    def execute(self):
        self.__download_status.set()
        try:
            while command := self._commands.get():
                logging.info(f"Downloading {command.full_path}, type: {type(command)}")
                command.download()
                self._commands.task_done()

        except Exception as ex:
            logging.error(f"Error while downloading: {ex}")

        finally:
            self.__download_status.clear()
            if self.__is_download_finished is not None:
                self.__is_download_finished.set()
