from math import *
thefun = input("Enter function on x : ")
thefun2 = input("Enter the suitable phi function on x : ")
def f(x):
    return eval(thefun)
def fi(x):
    return eval(thefun2)
a, b=int(input('Enter value for a : ')), int(input('Enter value for b : '))
if f(a)<0:#negative fa
    while f(b)<0: #negative fb
        if f(b)-f(a)>0:
            a, b=b, b+b-a
        else:
            a, b=a, b-2*(b-a)
else:#positive fa
    while f(b)>0: #positive fb
        if f(b)-f(a)>0:
            a,b=a,b-2*(b-a)
        else :
            a, b=b, b+b-a
#a, b=min(abs(a), abs(b)), max(abs(a), abs(b))
a=(a+b)/2
accuracy=4
n=0
x=a-1
print("Root lies between {} and {}, closer to".format(a, b), end=' ')
if abs(f(a))<abs(f(b)):print(a)
else:print(b)
while (round(a, accuracy)!=round(x, accuracy)):
    print('x{} ='.format(n), round(a, accuracy))
    n+=1
    x=a
    a=fi(a)
input('Press enter to quit')
