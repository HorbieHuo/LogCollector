import json
import logging
import logging.config
import os

def setup_logging(
    default_path='logging.json', 
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

if __name__ == "__main__":
    setup_logging()
    logger = logging.getLogger("lifemg")
    logger.debug("this is a debugmsg!")
    logger.info("this is a infomsg!")
    logger.warn("this is a warn msg!")
    logger.error("this is a error msg!")
    logger.critical("this is a critical msg!")