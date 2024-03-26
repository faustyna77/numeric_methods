def bisekcja(a,b,blad):
    def f(x):
         return -x**3+x+9
    
    

    if(f(a)*f(b)>=0):
        raise ArithmeticError("błąd")
    
    while(b-a)>blad:
        c=(a+b)/2
        if(f(c)==0):
            break
        elif(f(a)*f(c)<0):
            b=c
        else:
            a=c
    

    return (a+b)/2



print(bisekcja(0,100,0.01))