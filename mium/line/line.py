import matplotlib.pyplot as plt
import random
# x=[1,2,3,4]
# y=[1,2,3,5]
# print('123123213')
# plt.plot(x,y)
plt.xlabel('X1')
plt.ylabel('X2')
plt.xlim(-15,15)
plt.ylim(-15,15)

plt.axhline(0, color='black')
plt.axvline(0, color='black')
#   x1+4x2=28
f1x1 = []
f1x2 = []
for x1 in range(11):
    x2 = (28 - x1) /4
    f1x1.append(x1)
    f1x2.append(x2)
print()

plt.plot(f1x1, f1x2, color='red')

#   2x1+3x2=26
f2x1 = []
f2x2 = []
for x1 in range(11):
    x2 = (26 - (2 * x1)) /3
    f2x1.append(x1)
    f2x2.append(x2)

plt.plot(f2x1, f2x2)

#   4x1+x2=32
f3x1 = []
f3x2 = []
for x1 in range(11):
    x2 = 32 - 4 * x1
    f3x1.append(x1)
    f3x2.append(x2)

plt.plot(f3x1, f3x2)

#   3x1+2x2=4
f4x1 = []
f4x2 = []
for x1 in range(11):
    x2 = ((4 - (3 * x1)) / 2)
    f4x1.append(x1)
    f4x2.append(x2)

plt.plot(f4x1, f4x2)

vx1 = [0, 3]
vx2 = [0, 2]

plt.plot(vx1, vx2, color='black')
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

print('x* = (7; 4)')
print('Z* = 29')

plt.show()