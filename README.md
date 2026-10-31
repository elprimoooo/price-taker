# Price Tracker

Aplikace sleduje ceny produktů v e-shopech, ukládá jejich historii a upozorní,
když cena klesne pod zvolenou hranici. Do budoucna bude z historie odhadovat,
kdy produkt zlevní.

> 🚧 **Projekt ve vývoji.** Vzniká jako učební projekt: kompletní
> životní cyklus backendové aplikace od návrhu přes testy po nasazení.

## Co umí

- [x] Převod textu ceny na číslo a měnu (`£51.77`, `$1,299.99`, `1 299,90 Kč`)
- [x] Scraper pro books.toscrape.com
- [ ] Ukládání historie cen do databáze
- [ ] REST API (FastAPI)
- [ ] Upozornění při poklesu ceny pod zvolenou hranici
- [ ] Odhad časové osy zlevnění produktu
- [ ] Docker a CI/CD

Podrobný návrh je v [DESIGN.md](DESIGN.md).

## Technologie

Python 3.14 · uv · Pydantic · BeautifulSoup · pytest · ruff · mypy (strict)

## Spuštění

Požadavky: [uv](https://docs.astral.sh/uv/)

```bash
git clone https://github.com/elprimoooo/price-taker.git
cd price-taker
uv sync
```

## Testy a kontrola kvality

```bash
uv run pytest          # testy
uv run ruff check .    # linter
uv run ruff format .   # formátování
uv run mypy            # kontrola typů
```

## Struktura projektu

```
src/price_taker/
├── domain/      # doménové modely
└── scrapers/    # stahování a čtení cen z e-shopů
    └── shops/   # jeden soubor = jeden e-shop
tests/
├── fixtures/    # uložené HTML stránky pro testy
└── unit/
```
