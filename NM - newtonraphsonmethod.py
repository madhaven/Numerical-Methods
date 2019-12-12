from math import *
thefun = input("Enter function on x : ")
thefun2 = input("Enter the derivative function on x : ")
def f(x):
    return eval(thefun)#math.cos(x)-x*math.exp(x)
    #return exp(2*x)-x-6
def df(x):
    return eval(thefun2)
    #return 2*exp(2*x)-1

a, b=int(input("Enter a : ")), int(input('Enter b : '))
if f(a)<0:#negative fa
    print("fa={} negative".format(f(a)))
    while f(b)<0: #negative fb
        print('fb={} negative'.format(f(b)))
        if f(b)-f(a)>0:
            print('fb-fa>0, ', end=' ')
            a, b=b, b+b-a
            print('a and b = {} and {}'.format(a, b))
        else:
            print('fb-fa<=0, ', end=' ')
            a, b=a, b-2*(b-a)
            print('a and b = {} and {}'.format(a, b))
else:#positive fa
    print('fa={} positive'.format(f(a)))
    while f(b)>0: #positive fb
        print('fb={} positive'.format(f(b)))
        if f(b)-f(a)>0:
            print('fb-fa>0, ',end=' ')
            a,b=a,b-2*(b-a)
            print('a and b = {} and {}'.format(a, b))
        else :
            print('fb-fa<=0, ', end=' ')
            a, b=b, b+b-a
            print('a and b = {} and {}'.format(a, b))
#a, b=min(abs(a), abs(b)), max(abs(a), abs(b))
a=(a+b)/2
accuracy=4
n=0
x=a-1
print("\nRoot lies between {} and {}, closer to".format(a, b), end=' ')
if abs(f(a))<abs(f(b)):print(a)
else:print(b)
while (round(a, accuracy)!=round(x, accuracy)):
    print('x{} ='.format(n), round(a, accuracy))
    n+=1
    x=a
    a=a-f(a)/df(a)
input('press enter to quit')
