##itertools.product()
# from itertools import product
# A = map(int, '1 2'.split(' '))
# B = map(int, '3 4'.split(' '))
# print(*product(A, B))

##itertools.permutations()
# from itertools import permutations
# s,k = input().split()
# l=[]
# for line in tuple(permutations(sorted(s),int(k))):
#     l.append(''.join(line))
# print(l)
# for line in l:
#     print(line)

##itertools.combinations()
from itertools import combinations
# s,k = input().split()
#print('\n'.join([str(line) for line in sorted(s)]))
# for i in range(1,int(k)+1):
#     print(*[''.join(line) for line in combinations(sorted(s),int(i))],sep='\n')

#itertools.combinations_with_replacement()
#from itertools import combinations_with_replacement
#s = 'HACK'
#k = '2'
#print(*[''.join(line) for line in combinations_with_replacement(sorted(s),int(k))],sep='\n')

#Compress the String!
# from itertools import groupby
# s = '1222311'
# print(*[(len(list(g)),int(k)) for k, g in groupby(s)])
# print()
# for k, g in groupby(s):
#     l = []
#     l.append(len(list(g)))
#     l.append(int(k))
#     print(tuple(l),end=' ')
# print()

##Iterables and Iterators
# from itertools import combinations
# l = []
# m = []
# l = [''.join(i) for i in combinations('aacd',2) if i.count('a')]
# m = [''.join(i) for i in combinations('aacd',2) if not i.count('a')]
# print('{0:.3}'.format(len(l)/(len(l)+len(m))))

##Maximize It!
from itertools import product
f = open('testcase_0.txt','r')
k, m = map(int, f.readline().split())
l=[]
for _ in f:
    l.append(list(map(int, _.split(' ')))[1:])
results = map(lambda x: sum(i**2 for i in x)%m, product(*l))
print(max(results))
# l=[]
# for line in x:
#     l.append(max(line)**2)
# print(l)
# print()
# print(abs(sum(l)%m))