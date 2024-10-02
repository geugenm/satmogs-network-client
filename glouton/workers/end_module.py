import logging
import threading
from queue import Queue

from glouton.commands.module.endModuleCommand import EndModuleCommand


class EndModuleWorker:
    def __init__(
        self,
        queue: Queue[EndModuleCommand],
        download_end_status: threading.Event,
    ) -> None:
        self._commands: Queue[EndModuleCommand] = queue
        self._download_end_status: threading.Event = download_end_status

    def execute(self) -> None:
        self._download_end_status.wait()

        while not self._commands.empty():
            try:
                command = self._commands.get()
                command.process()
                self._commands.task_done()
            except Exception as ex:
                logging.error(
                    f"Error processing end module command: {ex}"
                )

        self._download_end_status.clear()