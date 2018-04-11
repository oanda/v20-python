import ujson as json
from v20.base_entity import BaseEntity
from v20.base_entity import EntityDict
from v20.request import Request
from v20 import spec_properties



class MT4TransactionHeartbeat(BaseEntity):
    """
    A TransactionHeartbeat object is injected into the Transaction stream to
    ensure that the HTTP connection remains active.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Transaction Heartbeat {time}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = ""

    #
    # Property metadata for this object
    #
    _properties = spec_properties.site_MT4TransactionHeartbeat

    def __init__(self, **kwargs):
        """
        Create a new MT4TransactionHeartbeat instance
        """
        super(MT4TransactionHeartbeat, self).__init__()
 
        #
        # The string "HEARTBEAT"
        #
        self.type = kwargs.get("type", "HEARTBEAT")
 
        #
        # The date/time when the TransactionHeartbeat was created.
        #
        self.time = kwargs.get("time")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new MT4TransactionHeartbeat from a dict (generally from
        loading a JSON response). The data used to instantiate the
        MT4TransactionHeartbeat is a shallow copy of the dict passed in, with
        any complex child types instantiated appropriately.
        """

        data = data.copy()

        return MT4TransactionHeartbeat(**data)


class EntitySpec(object):
    """
    The site.EntitySpec wraps the site module's type definitions
    and API methods so they can be easily accessed through an instance of a v20
    Context.
    """

    MT4TransactionHeartbeat = MT4TransactionHeartbeat

    def __init__(self, ctx):
        self.ctx = ctx

