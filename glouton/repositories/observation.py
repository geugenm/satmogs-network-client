import logging
from threading import Thread
from typing import List

from glouton.repositories.downloadable import Downloadable
from glouton.domain.parameters.program_cmd import ProgramCmd
from glouton.clients.satnog_network import SatnogNetworkClient
from glouton.workers.page_scan import PageScanWorker


class ObservationRepo:
    def __init__(self, cmd: ProgramCmd, repos: List[Downloadable]):
        self.OBSERVATION_URL: str = 'observations/'
        self.__repos: List[Downloadable] = repos
        self.__cmd: ProgramCmd = cmd
        self.__threads: List[Thread] = []

    def extract(self):
        client: SatnogNetworkClient = SatnogNetworkClient()
        page_counter: int = 0

        page_scanner: PageScanWorker = PageScanWorker(
            client, self.__cmd, self.__repos, self.OBSERVATION_URL, self.__url_param_builder(page_counter))

        while True:
            page_scanner.scan_page_for_obs(page_counter)

            page_counter += 1
            self.__register_end_command()
            self.__create_workers_and_wait()

    def __register_end_command(self):
        for repo in self.__repos:
            repo.register_end_command(
                self.__cmd.start_date, self.__cmd.end_date)

    def __create_workers_and_wait(self):
        self.__threads.clear()

        for repo in self.__repos:
            workers = repo.create_worker()
            for worker in workers:
                if not worker.is_alive():
                    worker.start()
                    self.__threads.append(worker)

        for thread in self.__threads:
            try:
                thread.join()
            except Exception as ex:
                logging.error(f"Error joining thread: {ex}")

    def __url_param_builder(self, page):
        return {'satellite__norad_cat_id': self.__cmd.norad_id,
                'ground_station': self.__cmd.ground_station_id,
                'start': self.__cmd.start_date.isoformat(),
                'end': self.__cmd.end_date.isoformat(),
                'status': self.__cmd.observation_status,
                'vetted_user': self.__cmd.user,
                'transmitter_uuid': self.__cmd.transmitter_uuid,
                'transmitter_mode': self.__cmd.transmitter_mode,
                'transmitter_type': self.__cmd.transmitter_type,
                'page': str(page),
                'format': 'json'}
