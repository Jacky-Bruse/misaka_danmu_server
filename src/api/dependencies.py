from fastapi import Request

from ..config_manager import ConfigManager
from ..metadata_manager import MetadataSourceManager
from ..rate_limiter import RateLimiter
from ..scheduler import SchedulerManager
from ..scraper_manager import ScraperManager
from ..task_manager import TaskManager
from ..title_recognition import TitleRecognitionManager
from ..webhook_manager import WebhookManager


async def get_scraper_manager(request: Request) -> ScraperManager:
    return request.app.state.scraper_manager


async def get_task_manager(request: Request) -> TaskManager:
    return request.app.state.task_manager


async def get_scheduler_manager(request: Request) -> SchedulerManager:
    return request.app.state.scheduler_manager


async def get_webhook_manager(request: Request) -> WebhookManager:
    return request.app.state.webhook_manager


async def get_metadata_manager(request: Request) -> MetadataSourceManager:
    return request.app.state.metadata_manager


async def get_config_manager(request: Request) -> ConfigManager:
    return request.app.state.config_manager


async def get_rate_limiter(request: Request) -> RateLimiter:
    return request.app.state.rate_limiter



async def get_title_recognition_manager(request: Request) -> TitleRecognitionManager:
    return request.app.state.title_recognition_manager

