from decimal import Decimal

import pytest

from price_taker.scrapers.parsing import PriceParseError, parse_price


def test_parses_pounds() -> None:
    assert parse_price("£51.77") == (Decimal("51.77"), "GBP")


def test_parses_czk_with_surrounding_spaces() -> None:
    assert parse_price(" 32.5Kč ") == (Decimal("32.5"), "CZK")


def test_different_currency_whole_number() -> None:
    assert parse_price("$10") == (Decimal("10"), "USD")


def test_thousand_seperator() -> None:
    assert parse_price("1 299,90 Kč") == (Decimal("1299.90"), "CZK")


def test_thousand_with_comma_and_dot() -> None:
    assert parse_price("$1,299.99") == (Decimal("1299.99"), "USD")


def test_thousand_with_comma() -> None:
    assert parse_price("$1,299") == (Decimal("1299"), "USD")


def test_unknown_currency_raises() -> None:
    with pytest.raises(PriceParseError):
        parse_price("zdarma")


def test_no_number_only_symbol_nad_chars_in_price_raise() -> None:
    with pytest.raises(PriceParseError):
        parse_price("£abc")


def test_no_number_symbol_or_chars_in_price_raise() -> None:
    with pytest.raises(PriceParseError):
        parse_price("")
