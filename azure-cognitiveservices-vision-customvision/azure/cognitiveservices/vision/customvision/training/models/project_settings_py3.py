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


class ProjectSettings(Model):
    """Represents settings associated with a project.

    :param domain_id: Gets or sets the id of the Domain to use with this
     project
    :type domain_id: str
    """

    _attribute_map = {
        'domain_id': {'key': 'DomainId', 'type': 'str'},
    }

    def __init__(self, *, domain_id: str=None, **kwargs) -> None:
        super(ProjectSettings, self).__init__(**kwargs)
        self.domain_id = domain_id