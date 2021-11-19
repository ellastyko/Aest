
# .env variables 
from dotenv import dotenv_values
config = dotenv_values(".env")


def env(target = None):
    return int(config[target]) if config[target].isnumeric() else config[target]





# import sys, os

# BASEDIR = os.path.dirname(__file__)
# sys.path.append(BASEDIR)