print('General equation format : ax+by+cz=d')
a1=float(input('Enter value for a1 : '))
b1=float(input('Enter value for b1 : '))
c1=float(input('Enter value for c1 : '))
d1=float(input('Enter value for d1 : '))
a2=float(input('Enter value for a2 : '))
b2=float(input('Enter value for b2 : '))
c2=float(input('Enter value for c2 : '))
d2=float(input('Enter value for d2 : '))
a3=float(input('Enter value for a3 : '))
b3=float(input('Enter value for b3 : '))
c3=float(input('Enter value for c3 : '))
d3=float(input('Enter value for d3 : '))
prec=int(input('Enter precision : '))
x=y=z=0
xx=yy=zz=0
n=1
while True:
    x=round((1/a1)*(d1-b1*yy-c1*zz), prec)
    print('\nx', n, ' : ', x, sep='')
    y=round((1/b2)*(d2-a2*xx-c2*zz), prec)
    print('y', n, ' : ', y, sep='')
    z=round((1/c3)*(d3-a3*xx-b3*yy), prec)
    print('z', n, ' : ', z, sep='')
    if ((x==xx) and (y==yy) and (z==zz)):
        break
    xx, yy, zz=x, y, z
    n+=1
