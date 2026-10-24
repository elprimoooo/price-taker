from decimal import Decimal


class PriceParseError(ValueError):
    """
    ted jeste nevim co tam chci napsat
    """


CURRENCY_SYMBOLS = {"£": "GBP", "$": "USD", "Kč": "CZK"}


def parse_price(raw: str) -> tuple[Decimal, str]:
    for symbol, code in CURRENCY_SYMBOLS.items():
        if symbol in raw:
            just_price = raw.replace(symbol, "").strip()
            amount = Decimal(just_price)
            return amount, code
    raise PriceParseError(f"Neznámá měna v textu: {raw!r}")
