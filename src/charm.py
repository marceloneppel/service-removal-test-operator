#!/usr/bin/env python3
# Copyright 2024 Ubuntu
# See LICENSE file for licensing details.

"""Charm the application."""

import logging

import ops
from charms.observability_libs.v1.kubernetes_service_patch import KubernetesServicePatch
from lightkube.models.core_v1 import ServicePort

logger = logging.getLogger(__name__)


class ServiceRemovalTestOperatorCharm(ops.CharmBase):
    """Charm the application."""

    def __init__(self, framework: ops.Framework):
        super().__init__(framework)
        framework.observe(self.on["some_container"].pebble_ready, self._on_pebble_ready)
        port = ServicePort(8008, name="api")
        self.service_patcher = KubernetesServicePatch(self, [port])

    def _on_pebble_ready(self, event: ops.PebbleReadyEvent):
        """Handle pebble-ready event."""
        self.unit.status = ops.ActiveStatus()


if __name__ == "__main__":  # pragma: nocover
    ops.main(ServiceRemovalTestOperatorCharm)  # type: ignore
