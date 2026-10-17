# Price Tracker: Design

## 1. Cíl projektu

Cíl je dynamicky porovnávat jednotlivé produkty na několika eshopech najednou v pravidelných intervalech a schopnost dodávat co nejmenší cenu za jendotlivý produkt.
Úplný cíl je schopnost porovnat ihned jakýkoliv produkt z jakýchkoliv stránek vždy a hned.
Produkt, který si uživatel označí se průběžně zaznamenává do databáze včetně změn cen a dostupnosti, uživatel bude mít přístup k algoritmu, který pozná v jakém intervalu se produkt zlevňuje/zdražuje

## 2. Rozsah MVP

### V MVP

testing proběhne na 2 stránkách vytvořených pro scraping(jedna je v librách)

### Mimo MVP (později)

-Program bude moct zobrazit jakýkoliv produkt bude chtít, stačí když zadá stránku, aktuální cenu a název produktu a algoritmus si produkt zapamatuje a bude stránku scrapovat dokud uživatel proces nezastaví

## 3. User stories

Uživatel bude mít přístup si hned vybrat nejlevnější produkt na trhu, zároveň si může nastavit upozornění na produkty a v případě, že cena klesne pod určitou hodnotu, uživatel dostane upozornění na whatsapp/telegram

1. Jako uživatel chci přidat produkt podle URL, abych začal sledovat jeho cenu.
2. Uživatel bude dostávat upozornění, tam kde je cena nejlevnější
3. Uživatel bude dostávat upozornění, tam kde je cena produktu, který si vybere nejlevnější, zároveň dostane srovnání mezi eshopy včetně dopravy

## 4. Doménový model

### Product

| Pole        | Typ  | Popis                                     |
| ----------- | ---- | ----------------------------------------- |
| id          | int  | primární klíč                             |
| url         | str  | unikátní                                  |
| name        | str  | název produktu                            |
| external_id | str  | id pruduktu na jedné stránce(může chybět) |
| created_at  | date | čas, kdy uživatel začne sledovat produkt  |

### PricePoint

| Pole       | Typ     | Popis                            |
| ---------- | ------- | -------------------------------- |
| id         | int     | cena produktu                    |
| product_id | id      | ke kterému produktu se cena váže |
| on_stock   | boolean | je produkt na skladě?            |

### Watch

| Pole       | Typ     | Popis                                                                 |
| ---------- | ------- | --------------------------------------------------------------------- |
| product_id | Int     | K jakému productu se pricewatch váže?                                 |
| watch_on   | Booelan | Běží hlídaní ceny?                                                    |
| price_set  | Int     | Když se sníží cena daného produktu, tak se pošle uživateli upozornění |

### Rozhodnutí

> Proč je model navržený takhle. Ke každé změně oproti návrhu z Fáze 1
> napiš jednu větu proč. Sem patří i odpověď na otázku s měnami (£ vs Kč).

- [...]

## 5. Analýza zdrojů

### books.toscrape.com

- \*\*Testovací URL: https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
- Fixtures: `\tests\fixtures\view-source_https___books.toscrape.com_catalogue_a-light-in-the-attic_1000_index.html`
- Zdroj ceny: HTLML
- Cena v syrovém HTML: ano
- Skladovost: Na demostránce je ano/ne a kolik, ale do budoucna bude stačit boolean
- Formát ceny:
- Komplikace: na jedné stránce to je v librech

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
