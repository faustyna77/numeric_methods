import math

def f(x):
    return math.sin(x)-0.5*x

def df(x):
    return math.cos(x)-0.5


def styczne(x0,e):
     xn=x0
     while True:
        x_next = xn - f(xn) / df(xn)
        if abs(x_next - xn) < e:
            return x_next
        xn = x_next



x0=math.pi
e=0.01
print(styczne(x0,e))

     

    
   
