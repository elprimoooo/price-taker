from decimal import Decimal

import pytest

from price_taker.scrapers.parsing import PriceParseError, parse_price


def test_parses_pounds() -> None:
    assert parse_price("£51.77") == (Decimal("51.77"), "GBP")


def test_unknown_currency_raises() -> None:
    with pytest.raises(PriceParseError):
        parse_price("zdarma")
