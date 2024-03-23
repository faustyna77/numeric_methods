def hornerDzielenie(wspolczynniki, x, stopienWielomianu):
    # Inicjalizacja pustej listy na wyniki dzielenia wielomianu przez dwumian
    wynik = []

    # Iteracja po stopniu wielomianu
    for i in range(stopienWielomianu + 1):
        # Obliczenie nowego współczynnika wielomianu wynikowego
        wartosc = wspolczynniki[i] + x * (wynik[-1] if wynik else 0)
        wynik.append(wartosc)

    # Zwrócenie listy zawierającej współczynniki wynikowego wielomianu oraz resztę z dzielenia
    return wynik

# Pobranie stopnia wielomianu od użytkownika
stopienWielomianu = int(input("Podaj stopień wielomianu: "))

# Inicjalizacja listy współczynników
wspolczynniki = []

# Pobranie współczynników wielomianu od użytkownika
print("Podaj współczyyniki wielomianu od najwyższej potęgi: ")
for i in range(stopienWielomianu + 1):
    wsp = int(input())
    wspolczynniki.append(wsp)

# Pobranie liczby, przez którą będzie dzielony wielomian
x = int(input("Podaj liczbę przez którą będziemy dzielić wielomian: "))

# Wywołanie funkcji dzielącej wielomian przez dwumian i zapisanie wyniku w zmiennej wynik
wynik = hornerDzielenie(wspolczynniki, x, stopienWielomianu)

# Wyświetlenie współczynników ilorazu (wszystko oprócz ostatniego elementu listy wynik)
print("Współczynniki dzielenia:", wynik[:-1])

# Wyświetlenie reszty z dzielenia (ostatni element listy wynik)
print("Reszta dzielenia:", wynik[-1])
