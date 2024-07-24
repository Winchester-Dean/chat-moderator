from abc import ABC, abstractmethod
from aiogram import Dispatcher

class BaseHandler(ABC):
    @abstractmethod
    def register(self, dp: Dispatcher):
        pass

