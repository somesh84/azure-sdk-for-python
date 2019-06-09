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


class TagCreateUpdateParameters(Model):
    """Parameters supplied to Create/Update Tag operations.

    All required parameters must be populated in order to send to Azure.

    :param display_name: Required. Tag name.
    :type display_name: str
    """

    _validation = {
        'display_name': {'required': True, 'max_length': 160, 'min_length': 1},
    }

    _attribute_map = {
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TagCreateUpdateParameters, self).__init__(**kwargs)
        self.display_name = kwargs.get('display_name', None)