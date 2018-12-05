#import string
#s = 'chris alan'
#print(string.capwords(s,sep=' '))

##Merge the Tools!
# s = 'AABCAAADA'
# k = 3
#
# l = []
# for i in range(0,len(s),k):
#     l.append(s[i:k+i])
# for line in l:
#     s = ''
#     for i in range(3):
#         if line[i] not in s:
#             s += line[i]
#     print(s)

##Polar Coordinates
# import math
# s = complex('-1-5j')
# r = math.fabs(math.pow((math.pow(s.real, 2)+math.pow(s.imag, 2)), 0.5))
# print(r)
# f = math.atan(s.imag/s.real)
# print(f)
# import cmath
# print(*cmath.polar(complex(input())), sep='\n')
