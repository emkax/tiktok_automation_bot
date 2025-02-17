"""
TikTok Uploader Initialization
"""
from os.path import abspath, join, dirname
import logging

import toml

import os


## Load Config
src_dir = abspath(dirname(__file__))
print(src_dir)
path = os.path.join(src_dir,'config.toml') 
print(os.path.join(src_dir,'config.toml'))
with open(path, 'r') as f:
    config = toml.load(f)

## Setup Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s %(message)s',
    datefmt='[%H:%M:%S]'
)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
