import json
import sys, os
from os.path import isfile

import twitter

import config


def get_api():
    return twitter.Api(consumer_key=config.twitter['CONSUMER_KEY'],
                       consumer_secret=config.twitter['CONSUMER_SECRET'],
                       access_token_key=config.twitter['ACCESS_TOKEN'],
                       access_token_secret=config.twitter['ACCESS_TOKEN_SECRET'])


def cur_dir(filename=None):
    cur_path = os.path.dirname(os.path.realpath(__file__))
    if filename is not None:
        cur_path = os.path.join(cur_path, filename)
    return cur_path


def clean_file(filepath):
    open(filepath, 'w').close()


def write_json(filepath, data):
    with open(filepath, 'a+') as outfile:
        outfile.write(data)


def clean_folder(dir_path):
    files = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if isfile(os.path.join(dir_path, f))]
    for f in files:
        os.remove(f)


def file_exists(path):
    return os.path.isfile(path)


def directory_exists(path):
    return os.path.isdir(path)


def dd(input):
    print(input)
    sys.exit(0)
