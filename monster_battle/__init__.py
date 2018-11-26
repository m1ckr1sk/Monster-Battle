import json
import logging
import logging.config

logging.basicConfig(level="INFO")
logger = logging.getLogger()
logger.info("Starting the logger..")


# set up proper logging. This one disables the previously configured loggers.
with open("monster_battle/logging/logging_config.json", "r", 
          encoding="utf-8") as fd:
    json_config = json.load(fd)
    logging.config.dictConfig(json_config['logging'])

logger = logging.getLogger()
logger.info("Loaded logger config.")

