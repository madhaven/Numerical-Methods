print('General equation format : aw+bx+cy+dz=e')
a1=float(input('Enter value for a1 : '))
b1=float(input('Enter value for b1 : '))
c1=float(input('Enter value for c1 : '))
d1=float(input('Enter value for d1 : '))
e1=float(input('Enter value for e1 : '))
a2=float(input('Enter value for a2 : '))
b2=float(input('Enter value for b2 : '))
c2=float(input('Enter value for c2 : '))
d2=float(input('Enter value for d2 : '))
e2=float(input('Enter value for e2 : '))
a3=float(input('Enter value for a3 : '))
b3=float(input('Enter value for b3 : '))
c3=float(input('Enter value for c3 : '))
d3=float(input('Enter value for d3 : '))
e3=float(input('Enter value for e3 : '))
a4=float(input('Enter value for a4 : '))
b4=float(input('Enter value for b4 : '))
c4=float(input('Enter value for c4 : '))
d4=float(input('Enter value for d4 : '))
e4=float(input('Enter value for e4 : '))
prec=int(input('Enter precision : '))
w=x=y=z=0
ww=xx=yy=zz=0
n=1
while True:
    w=round((1/a1)*(e1-b1*xx-c1*yy-d1*zz), prec)
    print('\nw', n, ' : ', w, sep='')
    x=round((1/b2)*(e2-a1*ww-c2*yy-d2*zz), prec)
    print('x', n, ' : ', x, sep='')
    y=round((1/c3)*(e3-a3*ww-b3*xx-d3*zz), prec)
    print('y', n, ' : ', y, sep='')
    z=round((1/d4)*(e4-a4*ww-b4*xx-c3*yy), prec)
    print('z', n, ' : ', y, sep='')
    if ((x==xx) and (y==yy) and (z==zz) and (w==ww)):
        break
    ww, xx, yy, zz=w, x, y, z
    n+=1
