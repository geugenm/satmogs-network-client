from glouton.commands.download.downloadObservationCommand import (
    DownloadObservationCommand,
)
from glouton.shared import fileHelper
from glouton.shared.logger import logger
import os
import ntpath
import requests


class DemoddataDownloadCommand(DownloadObservationCommand):
    def __init__(self, params, observation, modules_commands):
        DownloadObservationCommand.__init__(self, params, observation, modules_commands)
        self.__json_id = "demoddata"

    def download(self):
        demoddata = self.observation[self.__json_id]
        if not any(demoddata):
            logger.Info(
                "no demoddata found for the observation "
                + str(self.observation["id"])
                + " of "
                + self.observation["start"]
            )
            return

        os.makedirs(self.full_path, exist_ok=True)

        for demod in demoddata:
            url = demod["payload_demod"]
            file_name = ntpath.basename(url)
            full_path_file = os.path.join(self.full_path, file_name)

            if os.path.exists(full_path_file):
                logger.Warning("pass " + file_name + "... file already exist")
                return

            response = self.client.get(url)
            if response.status_code == 200:
                logger.Info("downloading..." + file_name)
                with open(full_path_file, "wb") as file:
                    file.write(response.content)
                self.runModulesAfterDownload(file_name)
