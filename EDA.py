import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("SuperStoreOrders.csv", sep=";")


# 2 Podstawowe informacje
print('\n' + '='*50)
print(f'Wymiary danych: {df.shape}')
print(f'Liczba wierszy: {df.shape[0]}')
print(f'Liczba kolumn: {df.shape[1]}')

#3 Podgląd danych
print('\n' + '='*50)
print('Pierwsze 5 zamówień:')
print(df.head())

print('\nOstatnie 5 zamówień:')
print(df.tail())

#4Typy danych
print('\n' + '='*50)
print(df.info())
print(f'\n{df.describe()}')

#5 Analiza duplikatów
print('\n' + '='*50)
print("ANALIZA DUPLIKATÓW")
print("="*50)

duplikaty =df.duplicated()
print(duplikaty)
if duplikaty.sum() > 0:
    print(f'Znaleziono {duplikaty} zduplikowanych wierszy')
    print('zduplikowane wiersze: ')
    print(df[duplikaty])
else:
    print('Brak duplikatów')

#6 Brakujące wartości
print('\n' + '='*50)
print("BRAKUJĄCE WARTOŚCI")
print("="*50)

brakujace=df.isnull().sum()
if brakujace.sum() > 0:
    print('Kolumny z brakujacymi wartosciami: ')
    for kolumna in df.columns:
        if df[kolumna].isnull().sum() >0:
            braki_liczbowe =df[kolumna].isnull().sum()
            braki_procentowe= (braki_liczbowe/ len(df)*100)
            print(f' {kolumna}: {braki_liczbowe} ({braki_procentowe: .1f}%)')
else:
    print("Brak brakujących danych")


#Usuniecie brakujących wartości
df = df.dropna(subset=["category", "sub_category"])
print("Usunięto brakujące wartości")

#7 Czyszczenie danych i zmiana typu danych

df["order_date"] = pd.to_datetime(df["order_date"], dayfirst=True)
df["ship_date"] = pd.to_datetime(df["ship_date"], dayfirst=True)

df["sales"] = df["sales"].str.replace(",", "").astype(float)

#8 inżynieria cech (Feature Engineering)

df["ship_time"] = (df["ship_date"] - df["order_date"]).dt.days
df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month

#9 Statystyki numeryczne
print("STATYSTYKI NUMERYCZNE")
print("="*50)
kolumny_numeryczne=df.select_dtypes(include='number').columns
print(kolumny_numeryczne)

if len(kolumny_numeryczne)>0:
    print('\nStatystyki dla ocen numerycznych: ')
    print(df[kolumny_numeryczne].describe())
else:
    print('Brak kolumn numerycznych')

#10 Statystyki kategoryczne
print("STATYSTYKI KATEGORYCZNE")
print("="*50)

kolumny_tekstowe =df.select_dtypes(include='object').columns
if len(kolumny_tekstowe)>0:
    for kolumna in kolumny_tekstowe:
        print(f'\nKolumna {kolumna}')
        print(f'Liczba unikalnych wartości: {df[kolumna].nunique()}')
        print(' 4 najczęstsze wartości')
        print(df[kolumna].value_counts().head(4))
else:
    print('Brak kolumn kategorycznych w danych')

#11 Outliery
print('\n' + '='*50)
print("ANALIZA OUTLIERÓW")
print("="*50)

if len(kolumny_numeryczne) >= 0:
    for kolumna in  kolumny_numeryczne:
        Q1= df[kolumna].quantile(0.25)
        Q3= df[kolumna].quantile(0.75)
        IQR = Q3 - Q1
        dolna_granica =Q1 -1.5 * IQR
        gorna_granica = Q3 + 1.5 * IQR

        outliers = df[(df[kolumna] < dolna_granica) | (df[kolumna] > gorna_granica)]
        print(f'Outliery w {kolumna}: {outliers}')
        print(f"{kolumna}: {len(outliers)} ({len(outliers) / len(df) * 100:.2f}%)")


#12 WIZUALIZACJE
print('\n' + '='*50)
print("WIZUALIZACJE")
    #1 Wykres - Rozkład sprzedaży
sns.histplot(df["sales"], bins=100, kde=True)
plt.title("Rozkład sprzedaży")
plt.xlabel("Sprzedaż")
plt.ylabel("Liczba")
plt.show()
 #2 Wykres -  Rozkład sprzedaży - skala logarytmiczna
plt.figure(figsize=(10,6))
sns.histplot(df["sales"], bins=100, kde=True, color="lightblue")
plt.xscale("log")
plt.title("Rozkład sprzedaży (skala log)")
plt.xlabel("Sprzedaż")
plt.ylabel("Liczba")
plt.show()

 #3 Wykres - Analiza sprzedaży w czasie
df.groupby("order_date")["sales"].sum().plot(figsize=(12,5), color="salmon", linewidth=2)
plt.title("Sprzedaż w czasie")
plt.xlabel("Data")
plt.ylabel("Sprzedaż")
plt.show()
 #4 Wykres - Analiza sprzedaży w miesiącach
df.groupby("month")["sales"].sum().plot(kind="bar", color="lightgreen", edgecolor="k", figsize=(10,6), linewidth=1)
plt.title("Sprzedaż w miesiącu", fontsize=12)
plt.xlabel("Miesiąc")
plt.ylabel("Suma sprzedaży [mln]")
plt.grid(alpha=0.3, axis="y")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

 #5 Wykres -  Zysk w kategoriach
profit_per_category = df.groupby("category")["profit"].sum()/ 1_000_000
profit_per_category.plot(kind="bar",figsize=(10,6), color = ["darkblue","blue", "lightblue"], edgecolor="k", linewidth=1)
plt.title("Zysk w kategoriach")
plt.xlabel("Kategoria")
plt.xticks( rotation=0, fontsize=8)
plt.ylabel("Zysk [mln]")
plt.show()

#6 Wykres -  Zysk w podkategoriach
profit_per_subcategory = df.groupby("sub_category")["profit"].sum()
profit_per_subcategory = profit_per_subcategory.sort_values()
df.groupby("sub_category")["profit"].sum().sort_values().plot(kind="barh")
plt.title("Zysk w podkategoriach", fontsize=12)
plt.xlabel("Zysk")
plt.ylabel("Podkategorie")
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.show()
plt.show()

 #7 Wykres -wpływ rabatu na zysk -  relacje między zmiennymi
plt.figure(figsize=(10,6))

sns.regplot(
    x="discount",
    y="profit",
    data=df,
    scatter_kws={"alpha": 0.3},
    line_kws={"color": "darkblue", "linewidth": 2}
)

plt.title("Wpływ rabatu na zysk", fontsize=12)
plt.xlabel("Rabat")
plt.ylabel("ZYsk")

plt.grid(alpha=0.3)
plt.show()


 #8 Wykres -  Zysk a region
region_profit = df.groupby("region")["profit"].sum().sort_values()

plt.figure(figsize=(10,8))

region_profit.plot(
    kind="bar",
    color="teal",
    edgecolor="black"
)

plt.title("Zysk a region", fontsize=12)
plt.xlabel("Region")
plt.ylabel("Zysk")
plt.xticks(rotation=45, fontsize=8)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

 #9 Wykres -  Sprzedaż w top 10 krajach
top_countries=df.groupby("country")["sales"].sum().sort_values(ascending=False).head(10)
top_countries.plot(kind="bar", color="steelblue", linewidth=2)
plt.title("Sprzedaż w top 10 krajach ", fontsize=12)
plt.xlabel("Kraje")
plt.ylabel("Spredaż [mln]")
plt.xticks(rotation=45)
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.show()

 #10 Wykres -  Sprzedaż według segmentu klientów
segment_sales=df.groupby("segment")["sales"].sum()
segment_sales.plot(kind="bar", color=["darkblue","blue", "lightblue"])
plt.title("Sprzedaż według segmentu klientów")
plt.xlabel("Segment")
plt.ylabel("Sprzedaż [mln]")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

 #11 Wykres -  Zysk według segmentu klientów
segment_profit=df.groupby("segment")["profit"].sum()/1000
segment_profit.plot(kind="bar",color=["darkblue","blue", "lightblue"])
plt.title("Zysk według segmentu klientów", fontsize=12)
plt.xlabel("Segment")
plt.ylabel("Zysk [tyś.]")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

 #12 Wykres - Wielkość sprzedaży 10 najlepiej sprzedających się produktów
top10 = (
    df.groupby("product_name")["sales"]
    .sum()
    .sort_values(ascending=True)
    .tail(10)
)
def get_color(value):
    if value <= 45000:
        return "lightblue"
    elif value <= 60000:
        return "blue"
    else:
        return "darkblue"

colors = [get_color(v) for v in top10]

plt.figure(figsize=(10, 8))
bars = top10.plot(kind="barh", color=colors)

plt.title("Top 10 produktów", fontsize=12)
plt.xlabel("Sprzedaż")
plt.ylabel("Nazwa produktu")

# dodanie wartości na końcu słupków
for i, value in enumerate(top10):
    plt.text(
        value,
        i,
        f"{round(value/1000)} tyś.",
        va="center",
        fontsize=8
    )

plt.tight_layout()
plt.show()

 #13 Wykres - Czas dostawy vs tryb wysyłki
plt.figure(figsize=(10, 6))

sns.boxplot(x="ship_mode", y="ship_time", data=df)

plt.title("Czas dostawy vs tryb wysyłki", fontsize=12)
plt.xlabel("Tryb wysyłki")
plt.ylabel("Czas dostawy (dni)")

plt.xticks(rotation=20)
plt.tight_layout()
plt.show()


 #14 Wykres - macierz korelacji
macierz_korelacji = df[["sales","profit","discount","quantity","shipping_cost"]].corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    macierz_korelacji,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    center=0,
    linewidths=0.5
)

plt.title("Macierz korelacji", fontsize=12)
plt.tight_layout()
#plt.show()


###########
print("\n=== ISTOTNE KORELACJE ===")

threshold = 0.3

for i in range(len(macierz_korelacji.columns)):
    for j in range(i + 1, len(macierz_korelacji.columns)):
        kol1 = macierz_korelacji.columns[i]
        kol2 = macierz_korelacji.columns[j]
        korelacja = macierz_korelacji.iloc[i, j]

        if abs(korelacja) < threshold:
            continue

        # siła
        if abs(korelacja) >= 0.7:
            sila = "BARDZO SILNA"
        elif abs(korelacja) >= 0.5:
            sila = "SILNA"
        else:
            sila = "UMIARKOWANA"

        # kierunek
        if korelacja > 0:
            kierunek = "dodatnia"
        else:
            kierunek = "ujemna"

        print(f"{kol1} vs {kol2}: {korelacja:.2f} ({sila}, {kierunek})")
plt.show()

  #15 Wykres -  Heatmap: region vs category
pivot = df.pivot_table(values="sales", index="region", columns="category", aggfunc="sum")

plt.figure(figsize=(10, 6))

sns.heatmap(
    pivot,
    annot=True,
    fmt=",.0f",
    cmap="Blues",
    linewidths=0.5,
    linecolor="gray"
)

plt.title("Sprzedaż: Region vs Kategoria", fontsize=12)
plt.xlabel("Kategoria")
plt.ylabel("Region")

plt.xticks(rotation=30)
plt.yticks(rotation=0)

plt.tight_layout()
plt.show()

 #16 Wykres - Boxplot: profit per category
plt.figure(figsize=(10, 6))

sns.boxplot(
    x="category",
    y="profit",
    data=df,
    width=0.6
)

plt.title("Rozkład zysku w kategoriach", fontsize=14)
plt.xlabel("Kategoria")
plt.ylabel("Zysk")

plt.xticks(rotation=20)
plt.tight_layout()
plt.show()


#13 Podsumowanie
print('\n' + '='*50)
print("PODSUMOWANIE ANALIZY")
print("="*50)

print("Analiza EDA zakończona pomyślnie")
print(f'Przeanalizowano {len(df)} zamówień')
