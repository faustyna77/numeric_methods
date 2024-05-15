import math

def falsi(f, a, b, epsilon=0.0001, iterations=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Brak zmiany znaku funkcji w przedziale")
    
    for i in range(iterations):
        xn = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if abs(f(xn)) < epsilon:
            return xn
        if f(xn) * f(a) < 0:
            b = xn
        else:
            a = xn
    
    raise ValueError("Nie osiągnięto wymaganej dokładności w zadanej liczbie iteracji")

def f(x):
    return 3 * x - math.cos(x) - 1

print(falsi(f, 0.25, 0.75))
