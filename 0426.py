import gmpy2
#1 隨意選擇兩個大的質數p和q，p不等於q，計算N=p*q;
p = 3
q = 5
N = p*q
print(f'{p}x{q}={N}')

#2 根據歐拉函數取得
phi = (p-1)*(q-1)
e=7
print(f'GCD({e},{phi})={gmpy2.gcd(e,phi)}')
d=gmpy2.invert(e,phi)
print(f'{e}*{d}%{phi}={e*d%phi}')
print(d)

P=87
print(P)
print(C :=pow(P,e,N))        #P的e次方 mod N
print(pow(C,d,N))

#加密 : M ^ e = C(mod N)
#解密 : C ^ d = M(mod N)
#公鑰 : (N , e)
#私鑰 : (N , d)
