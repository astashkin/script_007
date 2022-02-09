import logging.config
import yaml


with open(file="src/logger/log_config.yaml", mode='r') as file:
    logging_yaml = yaml.load(stream=file, Loader=yaml.FullLoader)
    logging.config.dictConfig(config=logging_yaml)
