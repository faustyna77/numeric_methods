def Bisekcja(a,b,blad):


#funkcja dla której liczone sa miejsca zerowe
    def f(x):
        return -x**3+x+9
    

    # warunek bisekcji
    if(f(a)*f(b)>=0):
        raise ArithmeticError("niespełnione załozenia")
    while(b-a)>blad:
        c=(a+b)/2
        if(f(c)==0):
            break
        elif(f(a)*f(c)<0):
            b=c
        else:
            a=c
    return (a+b)/2




try:
    wynik = Bisekcja(0, 100, 0.01)
    print("Pierwiastek wielomianu:", wynik)
except ArithmeticError as e:
    print("Błąd:", e)
        

        
    
    

