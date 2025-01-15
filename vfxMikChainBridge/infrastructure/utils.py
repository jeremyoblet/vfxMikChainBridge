import os

def get_prod_root_env_variable():
    prod_env = os.getenv("PROD_ROOT")
    if not prod_env:
        raise EnvironmentError("Environment variable '$PROD_ROOT' is not defined")
    return prod_env
