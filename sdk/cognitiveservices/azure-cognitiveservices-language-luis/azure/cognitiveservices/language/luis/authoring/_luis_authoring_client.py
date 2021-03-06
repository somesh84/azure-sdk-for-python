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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import LUISAuthoringClientConfiguration
from msrest.exceptions import HttpOperationError
from .operations import FeaturesOperations
from .operations import ExamplesOperations
from .operations import ModelOperations
from .operations import AppsOperations
from .operations import VersionsOperations
from .operations import TrainOperations
from .operations import PermissionsOperations
from .operations import PatternOperations
from .operations import SettingsOperations
from .operations import AzureAccountsOperations
from . import models


class LUISAuthoringClient(SDKClient):
    """LUISAuthoringClient

    :ivar config: Configuration for client.
    :vartype config: LUISAuthoringClientConfiguration

    :ivar features: Features operations
    :vartype features: azure.cognitiveservices.language.luis.authoring.operations.FeaturesOperations
    :ivar examples: Examples operations
    :vartype examples: azure.cognitiveservices.language.luis.authoring.operations.ExamplesOperations
    :ivar model: Model operations
    :vartype model: azure.cognitiveservices.language.luis.authoring.operations.ModelOperations
    :ivar apps: Apps operations
    :vartype apps: azure.cognitiveservices.language.luis.authoring.operations.AppsOperations
    :ivar versions: Versions operations
    :vartype versions: azure.cognitiveservices.language.luis.authoring.operations.VersionsOperations
    :ivar train: Train operations
    :vartype train: azure.cognitiveservices.language.luis.authoring.operations.TrainOperations
    :ivar permissions: Permissions operations
    :vartype permissions: azure.cognitiveservices.language.luis.authoring.operations.PermissionsOperations
    :ivar pattern: Pattern operations
    :vartype pattern: azure.cognitiveservices.language.luis.authoring.operations.PatternOperations
    :ivar settings: Settings operations
    :vartype settings: azure.cognitiveservices.language.luis.authoring.operations.SettingsOperations
    :ivar azure_accounts: AzureAccounts operations
    :vartype azure_accounts: azure.cognitiveservices.language.luis.authoring.operations.AzureAccountsOperations

    :param endpoint: Supported Cognitive Services endpoints (protocol and
     hostname, for example: https://westus.api.cognitive.microsoft.com).
    :type endpoint: str
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    """

    def __init__(
            self, endpoint, credentials):

        self.config = LUISAuthoringClientConfiguration(endpoint, credentials)
        super(LUISAuthoringClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.features = FeaturesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.examples = ExamplesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.model = ModelOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.apps = AppsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.versions = VersionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.train = TrainOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.permissions = PermissionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.pattern = PatternOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.settings = SettingsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.azure_accounts = AzureAccountsOperations(
            self._client, self.config, self._serialize, self._deserialize)
