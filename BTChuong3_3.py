a=int(input('Tieu thu='))
p1=550
p2=750
p3=950
p4=1350
if 1<=a<=100:
    print('Phai tra='+str(p1*a+10/100*(p1*a)))
if 101<=a<=150:
    print('Phai tra='+str(p1*100+p2*(a-100)+10/100*(p1*100+p2*(a-100))))
if 151<=a<=200:
    print('Phai tra='+str(p1*100+p2*50+p3*(a-150)+10/100*(p1*100+p2*50+p3*(a-150)))) 
if 201<=a:
    print('Phai tra='+str(p1*100+p2*50+p3*50+p4*(a-200)+10/100*(p1*100+p2*50+p3*50+p4*(a-200))))           
