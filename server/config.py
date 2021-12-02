
# .env variables 
from dotenv import dotenv_values
config = dotenv_values(".env")


def env(target = None):
    return int(config[target]) if config[target].isnumeric() else config[target]
