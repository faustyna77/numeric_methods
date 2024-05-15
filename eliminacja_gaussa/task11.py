import numpy as np

def gaussian_elimination(A, b):
    n = len(b)
    # Tworzenie rozszerzonej macierzy
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    # Forward elimination
    for i in range(n):
        # Szukamy maksymalnego elementu w kolumnie do pivotowania
        max_row = i + np.argmax(np.abs(Ab[i:, i]))
        Ab[[i, max_row]] = Ab[[max_row, i]]  # Zmiana miejscami wierszy
        
        # Normalizujemy wiersz, aby wiodący element był równy 1
        Ab[i] = Ab[i] / Ab[i, i]
        
        # Eliminujemy elementy poniżej wiodącego elementu
        for j in range(i + 1, n):
            Ab[j] = Ab[j] - Ab[j, i] * Ab[i]
    
    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:n])
    
    return x

# Przykład
A = np.array([[2, 3, 1],
              [4, 1, 2],
              [3, 2, 3]], dtype=float)
b = np.array([1, 2, 3], dtype=float)

rozwiązanie = gaussian_elimination(A, b)
print("Rozwiązanie:", rozwiązanie)
