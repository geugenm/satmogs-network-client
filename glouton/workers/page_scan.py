import logging

import time
from typing import Dict, Any

import requests

from glouton.domain.parameters.programCmd import ProgramCmd


class PageScanWorker:

    def __init__(self, client, cmd: ProgramCmd, repos, path, url_params, job_number, end_signal):
        self.client = client
        self.cmd: ProgramCmd = cmd
        self.repos = repos
        self.path = path
        self.url_params = url_params
        self.job_number = job_number
        self.end_signal = end_signal

    def scan(self) -> None:
        params = self.url_params
        job_string = f"Job {self.job_number}"
        logging.info(f"{job_string} scanning page {params['page']}...")

        max_retries: int = 3
        retry_delay_sec: int = 10

        for attempt in range(1, max_retries + 1):
            try:
                response: requests.Response = self.client.get_from_base(self.path, params)
                response.raise_for_status()
                data = response.json()
                self._process_data(data)
                return
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 429:  # Check for rate limiting (429 Too Many Requests)
                    logging.warning(
                        f"{job_string}: Rate limit reached. Retrying in {retry_delay_sec} seconds (attempt {attempt}/{max_retries})")
                    time.sleep(retry_delay_sec)
                else:
                    logging.error(f"{job_string}: HTTP error: {e}")
                    self.end_signal.set()
                    return
            except Exception as e:
                logging.error(f"{job_string}: Error processing data: {e}")
                self.end_signal.set()
                return

    def _process_data(self, elements: Dict[str, Any]) -> None:
        for element in elements:
            for repo in self.repos:
                repo.register_download_command(
                    element, self.cmd.start_date, self.cmd.end_date
                )
