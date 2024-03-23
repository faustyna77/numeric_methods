def horner(wspolczynniki, x):
    # Inicjalizacja wartości wielomianu na wartość pierwszego współczynnika
    wartosc = wspolczynniki[0]

    # Iteracja przez pozostałe współczynniki i zastosowanie schematu Hornera
    for i in range(1, len(wspolczynniki)):
        # Mnożenie aktualnej wartości przez x i dodanie kolejnego współczynnika
        wartosc = wartosc * x + wspolczynniki[i]

    # Zwrócenie obliczonej wartości wielomianu dla x
    return wartosc

# Pobranie stopnia wielomianu od użytkownika
stopienWielomianu = int(input("Podaj stopień wielomianu: "))

# Inicjalizacja listy współczynników
wspolczynniki = []

# Pobranie współczynników wielomianu od użytkownika
print("Podaj współczynniki wielomianu od najwyższej potęgi: ")
for i in range(stopienWielomianu + 1):
    wsp = int(input())
    wspolczynniki.append(wsp)

# Pobranie wartości x, dla której chcemy obliczyć wartość wielomianu
x = int(input("Podaj wartość w punkcie x: "))

# Wyświetlenie współczynników wielomianu
print("Wspołczynniki: ", wspolczynniki)

# Obliczenie i wyświetlenie wartości wielomianu dla x
wartosc = horner(wspolczynniki, x)
print("Wartość wielomianu dla x =", x, "wynosi", wartosc)
