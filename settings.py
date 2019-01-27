# coding: UTF-8
from os import getenv
from os.path import dirname
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(dirname(__file__)) / '.env'
load_dotenv(dotenv_path=env_path)

WEB_HOOK_URL = getenv('WEB_HOOK_URL')
