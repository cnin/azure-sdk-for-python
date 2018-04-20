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

from .entity_health_state_chunk import EntityHealthStateChunk


class ReplicaHealthStateChunk(EntityHealthStateChunk):
    """Represents the health state chunk of a stateful service replica or a
    stateless service instance.
    The replica health state contains the replica ID and its aggregated health
    state.

    :param health_state: The health state of a Service Fabric entity such as
     Cluster, Node, Application, Service, Partition, Replica etc. Possible
     values include: 'Invalid', 'Ok', 'Warning', 'Error', 'Unknown'
    :type health_state: str or ~azure.servicefabric.models.HealthState
    :param replica_or_instance_id: Id of a stateful service replica or a
     stateless service instance. This ID is used in the queries that apply to
     both stateful and stateless services. It is used by Service Fabric to
     uniquely identify a replica of a partition of a stateful service or an
     instance of a stateless service partition. It is unique within a partition
     and does not change for the lifetime of the replica or the instance. If a
     stateful replica gets dropped and another replica gets created on the same
     node for the same partition, it will get a different value for the ID. If
     a stateless instance is failed over on the same or different node it will
     get a different value for the ID.
    :type replica_or_instance_id: str
    """

    _attribute_map = {
        'health_state': {'key': 'HealthState', 'type': 'str'},
        'replica_or_instance_id': {'key': 'ReplicaOrInstanceId', 'type': 'str'},
    }

    def __init__(self, *, health_state=None, replica_or_instance_id: str=None, **kwargs) -> None:
        super(ReplicaHealthStateChunk, self).__init__(health_state=health_state, **kwargs)
        self.replica_or_instance_id = replica_or_instance_id
