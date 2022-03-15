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
