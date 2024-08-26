import shopify

from tap_shopify.context import Context
from tap_shopify.streams.base import Stream

class FulfillmentOrder(Stream):
    name = 'fulfillment_order'
    replication_object = shopify.Order

Context.stream_objects['fulfillment_order'] = FulfillmentOrder