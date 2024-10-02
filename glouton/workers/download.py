import logging
import threading
from queue import Queue
from typing import Optional

from glouton.commands.download.downloadCommand import DownloadCommand


class DownloadWorker:
    def __init__(
            self,
            queue: "Queue[DownloadCommand]",
            download_status: threading.Event,
            is_download_finished: Optional[threading.Event] = None,
    ) -> None:

        self._commands = queue
        self._download_status = download_status
        self._is_download_finished = is_download_finished

    def execute(self) -> None:
        self._download_status.set()
        try:
            while command := self._commands.get():
                logging.info(
                    f"Downloading {command.full_path}..."
                )
                command.download()
                self._commands.task_done()
        except Exception as ex:
            logging.error(f"Error while downloading: {ex}")
        finally:
            self._download_status.clear()
            if self._is_download_finished:
                self._is_download_finished.set()
