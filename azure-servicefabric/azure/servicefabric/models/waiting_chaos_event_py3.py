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

from .chaos_event import ChaosEvent


class WaitingChaosEvent(ChaosEvent):
    """Describes a Chaos event that gets generated when Chaos is waiting for the
    cluster to become ready for faulting, for example, Chaos may be waiting for
    the on-going upgrade to finish.

    All required parameters must be populated in order to send to Azure.

    :param time_stamp_utc: Required. The UTC timestamp when this Chaos event
     was generated.
    :type time_stamp_utc: datetime
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param reason: Describes why the WaitingChaosEvent was generated, for
     example, due to a cluster upgrade.
    :type reason: str
    """

    _validation = {
        'time_stamp_utc': {'required': True},
        'kind': {'required': True},
    }

    _attribute_map = {
        'time_stamp_utc': {'key': 'TimeStampUtc', 'type': 'iso-8601'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'reason': {'key': 'Reason', 'type': 'str'},
    }

    def __init__(self, *, time_stamp_utc, reason: str=None, **kwargs) -> None:
        super(WaitingChaosEvent, self).__init__(time_stamp_utc=time_stamp_utc, **kwargs)
        self.reason = reason
        self.kind = 'Waiting'
