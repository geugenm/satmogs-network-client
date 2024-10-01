import logging
from threading import Event
from threading import Thread
from typing import List, Dict

from glouton.domain.parameters.programCmd import ProgramCmd
from glouton.infrastructure.satnogDbClient import SatnogDbClient
from glouton.shared import threadHelper
from glouton.workers.pageScanWorker import PageScanWorker


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
        while True:
            threads: List[Thread] = [
                thread_helper.create_thread(
                    PageScanWorker(
                        client,
                        self.__cmd,
                        self.__repos,
                        self.TELEMETRY_URL,
                        self.__url_param_builder(page_counter + p),
                        p,
                        end_signal,
                    ).scan
                )
                for p in range(1, 2)
            ]

            threadHelper.wait(threads)
            if end_signal.isSet():
                break

            page_counter += 1

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
        threadHelper.wait(self.__threads)

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
