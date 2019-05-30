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


class TransferProductRequestProperties(Model):
    """The properties of the product to initiate a transfer.

    :param destination_invoice_section_id: Destination invoice section id.
    :type destination_invoice_section_id: str
    """

    _attribute_map = {
        'destination_invoice_section_id': {'key': 'destinationInvoiceSectionId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TransferProductRequestProperties, self).__init__(**kwargs)
        self.destination_invoice_section_id = kwargs.get('destination_invoice_section_id', None)