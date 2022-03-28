s = int(input('Введите число : '))
s = int(s)
c_s=s
result = 0 

while (s!=0):
    dig = s%10
    result = result*10 + dig
    s = int(s/10)

if (result == c_s):
    print('Palindrom! ')
else:
    print('NOT PALINDROM!')
