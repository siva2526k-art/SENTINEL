"""
SENTINEL — External Integrations Package
Discord Webhook · Real-Time SOC Alert Notifications
"""
from .discord_bot import SentinelDiscordNotifier

__all__ = ["SentinelDiscordNotifier"]
