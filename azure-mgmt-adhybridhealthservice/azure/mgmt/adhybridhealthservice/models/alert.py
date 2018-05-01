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


class Alert(Model):
    """The alert details indicating an issue with service or server.

    :param alert_id: The alert Id.
    :type alert_id: str
    :param level: The alert level which indicates the severity of the alert.
     Possible values include: 'Warning', 'Error', 'PreWarning'
    :type level: str or ~azure.mgmt.adhybridhealthservice.models.Level
    :param state: The alert state which can be either active or resolved with
     multile resolution types. Possible values include: 'Active',
     'ResolvedByPositiveResult', 'ResolvedManually', 'ResolvedByTimer',
     'ResolvedByStateChange'
    :type state: str or ~azure.mgmt.adhybridhealthservice.models.State
    :param short_name: The alert short name.
    :type short_name: str
    :param display_name: The display name for the alert.
    :type display_name: str
    :param description: The alert description.
    :type description: str
    :param remediation: The alert remediation.
    :type remediation: str
    :param related_links: The help links to get more information related to
     the alert.
    :type related_links:
     list[~azure.mgmt.adhybridhealthservice.models.HelpLink]
    :param scope: The scope of the alert. Indicates if it is a service or a
     server related alert.
    :type scope: str
    :param additional_information: Additional information related to the
     alert.
    :type additional_information:
     list[~azure.mgmt.adhybridhealthservice.models.AdditionalInformation]
    :param created_date: The date and time,in UTC,when the alert was created.
    :type created_date: datetime
    :param resolved_date: The date and time, in UTC, when the alert was
     resolved.
    :type resolved_date: datetime
    :param last_updated: The date and time, in UTC, when the alert was last
     updated.
    :type last_updated: datetime
    :param monitoring_role_type: The monitoring role type for which the alert
     was raised.
    :type monitoring_role_type: str
    :param active_alert_properties: The active alert properties.
    :type active_alert_properties: object
    :param resolved_alert_properties: The active alert properties.
    :type resolved_alert_properties: object
    :param tenant_id: The tenant Id.
    :type tenant_id: str
    :param service_id: The service Id.
    :type service_id: str
    :param service_member_id: The server Id.
    :type service_member_id: str
    """

    _attribute_map = {
        'alert_id': {'key': 'alertId', 'type': 'str'},
        'level': {'key': 'level', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'short_name': {'key': 'shortName', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'remediation': {'key': 'remediation', 'type': 'str'},
        'related_links': {'key': 'relatedLinks', 'type': '[HelpLink]'},
        'scope': {'key': 'scope', 'type': 'str'},
        'additional_information': {'key': 'additionalInformation', 'type': '[AdditionalInformation]'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'resolved_date': {'key': 'resolvedDate', 'type': 'iso-8601'},
        'last_updated': {'key': 'lastUpdated', 'type': 'iso-8601'},
        'monitoring_role_type': {'key': 'monitoringRoleType', 'type': 'str'},
        'active_alert_properties': {'key': 'activeAlertProperties', 'type': 'object'},
        'resolved_alert_properties': {'key': 'resolvedAlertProperties', 'type': 'object'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'service_id': {'key': 'serviceId', 'type': 'str'},
        'service_member_id': {'key': 'serviceMemberId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Alert, self).__init__(**kwargs)
        self.alert_id = kwargs.get('alert_id', None)
        self.level = kwargs.get('level', None)
        self.state = kwargs.get('state', None)
        self.short_name = kwargs.get('short_name', None)
        self.display_name = kwargs.get('display_name', None)
        self.description = kwargs.get('description', None)
        self.remediation = kwargs.get('remediation', None)
        self.related_links = kwargs.get('related_links', None)
        self.scope = kwargs.get('scope', None)
        self.additional_information = kwargs.get('additional_information', None)
        self.created_date = kwargs.get('created_date', None)
        self.resolved_date = kwargs.get('resolved_date', None)
        self.last_updated = kwargs.get('last_updated', None)
        self.monitoring_role_type = kwargs.get('monitoring_role_type', None)
        self.active_alert_properties = kwargs.get('active_alert_properties', None)
        self.resolved_alert_properties = kwargs.get('resolved_alert_properties', None)
        self.tenant_id = kwargs.get('tenant_id', None)
        self.service_id = kwargs.get('service_id', None)
        self.service_member_id = kwargs.get('service_member_id', None)
