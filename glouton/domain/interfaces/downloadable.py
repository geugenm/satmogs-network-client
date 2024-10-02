class Downloadable:
    def create_worker(self):
        raise NotImplementedError()

    def register_command(self):
        raise NotImplementedError()

    def register_end_command(self, start_date, end_date):
        raise NotImplementedError()

    def register_download_command(self, observation, start_date, end_date):
        raise NotImplementedError()