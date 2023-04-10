x=float(input('x='))
y=float(input('y='))
a='+'
b='-'
c='*'
d='/'
ch=input('Phep toan:')
import math
if ch==a or ch==b or ch==c or ch==d:      
    if ch==a:
        print(str(x)+'+'+str(y)+'='+str(round(x+y,1)))
    elif ch==b:
        print(str(x)+'-'+str(y)+'='+str(round(x-y,1)))
    elif ch==c:
        print(str(x)+'*'+str(y)+'='+str(round(x*y,1)))
    elif ch==d:
        if y==0:
            print('Khong hop le')
        else:
            print(str(x)+'/'+str(y)+'='+str(round(x/y,1)))
else:
    print('Khong hop le')
       