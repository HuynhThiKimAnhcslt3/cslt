ten=input('Ho ten: ')
so_ngay_cong=int(input('So ngay cong: '))
don_gia_ngay_cong=int(input('Don gia ngay cong: '))
he_so_phu_cap=float(input('He so phu cap: '))
tien_tam_ung=int(input('Tam ung: '))
import math
luong=don_gia_ngay_cong*so_ngay_cong*he_so_phu_cap
thuc_linh=luong-tien_tam_ung
print('Nhan vien ' +  str(ten) + ', Co tien luong='+str(luong) + ', Tam ung='+str(tien_tam_ung) + ' va Thuc Linh='+str(round(thuc_linh,1)))
