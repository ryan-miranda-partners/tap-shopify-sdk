import shopify

from tap_shopify.context import Context
from tap_shopify.streams.base import Stream

class Fulfillments(Stream):
    name = 'fulfillments'
    replication_object = shopify.Order

Context.stream_objects['fulfillments'] = Fulfillments