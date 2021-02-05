class Config:
    SECRET_KEY = None
    LOG_LEVEL = "DEBUG"


class Test(Config):
    TESTING = True
    DEBUG = True
    LOG_LEVEL = "CRITICAL"
    SECRET_KEY = "not-a-secret"


class Development(Config):
    DEBUG = True


class Live(Config):
    LOG_LEVEL = "ERROR"


def get_config(environment: str) -> Config:
    configs = {
        'test': Test,
        'development': Development,
        'live': Live
    }
    return configs.get(environment)
