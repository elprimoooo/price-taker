from bs4 import BeautifulSoup

from price_taker.domain.models import ScrapedProduct
from price_taker.scrapers.base import BaseScraper, ScrapeError
from price_taker.scrapers.parsing import parse_price
from pathlib import Path


class BooksToScrapeScraper(BaseScraper):
    domain = "books.toscrape.com"

    def parse(self, html: str) -> ScrapedProduct:
        soup = BeautifulSoup(html, "html.parser")

        # 1. Název z <h1>
        title = soup.select_one("h1")
        if title is None:
            raise ScrapeError("Na stránce chybí název produktu")
        name = title.get_text(strip=True)

        # 2. Tabulka jako slovník
        ##tenhle shit udelam v sobotu
        info = _read_info_table(soup)

        # 3. Cena
        ...   # vezmi info["Price (incl. tax)"] a pusť přes parse_price
              # když klíč chybí → ScrapeError

        # 4. Skladem?
        ...   # podle textu v info["Availability"]

        # 5. UPC
        ...   # info.get("UPC")  – může chybět, je nepovinné

        return ScrapedProduct(
            name=name,
            price=...,
            currency=...,
            in_stock=...,
            external_id=...,
        )


def _read_info_table(soup: BeautifulSoup) -> dict[str, str]:
    """Převede tabulku Product Information na slovník {popisek: hodnota}."""
    info: dict[str, str] = {}
    for row in soup.select("table.table-striped tr"):
        ...   # najdi th a td, když některý chybí → continue
              # jinak ulož: info[text z th] = text z td
    return info