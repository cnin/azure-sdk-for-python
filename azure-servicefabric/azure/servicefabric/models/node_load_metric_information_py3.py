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


class NodeLoadMetricInformation(Model):
    """Represents data structure that contains load information for a certain
    metric on a node.

    :param name: Name of the metric for which this load information is
     provided.
    :type name: str
    :param node_capacity: Total capacity on the node for this metric.
    :type node_capacity: str
    :param node_load: Current load on the node for this metric.
    :type node_load: str
    :param node_remaining_capacity: The remaining capacity on the node for
     this metric.
    :type node_remaining_capacity: str
    :param is_capacity_violation: Indicates if there is a capacity violation
     for this metric on the node.
    :type is_capacity_violation: bool
    :param node_buffered_capacity: The value that indicates the reserved
     capacity for this metric on the node.
    :type node_buffered_capacity: str
    :param node_remaining_buffered_capacity: The remaining reserved capacity
     for this metric on the node.
    :type node_remaining_buffered_capacity: str
    """

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'node_capacity': {'key': 'NodeCapacity', 'type': 'str'},
        'node_load': {'key': 'NodeLoad', 'type': 'str'},
        'node_remaining_capacity': {'key': 'NodeRemainingCapacity', 'type': 'str'},
        'is_capacity_violation': {'key': 'IsCapacityViolation', 'type': 'bool'},
        'node_buffered_capacity': {'key': 'NodeBufferedCapacity', 'type': 'str'},
        'node_remaining_buffered_capacity': {'key': 'NodeRemainingBufferedCapacity', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, node_capacity: str=None, node_load: str=None, node_remaining_capacity: str=None, is_capacity_violation: bool=None, node_buffered_capacity: str=None, node_remaining_buffered_capacity: str=None, **kwargs) -> None:
        super(NodeLoadMetricInformation, self).__init__(**kwargs)
        self.name = name
        self.node_capacity = node_capacity
        self.node_load = node_load
        self.node_remaining_capacity = node_remaining_capacity
        self.is_capacity_violation = is_capacity_violation
        self.node_buffered_capacity = node_buffered_capacity
        self.node_remaining_buffered_capacity = node_remaining_buffered_capacity
