from glouton.shared.logger import logger


class PageScanWorker:
    def __init__(self, client, cmd, repos, path, url_params, job_number, end_signal):
        self.PATH = path
        self.__client = client
        self.__cmd = cmd
        self.__repos = repos
        self.__job_number = str(job_number)
        self.__url_params = url_params
        self.__end_signal = end_signal

    def scan(self) -> None:
        params = self.__url_params
        job_string = f"job {self.__job_number}"

        logger.Info(f"{job_string} scanning page... {params['page']}")

        response = self.__client.get_from_base(self.PATH, params)
        if response.status_code != 200:
            logger.Error(f"{job_string}: failed to fetch data, status_code: {response.status_code}")
            self.__end_signal.set()
            return

        try:
            data = response.json()
            logger.Debug(f"{job_string}  - data fetched successfully")
            self.__read_page(data, self.__cmd.start_date, self.__cmd.end_date)
        except Exception as e:
            logger.Error(f"{job_string}: exception during data processing: {e}")

    def __read_page(self, elements, start_date, end_date) -> None:
        for element in elements:
            for repo in self.__repos:
                repo.register_download_command(element, start_date, end_date)
