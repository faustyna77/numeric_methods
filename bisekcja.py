def bisekcja(a,b,e):


    def f(x):
        return x**3+x-8
    
    while(f(a)*f(b)>=0):
        raise ArithmeticError("niespełnione załozenia")
    

    