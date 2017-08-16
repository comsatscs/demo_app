import logging


class Config:
    pass
    # @staticmethod
    # def init_app(app):
    #     # In production mode, add log handler to sys.stderr.
    #     app.logger.addHandler(logging.StreamHandler())
    #     app.logger.setLevel(logging.INFO)


class DevelopmentConfig(Config):
    DEBUG = True
    PORT = 8081

config = {
    'development': DevelopmentConfig,
    # Local server uses default config
    'default': DevelopmentConfig
}