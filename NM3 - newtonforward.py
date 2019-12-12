from math import *

def fact(x):
    if x==1: return 1
    else: return x*fact(x-1)

n=int(input('Enter number of observations : '))
prec=int(input('decimal precision : '))
thedict={float(input('Enter x%d : '%(x))):float(input('Enter y%d : '%(x))) for x in range(n)}
h=list(thedict.keys())[1]-list(thedict.keys())[0] #print(h)
f, delta, p, fx='', [], 1, 0

for x in range(2, n): #print(list(thedict.keys())[x], list(thedict.keys())[x-1])
    if (list(thedict.keys())[x]-list(thedict.keys())[x-1])!=h:
        print('Uneven data intervals are not supported.')
        input()
        exit()
if h==0:
    print('No notable interval')
    input()
    exit()

print('\nData received')
for x in thedict.keys(): print(x, ':', thedict[x])
print()

delta.insert(0, [thedict[list(thedict.keys())[y]]-thedict[list(thedict.keys())[y-1]] for y in range(1, n)])
for x in range(1, n):
    delta.insert(len(delta), [delta[len(delta)-1][y]-delta[len(delta)-1][y-1] for y in range(1, len(delta[len(delta)-1]))])
for x in range(n-1):
    print('delta^%d'%(x+1))
    for y in delta[x]:print(round(y, prec))

while(True):
    try:f=float(input('\nEnter value of x : '))
    except:
        if f=='': exit()
    p=(f-list(thedict.keys())[0])/h
    print('x :', f); print('x0 :', list(thedict.keys())[0]); print('h :', h); print('p :', p);print()

    fx=list(thedict.values())[0]; print(fx)
    for x in range(1, n-1):
        thep=1
        for y in range(x):
            thep*=(p-y)
        print(round(thep*delta[x-1][0]/fact(x), prec))
        fx+=thep*delta[x-1][0]/fact(x)

    print('f(%d) ='%(f), round(fx, prec))
    f=''
