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

from .resource import Resource


class ActionGroupResource(Resource):
    """An action group resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param group_short_name: Required. The short name of the action group.
     This will be used in SMS messages.
    :type group_short_name: str
    :param enabled: Required. Indicates whether this action group is enabled.
     If an action group is not enabled, then none of its receivers will receive
     communications. Default value: True .
    :type enabled: bool
    :param email_receivers: The list of email receivers that are part of this
     action group.
    :type email_receivers: list[~azure.mgmt.monitor.models.EmailReceiver]
    :param sms_receivers: The list of SMS receivers that are part of this
     action group.
    :type sms_receivers: list[~azure.mgmt.monitor.models.SmsReceiver]
    :param webhook_receivers: The list of webhook receivers that are part of
     this action group.
    :type webhook_receivers: list[~azure.mgmt.monitor.models.WebhookReceiver]
    :param itsm_receivers: The list of ITSM receivers that are part of this
     action group.
    :type itsm_receivers: list[~azure.mgmt.monitor.models.ItsmReceiver]
    :param azure_app_push_receivers: The list of AzureAppPush receivers that
     are part of this action group.
    :type azure_app_push_receivers:
     list[~azure.mgmt.monitor.models.AzureAppPushReceiver]
    :param automation_runbook_receivers: The list of AutomationRunbook
     receivers that are part of this action group.
    :type automation_runbook_receivers:
     list[~azure.mgmt.monitor.models.AutomationRunbookReceiver]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'group_short_name': {'required': True, 'max_length': 15},
        'enabled': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'group_short_name': {'key': 'properties.groupShortName', 'type': 'str'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
        'email_receivers': {'key': 'properties.emailReceivers', 'type': '[EmailReceiver]'},
        'sms_receivers': {'key': 'properties.smsReceivers', 'type': '[SmsReceiver]'},
        'webhook_receivers': {'key': 'properties.webhookReceivers', 'type': '[WebhookReceiver]'},
        'itsm_receivers': {'key': 'properties.itsmReceivers', 'type': '[ItsmReceiver]'},
        'azure_app_push_receivers': {'key': 'properties.azureAppPushReceivers', 'type': '[AzureAppPushReceiver]'},
        'automation_runbook_receivers': {'key': 'properties.automationRunbookReceivers', 'type': '[AutomationRunbookReceiver]'},
    }

    def __init__(self, **kwargs):
        super(ActionGroupResource, self).__init__(**kwargs)
        self.group_short_name = kwargs.get('group_short_name', None)
        self.enabled = kwargs.get('enabled', True)
        self.email_receivers = kwargs.get('email_receivers', None)
        self.sms_receivers = kwargs.get('sms_receivers', None)
        self.webhook_receivers = kwargs.get('webhook_receivers', None)
        self.itsm_receivers = kwargs.get('itsm_receivers', None)
        self.azure_app_push_receivers = kwargs.get('azure_app_push_receivers', None)
        self.automation_runbook_receivers = kwargs.get('automation_runbook_receivers', None)
