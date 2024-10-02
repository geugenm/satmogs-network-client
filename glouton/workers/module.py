import logging
import threading
from queue import Queue

from glouton.commands.module.moduleCommand import ModuleCommand


class ModuleWorker:
    def __init__(
        self,
        queue: Queue[ModuleCommand],
        download_status: threading.Event,
        is_download_finished: threading.Event,
    ) -> None:
        self._commands: Queue[ModuleCommand] = queue
        self._download_status: threading.Event = download_status
        self._is_download_finished: threading.Event = is_download_finished

    def execute(self) -> None:
        while not self._commands.empty() or self._download_status.is_set():
            try:
                command: ModuleCommand = self._commands.get(block=True, timeout=1)
                command.process()
                self._commands.task_done()
            except Exception as ex:
                logging.error(f"Error processing module command: {ex}")

        self._is_download_finished.set()