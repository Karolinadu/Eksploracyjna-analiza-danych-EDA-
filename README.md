# Analiza danych sprzedażowych SuperStore | Eksploracyjna analiza danych (EDA)

Projekt eksploracyjnej analizy danych wykonany w Pythonie. Obejmuje analizę sprzedaży, rentowności, segmentów klientów i zamówień w zbiorze danych sklepu detalicznego.

## Cel projektu

Celem projektu jest poznanie struktury danych zamówień SuperStore, ocena jakości danych oraz wizualizacja wskaźników biznesowych, które mogą pomóc wskazać obszary wymagające dalszej analizy. Jest to projekt edukacyjny przygotowany do portfolio, a nie produkcyjny system raportowania.

## Pytania analityczne

- Jak zmienia się sprzedaż w czasie i w poszczególnych miesiącach?
- Które kategorie i podkategorie produktów mają największy udział w zysku?
- Jak różnią się sprzedaż i rentowność pomiędzy segmentami klientów oraz obszarami geograficznymi?
- Jakie zależności można zaobserwować między rabatami, zyskiem i czasem realizacji zamówień?

## Wykorzystane technologie

- **Python** - przetwarzanie danych i analiza eksploracyjna
- **Pandas i NumPy** - przegląd, czyszczenie i przekształcanie danych
- **Matplotlib i Seaborn** - wizualizacja danych

## Etapy analizy

1. **Wczytanie i poznanie danych:** sprawdzenie liczby rekordów, kolumn, typów danych oraz statystyk opisowych.
2. **Kontrola jakości danych:** identyfikacja duplikatów, brakujących wartości i potencjalnych obserwacji odstających z wykorzystaniem metody IQR (rozstępu międzykwartylowego).
3. **Przygotowanie danych:** obsługa braków w kategoriach i podkategoriach, konwersja dat i pól sprzedażowych oraz utworzenie zmiennych `ship_time`, `year` i `month`.
4. **Analiza wskaźników biznesowych:** badanie sprzedaży i zysku w podziale na okresy, kategorie produktów oraz inne wymiary biznesowe.
5. **Wizualizacja:** przygotowanie wykresów rozkładów, trendów czasowych i porównań między kategoriami.

## Struktura repozytorium

```text
.
├── EDA.py                 # Kod analizy i wizualizacji w Pythonie
├── SuperStoreOrders.csv   # Zbiór danych wejściowych
└── README.md              # Dokumentacja projektu
```

## Jak uruchomić projekt?

1. Sklonuj lub pobierz repozytorium.
2. Zainstaluj wymagane biblioteki:

   ```bash
   pip install pandas numpy matplotlib seaborn
   ```

3. Uruchom skrypt w katalogu repozytorium:

   ```bash
   python EDA.py
   ```

Skrypt wczytuje plik `SuperStoreOrders.csv`, wykorzystując średnik (`;`) jako separator. Wyświetla informacje o danych, wyniki analiz oraz wykresy. W zależności od środowiska uruchomieniowego zamknięcie okna wykresu może być konieczne do kontynuowania działania skryptu.

## Interpretacja i ograniczenia

Projekt przedstawia proces analizy eksploracyjnej, a nie zweryfikowany model wspierania decyzji biznesowych. Wykresy służą do identyfikacji wzorców i formułowania pytań do dalszej analizy; nie stanowią dowodu zależności przyczynowo-skutkowych. Obserwacje odstające są wskazywane do weryfikacji, a nie automatycznie uznawane za błędne.

**Możliwe dalsze kroki:** dodanie sekcji z wynikami liczbowymi i rekomendacjami biznesowymi po ich weryfikacji, zapis wybranych wykresów do plików oraz dopracowanie kontroli jakości danych i opisów osi. W dokumentacji celowo nie podano niezweryfikowanych wyników liczbowych.

## Autorka

**Karolina Dudek**  
[Profil GitHub](https://github.com/Karolinadu)
