"""
utils
"""
import inspect
import pkgutil
import pathlib
import importlib

def initalize(calling_file: str, calling_module: str):
    """Dynamically import sub modules

    Args:
        file (str): current file
        module (str): current module
    """
    for (_, module_name, _) in pkgutil.iter_modules([pathlib.Path(calling_file).resolve().parent]):
        module = importlib.import_module(f"{calling_module}.{module_name}")
        for name, cls in inspect.getmembers(module, inspect.isclass):
            globals()[name] = cls
