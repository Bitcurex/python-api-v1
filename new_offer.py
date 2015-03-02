# -*- coding: utf-8 -*-

import requests
import json
from settings import CONFIG


def new_offer(config):
    full_url = '%(main_api_url)s/offer/%(market)s/' \
               '%(api_user_id)s/%(api_key)s/' % (config)

    send_data = {
        'limit': CONFIG['limit'],
        'volume': CONFIG['volume'],
        'offer_type': CONFIG['offer_type'],
        'api_secret': CONFIG['api_secret']
    }
    headers = {
        'content-type': 'application/json',
        'accept': 'application/json'
    }

    api_response = requests.post(
        full_url,
        data=json.dumps(send_data),
        headers=headers
    )
    return (api_response, api_response.text)


if __name__ == "__main__":
    print new_offer(CONFIG)
