import logging
import ntpath
import os

from glouton.commands.download.downloadObservationCommand import (
    DownloadObservationCommand,
)


class ArchiveDownloadCommand(DownloadObservationCommand):
    def __init__(self, params, observation, modules_commands):
        DownloadObservationCommand.__init__(self, params, observation, modules_commands)
        self.__json_id = "payload"
        if observation["archived"] is True:
            self.__json_id = "archive_url"

    def download(self):
        url = self.observation[self.__json_id]
        if not url:
            logging.info(
                f"No archive found for observation {self.observation['id']} ({self.observation['start']})"
            )
            return

        os.makedirs(self.full_path, exist_ok=True)
        file_name = ntpath.basename(url)
        full_path_file = os.path.join(self.full_path, file_name)

        if os.path.exists(full_path_file):
            logging.warning("pass " + file_name + "... file already exist")
            return

        response = self.client.get(url)
        if response.status_code == 200:
            logging.info(f"Downloading archive... {file_name}")
            with open(full_path_file, "wb") as file:
                file.write(response.content)
            self.runModulesAfterDownload(file_name)
