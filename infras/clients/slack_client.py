# coding: UTF-8
from apps.logger import AppLogger
from slackweb import Slack
from urllib.error import HTTPError, URLError


class SlackClient:

    slack: Slack

    def __init__(self, url: str):
        self.slack = Slack(url=url)

    def post(self, message):

        logger = AppLogger.get_logger(__name__)

        try:
            self.slack.notify(text=message)

        except HTTPError as error:
            logger.error('Error code: %s' % error.code)

        except URLError as error:
            logger.error('Reason: %s' % error.reason)
