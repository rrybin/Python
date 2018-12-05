# while True:
#     reply = input('Enter text: ')
#     if reply == 'stop': break
#     try:
#         num = int(reply)
#     except:
#         print('Bad!' * 8)
#     else:
#         print(int(reply) ** 2)
# print('Bye')

# while True:
#     reply = input('Enter text ')
#     if reply == 'stop':
#         break
#     elif not reply.isdigit():
#         print('Bad!' * 8)
#     else:
#         num = int(reply)
#         if num < 20:
#             print('low')
#         else:
#             print(num ** 2)
# print('Bye')

# def timeConversion(s):
#     time = ''
#     if 'P' in s:
#         if s[0:2] != '12':
#             time = str(int(s[0:2])+12)+s[2:-2]
#         else:
#             time = s[:-2]
#     elif 'A' in s:
#         if s[0:2] == '12':
#             time = '00'+s[2:-2]
#         else:
#             time = s[:-2]
#     return time
#
# s='12:45:54PM'
# result = timeConversion(s)
# print(result)

# def equalizeArray(arr):
#     arr.sort()
#     res = 0
#     for id, dig in enumerate(arr):
#         count = 0
#         for id2, dig2 in enumerate(arr):
#             if dig != dig2 and id != id2:
#                 count += 1
#         if count + 1 == len(arr):
#             res += 1
#     return res
#
#
# arr = [1, 2, 3, 1, 2, 3, 3, 3]
#
# result = equalizeArray(arr)
#
# print(result)

# ar = [18, 90, 90, 13, 90, 75, 90, 8, 90, 43]
# max = ar[0]
# for id, i in enumerate(ar):
#     if max < i:
#         max = ar[id]
# count = 0
# for i in range(len(ar)):
#     if max == ar[i]:
#         count += 1
# print(count)

#Answer 1 2
def virusIndices(p, v):
    l = []                    #01 12 23 35
    for i in range(len(p)): #ab bb ba ab  ban ana nan ana
        if len(p[i:i+len(v)]) == len(v):
            l.append(p[i:i+len(v)])
    print('-------------')
    print(l)
    temp = []
    for sym in v:
        for line in l:
            if sym in line:
                for x in range(len(line)):
                    if line[x] == v[x]:
                        temp.append(line)
    print('-------------')
    print(temp)
    l.clear()
    for idx, line in enumerate(temp):
        if line != v and line not in l:
            l.append(line)
        elif line == v and line not in l:
            l.append(line)
    print('-------------')
    print(l)
    s = ''
    for line in l:
        s = s + str(p.index(line)) + ' '
    if len(l) == 0 or s == '0 ':
        s = 'No Match!'
    print(s)


#Answer 1 2
# p = 'abbab'
# v = 'ba'
# virusIndices(p, v)
#
# print()
#
# p = 'hello'
# v = 'world'
# virusIndices(p, v)
#
# print()
#
# #Answer 0 2
# p = 'banana'
# v = 'nan'
# virusIndices(p, v)

# p = 'bbabbaaaabababbaaba'
# v = 'aaababbaaaaaa'
# virusIndices(p, v)

# aabaa aaaab
# bbabbaaaabababbaaba aaababbaaaaaa
# babbbabaa bbaba
# baaaaababbaa abbab
# ababbaabbbabaababaaaabaa aaabaababbbabbabbaababbb
# aaaabaaaaabbaaaa aa
# abababaaaaabaaaaba ababba
# aabbbababaabaaa baabababbaaaaa
# bababa a
# bbbbabaaababaabbaab baaaaab

# import sys
# name_score = [['Test1', -51], ['Test2', -51], ['Test3', 51]]
#
# name_score.sort()
#
# min1 = name_score[0][1]
# min2 = sys.maxsize
#
# for line in name_score:
#     if line[1] < min1:
#         min2 = min1
#         min1 = line[1]
#     elif line[1] > min1 and line[1] < min2:
#         min2 = line[1]
# print(min1, min2)
# for line in name_score:
#     if line[1] == min2:
#         print(line[0])