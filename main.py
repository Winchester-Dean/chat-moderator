import os
import inspect

from aiogram import executor
from typing import List, Callable, Awaitable, Union
from importlib import import_module

from dispatcher import dp

class Main:
    def __init__(
        self,
        directory: str = "handlers"
    ):
        handlers = []

        for files in os.listdir(directory):
            if files.endswith("_handle.py"):
                file = files[:-3]

                modules = import_module(
                    f"{directory}.{file}"
                )

                for classname, classobj in inspect.getmembers(
                    modules, inspect.isclass
                ):
                    handlers.append(classobj())
    
    def start(self):
        for handler in handlers:
            handler[0].register(dp)

        executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
    Main().start()
