def bisekcja(a,b,bladE):
    def f(x):
        return x**3+5*x+8
    

    if((f(a)*f(b))>0):
        raise ArithmeticError ("bład ")
    while((b-a)>bladE):
        c=(a+b)/2
        if(f(c)==0):
            break
        if(f(a)*f(c))<0:
            b=c
        else:
            a=c
    return (a+b)/2
