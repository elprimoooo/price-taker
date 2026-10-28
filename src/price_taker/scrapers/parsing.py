from decimal import Decimal, InvalidOperation


class PriceParseError(ValueError):
    """
    ted jeste nevim co tam chci napsat
    """


CURRENCY_SYMBOLS = {"£": "GBP", "$": "USD", "Kč": "CZK"}


def _normalize_number(text: str, currency: str) -> str:
    text = text.replace(" ", "").replace("\xa0", "")  # mezery pryč vždycky
    if currency == "CZK":
        text = text.replace(",", ".")
    elif currency in ("USD", "GBP"):
        text = text.replace(",", "")

    return text


def parse_price(raw: str) -> tuple[Decimal, str]:
    for symbol, code in CURRENCY_SYMBOLS.items():
        if symbol in raw:
            just_price = raw.replace(symbol, "").strip()
            normalized = _normalize_number(just_price, code)
            try:
                amount = Decimal(normalized)
            except InvalidOperation as exc:
                raise PriceParseError(f"Chyba: v textu se nenašel cena ani symbol{raw}") from exc

            return amount, code

    raise PriceParseError(f"Neznámá měna v textu: {raw!r}")
