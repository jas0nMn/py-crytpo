#Caesar cipher
p = input()
c=''
for i in range(len(p)):
    if p[i].isalpha():
        c+=chr(ord(p[i])+3)
    else:
        c+=p[i]
print(c)
p=''
for i in range(len(c)):
    if c[i].isalpha():
        p+=chr(ord(c[i])-3)
    else:
        p+=c[i]
print(p)

#維吉尼亞密碼
def hash(input):
    hash_number=512
    for char in input:
        hash_number*=ord(char)
        hash_number+=3
        hash_number%=1024
    hash_number*=len(input)
    hash_number%=1024
    return hash_number
print(hash('hello world'))
print(hash('hello'))

#xor
def bytes_to_int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result
P=b"hello"
key=b"ctf"
P=(bytes_to_int(P))[2:-1]
key=(bytes_to_int(key))[2:-1]

for i in (bin(P)[2:-1]):
    

