import os
import logging.config
from utils.configmanager import Config

def init():
    logging.basicConfig(
        filename= Config.logging('FILE_PATH'),
        level=Config.logging('LEVEL'),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)