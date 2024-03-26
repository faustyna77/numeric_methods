import math 


def f(x):
    return math.sin(x)-x


def df(x):
    return math.cos(x)-1


def styczne(x0,n):
    xn=x0
    while True:
        x_next=xn- f(xn)/df(xn)
        if((x_next-xn )<n):
            return x_next
        xn=x_next
        
    
print(math.pi,0.01)