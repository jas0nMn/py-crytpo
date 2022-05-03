import gmpy2
#1 隨意選擇兩個大的質數p和q，p不等於q，計算N=p*q;
p = 473398607161
q = 4511491
e = 17
N = p*q
print(f'{p}x{q}={N}')
#2 根據歐拉函數取得
phi = (p-1)*(q-1)
print('phi = ',phi)
d=gmpy2.invert(e,phi)       #e*d%phi==1,
print('d = ',d)
M = 3        #密文
print('M = ',M)         
print('C = ',C :=pow(M,e,N))           #加密
print('M = ',M :=pow(C,d,N))           #解密
#M的e次方 mod N
#加密 : M ^ e = C(mod N)
#解密 : C ^ d = M(mod N)
#公鑰 : (N , e)
#私鑰 : (N , d)
# C(密文),M(明文)
