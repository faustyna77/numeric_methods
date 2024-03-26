def hornerFunc(wspolczynniki,x):
    wartosc=wspolczynniki[0]

    for i in range(1,len(wspolczynniki)):
        wartosc=wartosc*x+wspolczynniki[i]
    return wartosc



x=int(input("podaj punkt w którym chcesz obliczyć wartośc wielomianu"))

t=int(input("podaj stopień wielomianu"))


wspolczynniki=[]

for i in range(t+1):
    wsp=int(input())
    wspolczynniki.append(wsp)



print(hornerFunc(wspolczynniki,x))