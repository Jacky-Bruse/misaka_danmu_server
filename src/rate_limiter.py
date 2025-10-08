import logging
from typing import Optional


class RateLimitExceededError(Exception):
    """Placeholder exception kept for backward compatibility."""
    def __init__(self, message: str = "", retry_after_seconds: Optional[int] = None):
        super().__init__(message)
        self.retry_after_seconds = retry_after_seconds or 0


class RateLimiter:
    """No-op implementation to keep flow-control disabled."""

    def __init__(self, *args, **kwargs):
        self.enabled = False
        self.global_limit = 0
        self.global_period_seconds = 0
        self._logger = logging.getLogger(self.__class__.__name__)
        self._logger.info('RateLimiter disabled; all checks are skipped.')

    async def check(self, provider_name: str):
        """Async signature retained; performs no validation."""
        return

    async def increment(self, provider_name: str):
        """Async signature retained; performs no state tracking."""
        return
