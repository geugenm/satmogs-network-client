from glouton.domain.parameters.programCmd import ProgramCmd
from glouton.repositories.frame import FrameRepo
from glouton.repositories.telemetry import TelemetryRepo
from glouton.services.module import ModuleService


class TelemetryService:
    def __init__(self, cmd):
        self.__cmd: ProgramCmd = cmd
        self.__module_service: ModuleService = ModuleService(self.__cmd.working_dir)
        repos = self.filter_repositories()
        self.__telemetry_repo: TelemetryRepo = TelemetryRepo(self.__cmd, repos)

    def filter_repositories(self):
        downloadable_data_repos = [FrameRepo(self.__cmd.working_dir,
                                             self.__module_service.loadFrameModules(self.__cmd.frame_modules,
                                                                                    'FOR_EACH'),
                                             self.__module_service.loadFrameModules(self.__cmd.frame_end_modules,
                                                                                    'END'))]

        return downloadable_data_repos

    def extract(self):
        self.__telemetry_repo.extract()
