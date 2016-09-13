# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Sku(Model):
    """Sku of the Namespace.

    :param name: Name of this Sku. Possible values include: 'Basic',
     'Standard', 'Premium'
    :type name: str or :class:`SkuName <azure.mgmt.eventhub.models.SkuName>`
    :param tier: The tier of this particular SKU. Possible values include:
     'Basic', 'Standard', 'Premium'
    :type tier: str or :class:`SkuTier <azure.mgmt.eventhub.models.SkuTier>`
    :param capacity: The eventhub throughput units
    :type capacity: int
    """ 

    _validation = {
        'tier': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'int'},
    }

    def __init__(self, tier, name=None, capacity=None):
        self.name = name
        self.tier = tier
        self.capacity = capacity
