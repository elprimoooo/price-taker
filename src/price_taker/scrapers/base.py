from abc import ABC, abstractmethod
from typing import ClassVar

from price_taker.domain.models import ScrapedProduct


class ScrapeError(Exception):
    """Ze stránky nejde získat potřebná data (např. se změnilo HTML)."""


class BaseScraper(ABC):
    """Společné rozhraní pro všechny scrapery."""

    domain: ClassVar[str]

    @abstractmethod
    def parse(self, html: str) -> ScrapedProduct:
        """Z HTML produktové stránky vytáhne data o produktu."""
