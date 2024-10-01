import logging
from threading import Event
from threading import Thread
from typing import List, Dict

from glouton.domain.parameters.programCmd import ProgramCmd
from glouton.infrastructure.satnogDbClient import SatnogDbClient
from glouton.shared import thread_helper
from glouton.workers.page_scan import PageScanWorker


class TelemetryRepo:
    TELEMETRY_URL = 'telemetry/'

    def __init__(self, cmd: ProgramCmd, repos):
        self.__repos = repos
        self.__cmd: ProgramCmd = cmd
        self.__threads: List[Thread] = []

    def extract(self):
        client: SatnogDbClient = SatnogDbClient()
        end_signal: Event = Event()

        page_counter: int = 0

        threads: List[Thread] = []

        while True:
            for p in range(1, 5):
                page: int = page_counter + p
                page_scanner: PageScanWorker = PageScanWorker(
                    client,
                    self.__cmd,
                    self.__repos,
                    self.TELEMETRY_URL,
                    self.__url_param_builder(page),
                    end_signal,
                )
                thread: Thread = thread_helper.create_thread(page_scanner.scan)
                threads.append(thread)

            thread_helper.wait(threads)
            if end_signal.is_set():
                break

            page_counter += 4

        logging.info("Telemetry data extraction complete. Starting downloads.")
        self.__register_end_command()
        self.__create_workers_and_wait()

    def __register_end_command(self) -> None:
        for repo in self.__repos:
            repo.register_end_command(
                self.__cmd.start_date, self.__cmd.end_date)

    def __create_workers_and_wait(self) -> None:
        for repo in self.__repos:
            self.__threads.extend(repo.create_worker())
        thread_helper.wait(self.__threads)

    def __url_param_builder(self, page: int) -> Dict[str, str]:
        return {
            "satellite": self.__cmd.norad_id,
            "start": self.__cmd.start_date.isoformat(),
            "end": self.__cmd.end_date.isoformat(),
            "observer": self.__cmd.observer,
            "transmitter": self.__cmd.transmitter,
            "app_source": self.__cmd.app_source,
            "page": str(page),
            "format": "json",
        }
