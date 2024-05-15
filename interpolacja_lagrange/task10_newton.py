import numpy as np
import matplotlib.pyplot as plt

# Punkty
points = [(1, 5), (2, 7), (3, 6)]

def divided_diff_table(points):
    """
    Tworzy tabelę różnic podzielonych dla zadanych punktów.
    
    :param points: Lista punktów (x_i, y_i).
    :return: Tablica różnic podzielonych.
    """
    n = len(points)
    diff_table = np.zeros((n, n))
    for i in range(n):
        diff_table[i][0] = points[i][1]
    
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = (diff_table[i + 1][j - 1] - diff_table[i][j - 1]) / (points[i + j][0] - points[i][0])
    
    return diff_table

def newton_interpolation(x, points, diff_table):
    """
    Funkcja do interpolacji Newtona.
    
    :param x: Punkt, w którym obliczamy wartość wielomianu.
    :param points: Lista punktów (x_i, y_i).
    :param diff_table: Tablica różnic podzielonych.
    :return: Wartość wielomianu w punkcie x.
    """
    n = len(points)
    result = diff_table[0][0]
    product_term = 1.0
    
    for i in range(1, n):
        product_term *= (x - points[i - 1][0])
        result += diff_table[0][i] * product_term
    
    return result

# Obliczanie tablicy różnic podzielonych
diff_table = divided_diff_table(points)

# Testowanie funkcji w kilku punktach
x_values = np.linspace(0, 4, 100)
y_values = [newton_interpolation(x, points, diff_table) for x in x_values]

# Wizualizacja
plt.plot(x_values, y_values, label='Interpolacja Newtona')
plt.scatter(*zip(*points), color='red', zorder=5, label='Punkty')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolacja Newtona')
plt.grid(True)
plt.show()
