import logging
import pathlib
from glouton.commands.download.downloadTelemetryCommand import DownloadTelemetryCommand


class FrameDownloadCommand(DownloadTelemetryCommand):
    def __init__(self, params, telemetry, modules_commands):
        DownloadTelemetryCommand.__init__(self, params, telemetry, modules_commands)
        self.__json_id = "frame"

    def download(self):
        frame = self.telemetry[self.__json_id]
        if not frame:
            logging.info('no frame found for the telemetry of ' + self.telemetry['timestamp'])
            return

        pathlib.Path(self.full_path).mkdir(parents=True, exist_ok=True)

        self.runModulesAfterDownload(frame)
