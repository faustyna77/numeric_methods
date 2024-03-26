

def f(x):
    return 4*x-3



def secant_method(f, x0, x1, epsilon=0.001, max_iterations=100):
     for i in range(max_iterations):
        # Obliczanie kolejnego przybliżenia
        x_next = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        
        # Sprawdzenie warunku stopu
        if abs(x_next - x1) < epsilon:
            return x_next
        
        # Aktualizacja punktów
        x0, x1 = x1, x_next


print(secant_method(f,0,8))