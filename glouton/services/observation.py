from typing import List

from glouton.domain.interfaces.downloadable import Downloadable
from glouton.domain.parameters.programCmd import ProgramCmd
from glouton.repositories.archive import ArchiveRepo
from glouton.repositories.demoddata import DemoddataRepo
from glouton.repositories.observation import ObservationRepo
from glouton.repositories.waterfall import WaterfallRepo
from glouton.services.module import ModuleService


class ObservationsService:

    def __init__(self, cmd: ProgramCmd) -> None:
        self._cmd = cmd
        self._module_service = ModuleService(cmd.working_dir)
        self._observations_repo = ObservationRepo(
            cmd, self._filter_repositories()
        )

    def _filter_repositories(self) -> List[Downloadable]:
        downloadable_data_repos: List[Downloadable] = []
        all_repos = (
            not self._cmd.archives
            and not self._cmd.waterfalls
            and not self._cmd.demoddata
        )

        if all_repos or self._cmd.archives:
            downloadable_data_repos.append(
                ArchiveRepo(
                    self._cmd.working_dir,
                    self._module_service.loadArchiveModules(
                        self._cmd.archive_modules, "FOR_EACH"
                    ),
                    self._module_service.loadArchiveModules(
                        self._cmd.archive_end_modules, "END"
                    ),
                )
            )
        if all_repos or self._cmd.waterfalls:
            downloadable_data_repos.append(
                WaterfallRepo(
                    self._cmd.working_dir,
                    self._module_service.loadWaterfallModules(
                        self._cmd.waterfall_modules, "FOR_EACH"
                    ),
                    self._module_service.loadWaterfallModules(
                        self._cmd.waterfall_end_modules, "END"
                    ),
                )
            )
        if all_repos or self._cmd.demoddata:
            downloadable_data_repos.append(
                DemoddataRepo(
                    self._cmd.working_dir,
                    self._module_service.loadDemoddataModules(
                        self._cmd.demoddata_modules, "FOR_EACH"
                    ),
                    self._module_service.loadDemoddataModules(
                        self._cmd.demoddata_end_modules, "END"
                    ),
                )
            )

        return downloadable_data_repos

    def extract(self) -> None:
        self._observations_repo.extract()