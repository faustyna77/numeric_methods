import numpy as np

# Definicja punktów
x = np.array([0, 3, 6, 9, 12])
y = np.array([4, 5, 4, 1, 2])

# Tworzenie macierzy Vandermonde'a
A = np.vander(x, 4)

# Rozwiązanie układu równań
coefficients = np.linalg.lstsq(A, y, rcond=None)[0]

# Wyświetlenie współczynników
print("Współczynniki wielomianu:", coefficients)

# Definicja funkcji aproksymującej
def P(x):
    return coefficients[0]*x**3 + coefficients[1]*x**2 + coefficients[2]*x + coefficients[3]

# Wyświetlenie wielomianu
print(f"Funkcja aproksymująca: P(x) = {coefficients[0]}x^3 + {coefficients[1]}x^2 + {coefficients[2]}x + {coefficients[3]}")

# Przykładowe wartości funkcji aproksymującej
import matplotlib.pyplot as plt

x_vals = np.linspace(0, 12, 100)
y_vals = P(x_vals)

plt.scatter(x, y, color='red', label='Punkty danych')
plt.plot(x_vals, y_vals, label='Wielomian aproksymujący')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Aproksymacja wielomianowa stopnia 3')
plt.show()
