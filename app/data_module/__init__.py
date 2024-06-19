from .data_module import DataModule
from .submodules import DataSubmodule, TableSubmodule, BookmarkSubmodule


DataModule.register_module(TableSubmodule)
DataModule.register_module(BookmarkSubmodule)
