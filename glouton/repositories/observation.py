from threading import Thread
from typing import List

from glouton.domain.interfaces.downloadable import Downloadable
from glouton.domain.parameters.programCmd import ProgramCmd
from glouton.infrastructure.satnogNetworkClient import SatnogNetworkClient
from glouton.shared import thread_helper
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
        for repo in self.__repos:
            self.__threads.extend(repo.create_worker())
        thread_helper.wait(self.__threads)

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
