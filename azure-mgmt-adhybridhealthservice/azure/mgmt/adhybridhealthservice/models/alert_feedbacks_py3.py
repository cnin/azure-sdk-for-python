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


class AlertFeedbacks(Model):
    """The list of alert feedback.

    :param value: The value returned by the operation.
    :type value: list[~azure.mgmt.adhybridhealthservice.models.AlertFeedback]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[AlertFeedback]'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(AlertFeedbacks, self).__init__(**kwargs)
        self.value = value
