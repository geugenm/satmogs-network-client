import os
from queue import Queue
from threading import Event, Thread
from typing import List

from glouton.commands.download.downloadCommandParams import DownloadCommandParams
from glouton.commands.download.frameDownloadCommand import FrameDownloadCommand
from glouton.commands.module.endModuleCommand import EndModuleCommand
from glouton.commands.module.endModuleCommandParams import EndModuleCommandParams
from glouton.domain.interfaces.downloadable import Downloadable
from glouton.shared import thread_helper
from glouton.workers.download import DownloadWorker
from glouton.workers.end_module import EndModuleWorker
from glouton.workers.module import ModuleWorker


class FrameRepo(Downloadable):
    def __init__(self, working_dir, modules, end_modules):
        self.__working_dir = working_dir
        self.__frame_commands = Queue()
        self.__frame_modules_commands = Queue()
        self.__frame_end_modules_commands = Queue()
        self.__modules = modules
        self.__end_modules = end_modules
        self.__download_status = Event()
        self.__download_end_status = Event()

    def register_download_command(self, telemetry, start_date, end_date):
        cmd_parameters = DownloadCommandParams(
            self.__working_dir, self.__create_dir_name('frames', start_date, end_date), self.__modules)
        waterfallDownloadCommand = FrameDownloadCommand(
            cmd_parameters, telemetry, self.__frame_modules_commands)
        self.__frame_commands.put(waterfallDownloadCommand)

    def register_end_command(self, start_date, end_date):
        if self.__end_modules is not None:
            dir_name = self.__create_dir_name('frames', start_date, end_date)
            module_parameters = EndModuleCommandParams(full_path=os.path.join(
                self.__working_dir, dir_name), modules=self.__end_modules)
            frame_end_module_command = EndModuleCommand(
                module_parameters)
            self.__frame_end_modules_commands.put(frame_end_module_command)

    def create_worker(self):
        threads: List[Thread] = []
        download_worker: DownloadWorker = DownloadWorker(
            self.__frame_commands, self.__download_status, None)
        threads.append(thread_helper.create_thread(download_worker.execute))
        if self.__modules is not None:
            module_worker: ModuleWorker = ModuleWorker(
                self.__frame_modules_commands, self.__download_status, self.__download_end_status)
            threads.append(thread_helper.create_thread(module_worker.execute))

        if self.__end_modules is not None:
            end_worker: EndModuleWorker = EndModuleWorker(
                self.__frame_end_modules_commands, self.__download_end_status)
            threads.append(thread_helper.create_thread(end_worker.execute()))

        return threads

    def __create_dir_name(self, target, start_date, end_date):
        return target + '__' + start_date.strftime('%Y-%m-%dT%H-%M-%S') + '__' + end_date.strftime('%Y-%m-%dT%H-%M-%S')
