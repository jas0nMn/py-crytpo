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
