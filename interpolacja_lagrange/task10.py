import numpy as np
import matplotlib.pyplot as plt

# Punkty
points = [(1, 5), (2, 7), (3, 6)]

def lagrange_interpolation(x, points):
    """
    Funkcja do interpolacji Lagrange'a.
    
    :param x: Punkt, w którym obliczamy wartość wielomianu.
    :param points: Lista punktów (x_i, y_i).
    :return: Wartość wielomianu w punkcie x.
    """
    result = 0
    n = len(points)
    
    for i in range(n):
        xi, yi = points[i]
        li = 1
        
        for j in range(n):
            if i != j:
                xj, yj = points[j]
                li *= (x - xj) / (xi - xj)
        
        result += yi * li
    
    return result

# Testowanie funkcji w kilku punktach
x_values = np.linspace(0, 4, 100)
y_values = [lagrange_interpolation(x, points) for x in x_values]

# Wizualizacja
plt.plot(x_values, y_values, label='Interpolacja Lagrange\'a')
plt.scatter(*zip(*points), color='red', zorder=5, label='Punkty')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolacja Lagrange\'a')
plt.grid(True)
plt.show()
