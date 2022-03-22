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
