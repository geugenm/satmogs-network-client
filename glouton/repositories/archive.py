import os
from queue import Queue
from threading import Event, Thread
from typing import List

from glouton.commands.download.archiveDownloadCommand import ArchiveDownloadCommand
from glouton.commands.download.downloadCommandParams import DownloadCommandParams
from glouton.commands.module.endModuleCommand import EndModuleCommand
from glouton.commands.module.endModuleCommandParams import EndModuleCommandParams
from glouton.repositories.downloadable import Downloadable
from glouton.shared import thread_helper
from glouton.workers.download import DownloadWorker
from glouton.workers.end_module import EndModuleWorker
from glouton.workers.module import ModuleWorker


class ArchiveRepo(Downloadable):
    def __init__(self, working_dir, modules, end_modules):
        self.__working_dir = working_dir
        self.__archive_commands = Queue()
        self.__archive_modules_commands = Queue()
        self.__archive_end_modules_commands = Queue()
        self.__modules = modules
        self.__end_modules = end_modules
        self.__download_status = Event()
        self.__is_download_finished = Event()

    def register_download_command(self, observation, start_date, end_date):
        cmd_parameters = DownloadCommandParams(
            self.__working_dir, self.__create_dir_name('archive', start_date, end_date), self.__modules)
        waterfallDownloadCommand = ArchiveDownloadCommand(
            cmd_parameters, observation, self.__archive_modules_commands)
        self.__archive_commands.put(waterfallDownloadCommand)

    def register_end_command(self, start_date, end_date):
        if self.__end_modules is not None:
            dir_name = self.__create_dir_name('archive', start_date, end_date)
            module_parameters = EndModuleCommandParams(full_path=os.path.join(
                self.__working_dir, dir_name), modules=self.__end_modules)
            archive_end_module_command = EndModuleCommand(
                module_parameters)
            self.__archive_end_modules_commands.put(archive_end_module_command)

    def create_worker(self) -> List[Thread]:
        threads = []
        downloadWorker = DownloadWorker(
            self.__archive_commands, self.__download_status,
            self.__is_download_finished if self.__modules is None else None)
        threads.append(thread_helper.create_thread(downloadWorker.execute))
        if self.__modules is not None:
            moduleWorker = ModuleWorker(
                self.__archive_modules_commands, self.__download_status, self.__is_download_finished)
            threads.append(thread_helper.create_thread(moduleWorker.execute))

        if self.__end_modules is not None:
            endWorker = EndModuleWorker(
                self.__archive_end_modules_commands, self.__is_download_finished)
            threads.append(thread_helper.create_thread(endWorker.execute()))

        return threads

    def __create_dir_name(self, target, start_date, end_date):
        return target + '__' + start_date.strftime('%Y-%m-%dT%H-%M-%S') + '__' + end_date.strftime('%Y-%m-%dT%H-%M-%S')
