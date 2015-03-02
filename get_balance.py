# -*- coding: utf-8 -*-

import requests
import json
from settings import CONFIG


def get_balance(config):
    full_url = '%(main_api_url)s/balance/' \
               '%(api_user_id)s/%(api_key)s/%(api_secret)s/' % (config)

    api_response = requests.get(full_url)
    return (api_response, api_response.text)


if __name__ == "__main__":
    print get_balance(CONFIG)
