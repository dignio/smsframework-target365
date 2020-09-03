from smsframework import IProvider, exc
from . import error
import uuid
from target365_sdk import ApiClient
from target365_sdk.models.out_message import OutMessage
from requests.exceptions import HTTPError, ConnectionError


class Target365Provider(IProvider):
    """ Target365 provider
    Python SDK used - https://github.com/Target365/sdk-for-python/blob/master/USERGUIDE.md 
    """

    def __init__(self, gateway, name, base_url, key_name, private_key):
        """ Configure Target365 provider
            :param base_url: Target365 base url str. example - "https://shared.target365.io/"
            :param key_name: Api access key name
            :param private_key: BASE64 encrypted secret key
        """
        self.api_client = ApiClient(base_url, key_name, private_key)
        super(Target365Provider, self).__init__(gateway, name)


    def send(self, message):
        """ Send a message

            :type message: smsframework.data.OutgoingMessage.OutgoingMessage
            :rtype: OutgoingMessage
            """
        try:
            # Target365 SDK message
            out_message = OutMessage()
            out_message.transactionId = str(uuid.uuid4())
            if message.src is None and message.provider_options.senderId is None:
                raise exc.RequestError('message.src or message.provider_options.senderId is mandatory')

            out_message.sender = message.provider_options.senderId or message.src
            out_message.recipient = '+' + message.dst
            out_message.content = message.body
            self.api_client.create_out_message(out_message)
            message.msgid = out_message.transactionId
            return message
        except AssertionError as e:
            raise exc.RequestError(str(e))
        except HTTPError as e:
            raise exc.MessageSendError(str(e))
        except ConnectionError as e:
            raise exc.ConnectionError(str(e))

    def make_receiver_blueprint(self):
        """ Create the receiver blueprint """
        from . import receiver
        return receiver.bp
