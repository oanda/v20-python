The OANDA v20 REST API provides programmatic access to OANDA's next generation
v20 trading engine.

Installation
############

Install using pip::

	pip install v20

If you don't wish to use pip::

	git clone https://github.com/oanda/v20-python.git

Documentation
#############

For documentation, usage and examples, see: http://developer.oanda.com/rest-live-v20/introduction


Examples
########

Each REST V20 endpoint in the `documentation <http://developer.oanda.com/rest-live-v20/>`_ maps to a `Context` object
property which then has ``get()`` and ``list()`` methods used to get a list of objects (ie. ``/v3/accounts``) or a single
object (ie ``/v3/accounts/{accountId}``).

.. code-block:: python

    import v20

    # To use the v20 API, we start by creating a `Context` which first establishes what REST URL to use (ie Practice vs Prod)
    ctx = v20.Context(OANDA_REST_URL, 443, ssl=True)
    # Use your API Personal Access Token by setting it to our `Context` token
    ctx.set_token(OANDA_API_KEY)


See what accounts we have available to interact with.  Notice that our account methods (like ``list``, ``get``, ``summary``)
return ``Response`` objects which have to be drilled down into with their ``body`` property which is a dict with
keys matching what you see in the `"HTTP 200" response documentation for the account endpoints <http://developer.oanda.com/rest-live-v20/account-ep/>`_:


Furthermore, the dict or list values are objects with dot-notation accessible properties matching the object type.
For example, the list of AccountProperties objects has `these properties <http://developer.oanda.com/rest-live-v20/account-df/#AccountProperties>`_

.. code-block:: python

    account_id = ctx.account.list().body['accounts'][0].id
    # Now that we have an account_id, get the account summary.
    account_summary = ctx.account.summary(account_id).body['account']


We can access some properties matching documentation of an `AccountSummary object <http://developer.oanda.com/rest-live-v20/account-df/#AccountSummary>`_
 

.. code-block:: python

    print account_summary.alias
    print account_summary.balance





