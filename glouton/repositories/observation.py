from threading import Event

from glouton.infrastructure.satnogNetworkClient import SatnogNetworkClient
from glouton.shared import thread_helper
from glouton.workers.page_scan import PageScanWorker


class ObservationRepo:
    def __init__(self, cmd, repos):
        self.OBSERVATION_URL = 'observations/'
        self.__repos = repos
        self.__cmd = cmd
        self.__threads = []

    def extract(self):
        client: SatnogNetworkClient = SatnogNetworkClient()
        page_counter: int = 0
        end_signal: Event = Event()

        page_scanner = PageScanWorker(
            client, self.__cmd, self.__repos, self.OBSERVATION_URL, self.__url_param_builder(page_counter), end_signal)

        while True:
            page_scanner.scan_page_for_obs(page_counter)
            if end_signal.is_set():
                break

            page_counter += 1
            print("\ndownloading started (Ctrl + C to stop)...\t~(  ^o^)~")
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
