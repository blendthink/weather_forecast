# coding: UTF-8
from logging import getLogger, Logger, Formatter, INFO
from logging.handlers import TimedRotatingFileHandler


class AppLogger:

    __FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    __FILE_NAME = './../logs/app.log'
    __WHEN = 'D'
    __BACKUP_COUNT = 10

    @staticmethod
    def get_logger(name: str) -> Logger:

        logger = getLogger(name)
        logger.setLevel(INFO)

        handler = TimedRotatingFileHandler(
            filename=AppLogger.__FILE_NAME,
            when=AppLogger.__WHEN,
            backupCount=AppLogger.__BACKUP_COUNT
        )

        formatter = Formatter(AppLogger.__FORMAT)
        handler.setFormatter(formatter)

        logger.addHandler(handler)

        return logger
