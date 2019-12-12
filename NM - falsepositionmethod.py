from math import *
thefun = input("Enter function on x : ")
def f(x):
    return eval(thefun)
def fp(a, b):
    return a-((b-a)/(f(b)-f(a)))*f(a)
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
a, b=min(a, b), max(a, b)
x=fp(a, b)
accuracy=4
w=0
n=1
print("Root lies between {} and {}".format(a, b))
print("n\ta\tf(a)\tb\tf(b)\txn\tf(xn)\n")
while (round(w, accuracy)!=round(x, accuracy)):
    w=x
    print(n, round(a, accuracy), round(f(a), accuracy), round(b, accuracy), round(f(b), accuracy),round(x, accuracy), round(f(x), accuracy), sep='\t')
    if (f(a)>0) == (f(x)>0):a=x
    else:b=x
    n+=1
    x=fp(a, b)
input("Press enter to quit")
