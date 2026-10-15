# Price Tracker: Design

## 1. Cíl projektu
Cíl je dynamicky porovnávat jednotlivé produkty na několika eshopech najednou v pravidelných intervalech a schopnost dodávat co nejmenší cenu za jendotlivý produkt.
Úplný cíl je schopnost porovnat ihned jakýkoliv produkt z jakýchkoliv stránek vždy a hned.

## 2. Rozsah MVP

### V MVP
 testing proběhne na 2 stránkách vytvořených pro scraping(jedna je v librách)

### Mimo MVP (později)
- [...]

> Vycházej z toho, co jsme probrali ve Fázi 1. Klidně něco přesuň nebo přidej,
> ale každý bod, který přidáš do MVP, ho prodlužuje.

## 3. User stories
Uživatel bude mít přístup si hned vybrat nejlevnější produkt na trhu, zároveň si může nastavit upozornění na produkty a v případě, že cena klesne pod určitou hodnotu, uživatel dostane upozornění na whatsapp/telegram

1. Jako uživatel chci přidat produkt podle URL, abych začal sledovat jeho cenu.
2. [...]    
3. [...]

## 4. Doménový model

### Product
| Pole | Typ | Popis |
|---|---|---|
| id | int | primární klíč |
| url | str | unikátní |
| [...] | | |

### PricePoint
| Pole | Typ | Popis |
|---|---|---|
| [...] | | |

### Watch
| Pole | Typ | Popis |
|---|---|---|
| [...] | | |

### Rozhodnutí
> Proč je model navržený takhle. Ke každé změně oproti návrhu z Fáze 1
> napiš jednu větu proč. Sem patří i odpověď na otázku s měnami (£ vs Kč).

- [...]

## 5. Analýza zdrojů

### books.toscrape.com
- **Testovací URL:**
- **Fixtures:** `tests/fixtures/...`
- **Zdroj ceny:** JSON-LD / microdata / HTML selektor `...`
- **Cena v syrovém HTML:** ano / ne
- **Skladovost:** jak se pozná
- **Formát ceny:**
- **Komplikace:**

### webscraper.io (statická verze)
- (stejné body)

### Co mají zdroje společného → doménový model
- [...]

### Čím se liší → řeší scraper
- [...]

## 6. Otevřené otázky
> Věci, které zatím nevíš nebo jsi nerozhodl. Je v pořádku jich mít víc.
> Příklad: „Co když produkt zmizí z webu (404)? Smazat ho, nebo označit?“

- [...]