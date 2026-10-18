# Price Tracker: Design

## 1. Cíl projektu

### Vize (dlouhodobě)

Porovnávat ceny stejného produktu napříč e-shopy (včetně dopravy a variant),
najít nejlevnější nabídku a předpovídat, kdy produkt zlevňuje.

### Cíl MVP

Sledovat cenu konkrétních produktů v čase, ukládat historii ceny a dostupnosti
a upozornit uživatele, když cena klesne pod zvolenou hranici.

## 2. Rozsah MVP

### V MVP

- Přidání produktu podle URL a jeho odebrání ze sledování
- Pravidelné stahování ceny a dostupnosti (worker)
- Ukládání historie cen
- Nastavení cílové ceny; upozornění zatím jen zápisem do logu
- API: výpis produktů, historie cen, statistiky (min, max, poslední cena)
- Zdroje: books.toscrape.com a webscraper.io (tréninkové weby)

### Mimo MVP (později)

- Upozornění přes Telegram (případně WhatsApp)
- Analýza historie: v jakých intervalech produkt zlevňuje (Pandas)
- Vlastní falešný e-shop s měnícími se cenami (pro testování)
- Skutečné e-shopy
- Porovnání stejného produktu napříč e-shopy (product matching)
- Varianty produktu a cena dopravy
- Uživatelské účty a přihlášení

## 3. User stories

Uživatel bude mít přístup si hned vybrat nejlevnější produkt na trhu, zároveň si může nastavit upozornění na produkty a v případě, že cena klesne pod určitou hodnotu, uživatel dostane upozornění na whatsapp/telegram

1. Jako uživatel chci přidat produkt podle URL, abych začal sledovat jeho cenu.
2. Uživatel bude dostávat upozornění, tam kde je cena nejlevnější
3. Uživatel bude dostávat upozornění, tam kde je cena produktu, který si vybere nejlevnější, zároveň dostane srovnání mezi eshopy včetně dopravy
4. Uživatel si nastaví cílovou cenu a dostane upozornění, když se cena setká s jeho cílovou cenou

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
| id         | int     | id ceny                          |
| price      | int     | cena produktu                    |
| product_id | id      | ke kterému produktu se cena váže |
| date       | date    | čas, kdy byla cena scrapnuta     |
| in_stock   | boolean | je produkt na skladě?            |
| currency   | str     | měna                             |
| scraped_at | str     | webovka, kde se produkt našel    |

### Watch

| Pole          | Typ     | Popis                                                                 |
| ------------- | ------- | --------------------------------------------------------------------- |
| id            | Int     | ID jednoho watche ceny                                                |
| product_id    | Int     | K jakému productu se pricewatch váže?                                 |
| is_active     | Booelan | Běží hlídaní ceny?                                                    |
| target_price  | Int     | Když se sníží cena daného produktu, tak se pošle uživateli upozornění |
| last_notified | Date    | Poslední upozornění                                                   |

### Rozhodnutí

- Až si bude uživatle vybírat stránku a produkt, který tam chce sledovat, vybere si i měnu v jaké se produkt kupuje(default tam bude KČ)

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
