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


class DatasetLocation(Model):
    """Dataset location.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param type: Required. Type of dataset storage location.
    :type type: str
    :param folder_path: Specify the folder path of dataset. Type: string (or
     Expression with resultType string)
    :type folder_path: object
    :param file_name: Specify the file name of dataset. Type: string (or
     Expression with resultType string).
    :type file_name: object
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'type': {'key': 'type', 'type': 'str'},
        'folder_path': {'key': 'folderPath', 'type': 'object'},
        'file_name': {'key': 'fileName', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(DatasetLocation, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.type = kwargs.get('type', None)
        self.folder_path = kwargs.get('folder_path', None)
        self.file_name = kwargs.get('file_name', None)
