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


class DdosProtectionPlan(Model):
    """A DDoS protection plan in a resource group.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :ivar resource_guid: The resource GUID property of the DDoS protection
     plan resource. It uniquely identifies the resource, even if the user
     changes its name or migrate the resource across subscriptions or resource
     groups.
    :vartype resource_guid: str
    :ivar provisioning_state: The provisioning state of the DDoS protection
     plan resource. Possible values are: 'Succeeded', 'Updating', 'Deleting',
     and 'Failed'.
    :vartype provisioning_state: str
    :ivar virtual_networks: The list of virtual networks associated with the
     DDoS protection plan resource. This list is read-only.
    :vartype virtual_networks:
     list[~azure.mgmt.network.v2018_02_01.models.SubResource]
    :ivar etag: A unique read-only string that changes whenever the resource
     is updated.
    :vartype etag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'resource_guid': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'virtual_networks': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'resource_guid': {'key': 'properties.resourceGuid', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'virtual_networks': {'key': 'properties.virtualNetworks', 'type': '[SubResource]'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DdosProtectionPlan, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)
        self.resource_guid = None
        self.provisioning_state = None
        self.virtual_networks = None
        self.etag = None
