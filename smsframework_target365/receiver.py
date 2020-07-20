from datetime import datetime, timedelta

from flask import Blueprint
from flask.globals import request, g

from smsframework.data import IncomingMessage
from smsframework.data import MessageAccepted, MessageDelivered, MessageExpired, MessageError

bp = Blueprint('smsframework-target365', __name__, url_prefix='/')


@bp.route('/im')
def im():
    """ Incoming message handler
    TODO: Add documentation here
    """
    req = request.args.to_dict()
    """ Example use og g.provider
    # Prefixes
    if not g.provider.use_prefix:
        req['message'] = ' '.join(filter(lambda x: x, (req['prefix'], req['message'])))
        req['prefix'] = ''
    """

    # Construct IncomingMessage
    message = IncomingMessage(
        src=req['sourceaddr'],
        body=req['message'],
        msgid=req['refno'],
        dst=req['destinationaddr'],
        rtime=datetime.utcnow(),
        meta = {
            # Custom provider req fields
        }
    )

    # Process it
    " :type: smsframework.IProvider.IProvider "
    g.provider._receive_message(message)  # any exceptions will respond with 500, and Target365 will happily retry later

    # Ack. Custom response depends on provider
    return '<ack refno="{msgid}" errorcode="0" />'.format(msgid=message.msgid)


@bp.route('/status')
def status():
    """ Incoming status report
    Optional.
    """
    req = request.args.to_dict()


    # Create status
    status = {
        'DELIVRD': MessageDelivered,
        'ACCEPTD': MessageAccepted,
        'BUFFERD': MessageAccepted
    }[req['Status']](req['refno'], meta=req)
    status.status_code = req['StatusCode']
    status.status = '{0[Status]}: {0[StatusDescription]}'.format(req)

    # Process it
    g.provider._receive_status(status)  # exception respond with http 500

    # Ack. Custom response depends on provider
    return '<?xml version="1.0"?><ack refno="1234" errorcode="0" />'
