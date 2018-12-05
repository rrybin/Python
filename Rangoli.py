import string
n = 3
m = n * 3
c = '-'

abc = string.ascii_lowercase
print(abc)

# for x in range(n,0,-1):
#     s = ''
#     for i in range(96+n,95+x,-1):
#         s += chr(i)
#     for i in range(97+x, 97+n):
#         s += chr(i)
#     print(s)
# s = ''
# b = ''
# for x in range(n,0,-1):
#     s = abc[x-1:n]
#     b = ''
#     for t in range(len(s),1,-1):
#         b += s[t-1]
#     s = b + s
#     print(s)
# b=''
# for t in s:
#    b += t + c
# print(b)
import string
alpha = string.ascii_lowercase

L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print('\n'.join(L[:0:-1]+L))