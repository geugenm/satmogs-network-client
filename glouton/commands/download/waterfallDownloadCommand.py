import logging
import ntpath
import os
import pathlib

from glouton.commands.download.downloadObservationCommand import DownloadObservationCommand


class WaterfallDownloadCommand(DownloadObservationCommand):
    def __init__(self, params, observation, modules_commands):
        DownloadObservationCommand.__init__(self, params, observation, modules_commands)
        self.__json_id = "waterfall"

    def download(self):
        url = self.observation[self.__json_id]
        if not url:
            logging.info(
                'no waterfall found for the observation ' + str(self.observation['id']) + ' of ' + self.observation[
                    'start'])
            return

        pathlib.Path(self.full_path).mkdir(parents=True, exist_ok=True)
        file_name = ntpath.basename(url)
        full_path_file = self.full_path + os.path.sep + file_name
        if os.path.exists(full_path_file):
            logging.warning('pass ' + file_name + '... file already exist')
            return

        r = self.client.get(url)
        if r.status_code == 200:
            logging.info('downloading...' + file_name)
            with open(full_path_file, "wb") as file:
                file.write(r.content)
            self.runModulesAfterDownload(file_name)
