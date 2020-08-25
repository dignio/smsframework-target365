|Build Status|

SMSframework Target365 Provider
===============================================

`Target365` Provider for
`smsframework <https://pypi.python.org/pypi/smsframework/>`__.

You need an account with "SMS Server" service set up. You'll need the
following configuration: username, password.

Installation
============

Install from pypi:

::

    $ pip install smsframework_target365

To receive SMS messages, you need to ensure that `Flask
microframework <http://flask.pocoo.org>`__ is also installed:

::

    $ pip install smsframework_target365[receiver]

Initialization
==============

.. code:: python

    from smsframework import Gateway
    from smsframework_target365 import Target365Provider

    gateway = Gateway()
    gateway.add_provider('target365', Target365Provider,
        base_url='https://shared.target365.io/',
        key_name='YourKeyName',
        private_key='SecretHex'
    )

Config
------

Source: /smsframework_target365/provider.py


-  ``base_url: str``: target365 api base url
-  ``key_name: str``: Key identifier on target365
-  ``private_key: str``: hex number from ``openssl pkey -in mykey.pem -text`` see `Target365 SDK Mhttps://github.com/Target365/sdk-for-python>`

Sending Parameters
==================

Provider-specific sending params: None

Additional Information
======================

OutgoingMessage.meta
--------------------

Provider-specific sending params

IncomingMessage.meta
--------------------

Provider-specific income message fields.

MessageStatus.meta
------------------

Provider-specific message status fields.

Receivers
=========

Source: /smsframework_target365/receiver.py

Message Receiver: /im
---------------------

Go to Configuration > Connections, click 'Change'. Put the message
receiver URL into "HTTP url" field.

Message Receiver URL: ``<provider-name>/im``
