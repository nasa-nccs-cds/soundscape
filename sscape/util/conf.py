from hydra import compose, initialize
from omegaconf import DictConfig
import sys


def cfg() -> DictConfig:
    return Configuration.instance().cfg


def configure(config_name: str, config_path=None):
    sys.tracebacklimit = 100
    if config_path is None: config_path = "../../config"
    Configuration.init( config_name, config_path )

class Configuration:
    _instance = None
    _instantiated = None

    def __init__(self, config_name: str, config_path: str ):
        initialize( version_base=None, config_path=config_path )
        self.cfg: DictConfig = compose( config_name, return_hydra_config=True )

    @classmethod
    def init(cls, config_name: str, config_path: str ):
        if cls._instance is None:
            inst = cls(config_name,config_path)
            cls._instance = inst
            cls._instantiated = cls

    @classmethod
    def instance(cls) -> "Configuration":
        return cls._instance


