


from dotenv import dotenv_values
config = dotenv_values(".env")


def env(target = None):
    return config[target] 

print(env('PORT'))