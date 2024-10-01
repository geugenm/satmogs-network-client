import importlib
import logging

from glouton.shared import config


class ModuleService:
    def __init__(self, working_dir):
        self.__working_dir = working_dir
        self.__config = config.read()

    def loadDemoddataModules(self, demoddata_modules, when):
        logging.info('(' + when + ') Demoddata module(s) loading :')
        demoddata_modules = self.__get_modules_from_config(
            demoddata_modules, when, 'DEMODDATA')
        demoddata_modules = self.__get_modules_from_config(
            demoddata_modules, when, 'FOR_ALL_OBSERVATION')

        return self.__load_module(demoddata_modules)

    def loadArchiveModules(self, archive_modules, when):
        logging.info('(' + when + ') Archive module(s) loading :')
        archive_modules = self.__get_modules_from_config(
            archive_modules, when, 'ARCHIVE')
        archive_modules = self.__get_modules_from_config(
            archive_modules, when, 'FOR_ALL_OBSERVATION')

        return self.__load_module(archive_modules)

    def loadWaterfallModules(self, waterfall_modules, when):
        logging.info('(' + when + ') Waterfall module(s) loading :')
        waterfall_modules = self.__get_modules_from_config(
            waterfall_modules, when, 'WATERFALL')
        waterfall_modules = self.__get_modules_from_config(
            waterfall_modules, when, 'FOR_ALL_OBSERVATION')

        return self.__load_module(waterfall_modules)

    def loadFrameModules(self, frame_modules, when):
        logging.info('(' + when + ') Frame module(s) loading :')
        frame_modules = self.__get_modules_from_config(
            frame_modules, when, 'FRAME')

        return self.__load_module(frame_modules)

    def __load_module(self, modules):
        if modules is None:
            logging.info('No module list found')
            return None

        loaded_modules = []
        for name in modules:
            loaded_module = importlib.import_module(
                'glouton.modules.' + name.lower())
            module = getattr(loaded_module, name)
            loaded_modules.append(module(self.__working_dir))
            logging.info('module : ' + name + ' loaded')
        return loaded_modules

    def __get_modules_from_config(self, modules, when, config_array_name):
        try:
            modules_from_config = self.__config['MODULES'][when][config_array_name]
        except Exception as exception:
            logging.warning('config.json : modules bad format: ' + str(exception))
            modules_from_config = []

        if len(modules_from_config) == 0 and modules is None:
            return None

        if len(modules_from_config) == 0 and modules is not None:
            return modules

        if modules is None:
            modules = []

        for module in modules_from_config:
            if module in modules:
                logging.warning('warning : ' + module + ' already referenced.')

            modules.append(module)

        return modules
