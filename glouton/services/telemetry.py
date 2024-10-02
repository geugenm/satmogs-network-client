from glouton.domain.parameters.program_cmd import ProgramCmd
from glouton.repositories.frame import FrameRepo
from glouton.repositories.telemetry import TelemetryRepo
from glouton.services.module import ModuleService


class TelemetryService:
    def __init__(self, cmd: ProgramCmd) -> None:
        self._cmd: ProgramCmd = cmd
        self._module_service: ModuleService = ModuleService(cmd.working_dir)

        frame_repo: FrameRepo = FrameRepo(
            cmd.working_dir,
            self._module_service.loadFrameModules(
                cmd.frame_modules, "FOR_EACH"
            ),
            self._module_service.loadFrameModules(
                cmd.frame_end_modules, "END"
            ),
        )

        self._telemetry_repo: TelemetryRepo = TelemetryRepo(cmd, [frame_repo])

    def extract(self) -> None:
        self._telemetry_repo.extract()