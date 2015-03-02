# -*- coding: utf-8 -*-

import requests
import json
from settings import CONFIG


def cancel_offer(config):
    full_url = '%(main_api_url)s/offer/del/%(api_user_id)s/' \
               '%(api_key)s' % (config)

    send_data = {
        'offer_id': CONFIG['offer_id'],
        'api_secret': CONFIG['api_secret']
    }
    headers = {
        'content-type': 'application/json',
        'accept': 'application/json'
    }

    api_response = requests.delete(
        full_url,
        data=json.dumps(send_data),
        headers=headers
    )

    return (api_response, api_response.text)


if __name__ == "__main__":
    print cancel_offer(CONFIG)
