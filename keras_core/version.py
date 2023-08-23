from importlib import metadata

try:
    __version__ = metadata.version(__name__)
except metadata.PackageNotFoundError as error:
    __version__ = str(error)
