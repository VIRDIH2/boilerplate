import logging
from libraries.database import Database
from utils.configmanager import Config

class BaseDao(object):

    def __init__(self):
        self._logger = logging.getLogger(self.__class__.__name__)
        self._database = Database(Config.connections("DATABASE_SERVER"), Config.connections("DATABASE_NAME"))
    