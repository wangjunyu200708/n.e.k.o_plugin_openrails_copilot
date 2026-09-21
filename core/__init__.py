"""
Open Rails Copilot - Core Modules

This package contains the core monitoring and alerting logic:
- snapshot: Data collection from Open Rails API
- detector: Event detection and anomaly analysis
- arbiter: Alert arbitration and deduplication
- push_sender: Message delivery to AI assistant
- safety_guard: Circuit breaker protection
- event_catalog: Complete event definitions
- constants: Configuration parameters
"""

from .snapshot import ORSnapshot
from .detector import ORDetector
from .arbiter import AlertArbiter
from .push_sender import PushSender
from .safety_guard import CircuitBreaker
from .event_catalog import EVENT_CATALOG
from .constants import (
    POLLING_INTERVAL,
    ALERT_COOLDOWN,
    GLOBAL_RATE_LIMIT_WINDOW,
    GLOBAL_RATE_LIMIT_COUNT,
)

__all__ = [
    "ORSnapshot",
    "ORDetector",
    "AlertArbiter",
    "PushSender",
    "CircuitBreaker",
    "EVENT_CATALOG",
    "POLLING_INTERVAL",
    "ALERT_COOLDOWN",
    "GLOBAL_RATE_LIMIT_WINDOW",
    "GLOBAL_RATE_LIMIT_COUNT",
]
