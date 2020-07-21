# -*- coding: utf-8 -*-

import unittest
from datetime import datetime

from flask import Flask
from freezegun import freeze_time
import base64
import json
import responses

from smsframework import Gateway, OutgoingMessage
from smsframework.providers import NullProvider
from smsframework_target365 import Target365Provider


class Target365ProviderTest(unittest.TestCase):
    def setUp(self):
        # Gateway
        gw = self.gw = Gateway()
        gw.add_provider('null', NullProvider)  # provocation
        gw.add_provider('main', Target365Provider, base_url='https://target365.api/', 
            key_name='my_api_key',
            # Private key len is defined in the API SDK
            private_key=base64.binascii.hexlify(base64.b64encode(('a' * 23).encode('ascii'))))

        # Flask
        app = self.app = Flask(__name__)

        # Register receivers
        gw.receiver_blueprints_register(app, prefix='/a/b/')

    @responses.activate
    def test_send(self):
        """ Test message send """
        gw = self.gw
        
        # Mock the Target365 Api response.
        # See - https://generator.swagger.io/?url=https%3A%2F%2Ftest.target365.io%2Fapi%2Fswagger.json
        def send_callback(request):
            payload = json.loads(request.body)
            headers = {'Location': '/api/out-messages/{}'.format(payload['transactionId'])}
            return (201, headers, '')
        responses.add_callback(responses.POST, 'https://target365.api/api/out-messages',
            callback=send_callback)

        message = gw.send(OutgoingMessage('+123456', 'hey', provider='main'))
        self.assertEqual(len(responses.calls), 1)
        self.assertTrue(message.msgid)

    @freeze_time('2014-07-01 12:00:00')
    def test_receive_message(self):
        """ Test message receipt """
        self.assertTrue(False, 'Implement the test!')
