import logging
import time
from threading import Event
from typing import Dict, Any
from tqdm import tqdm

import requests

from glouton.domain.parameters.programCmd import ProgramCmd


class PageScanWorker:
    def __init__(self, client, cmd: ProgramCmd, repos, path, url_params: Dict[str, str], end_signal: Event):
        self.client = client
        self.cmd: ProgramCmd = cmd
        self.repos = repos
        self.path = path
        self.url_params: Dict[str, str] = url_params
        self.end_signal: Event = end_signal

    def scan(self) -> None:
        logging.info(f"Scanning page {self.url_params['Link']}...")

        max_retries: int = 3
        for attempt in range(0, max_retries):
            try:
                response: requests.Response = self._make_request()
                data: Dict[str, Any] = response.json()
                self._process_data(data)
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 429:
                    self._handle_rate_limit(e)
                else:
                    logging.error(f"HTTP error: {e}, response_info: {e.response.json()}")
                    self.end_signal.set()
            except Exception as e:
                logging.error(f"Error processing data: {e}")
                self.end_signal.set()

    def scan_page(self, page: int) -> None:
        self.url_params['page'] = str(page)
        self.scan()

    def scan_page_for_obs(self, page: int) -> None:
        self.url_params['page'] = str(page)
        self.url_params['Link'] = self.url_params.pop('page')
        self.scan()

    def _make_request(self) -> requests.Response:
        response = self.client.get_from_base(self.path, self.url_params)
        response.raise_for_status()
        return response

    @staticmethod
    def _handle_rate_limit(error: requests.exceptions.HTTPError) -> None:
        default_retry_delay_seconds: int = 10

        try:
            # typical response: "detail": "Request was throttled. Expected available in N seconds."
            # So we are extracting the number of seconds from the string of "detail"
            retry_after: int = int(error.response.json().get("detail").split(" in ")[-1].split(" seconds")[0])
            logging.warning(f"Rate limit reached. Retrying in {retry_after} seconds.")
            for _ in tqdm(range(retry_after), desc="Waiting"):
                time.sleep(1)
        except Exception as extraction_error:
            logging.warning(f"Failed to extract retry-after time: {extraction_error}")
            logging.warning(f"Using default retry delay of {default_retry_delay_seconds} seconds.")
            time.sleep(default_retry_delay_seconds)

    def _process_data(self, elements: Dict[str, Any]) -> None:
        logging.info(f"Incoming data: {elements}")
        for element in elements:
            for repo in self.repos:
                repo.register_download_command(element, self.cmd.start_date, self.cmd.end_date)
