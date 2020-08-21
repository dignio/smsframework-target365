from datetime import datetime, timedelta

from flask import Blueprint
from flask.globals import request, g

from smsframework.data import IncomingMessage
from smsframework.data import MessageAccepted, MessageDelivered, MessageExpired, MessageError

bp = Blueprint('smsframework-target365', __name__, url_prefix='/')


@bp.route('/im', methods=['POST'])
def im():
    """ Incoming message handler
    """
    req = request.json
    # Construct IncomingMessage
    message = IncomingMessage(
        src=req['sender'],
        body=req['content'],
        msgid=req['transactionId'],
        dst=req['recipient'],
        rtime=datetime.utcnow(),
        meta = {
            'created': req['created']
        }
    )

    # Process it
    " :type: smsframework.IProvider.IProvider "
    g.provider._receive_message(message)  # any exceptions will respond with 500, and Target365 will happily retry later

    return 'OK'
