from abc import ABC, abstractmethod


class IPlatformScrapper(ABC):
    def __init__(self, url):
        self.url = url

    @abstractmethod
    def problem_name(self):
        pass

    @abstractmethod
    def contest_name(self):
        pass

    @abstractmethod
    def count_submissions(self):
        pass

    @abstractmethod
    def problem_url(self):
        pass

    @abstractmethod
    def note(self):
        pass

    def submissions(self):
        pass
