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


class RegionForOnlineOffline(Model):
    """Cosmos DB region to online or offline.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar region: Cosmos DB region, with spaces between words and each word
     capitalized.
    :vartype region: str
    """

    _validation = {
        'region': {'readonly': True},
    }

    _attribute_map = {
        'region': {'key': 'region', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(RegionForOnlineOffline, self).__init__(**kwargs)
        self.region = None