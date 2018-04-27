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

from enum import Enum


class SkuName(Enum):

    basic = "Basic"
    standard = "Standard"
    premium = "Premium"


class SkuFamily(Enum):

    c = "C"
    p = "P"


class TlsVersion(Enum):

    one_full_stop_zero = "1.0"
    one_full_stop_one = "1.1"
    one_full_stop_two = "1.2"


class ProvisioningState(Enum):

    creating = "Creating"
    deleting = "Deleting"
    disabled = "Disabled"
    failed = "Failed"
    linking = "Linking"
    provisioning = "Provisioning"
    recovering_scale_failure = "RecoveringScaleFailure"
    scaling = "Scaling"
    succeeded = "Succeeded"
    unlinking = "Unlinking"
    unprovisioning = "Unprovisioning"
    updating = "Updating"


class RedisKeyType(Enum):

    primary = "Primary"
    secondary = "Secondary"


class RebootType(Enum):

    primary_node = "PrimaryNode"
    secondary_node = "SecondaryNode"
    all_nodes = "AllNodes"


class DayOfWeek(Enum):

    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"
    sunday = "Sunday"
    everyday = "Everyday"
    weekend = "Weekend"


class ReplicationRole(Enum):

    primary = "Primary"
    secondary = "Secondary"


class DefaultName(Enum):

    microsoft_cacheredis = "Microsoft.Cache/redis"
