
# 原矩陣：
#1   2  3
#4   5  6
#6   7  8
#10 11 12

#旋轉後：
#10  6  4  1
#11  7  5  2
#12  8  6  3


a1 = [[1,2,3],[4,5,6],[6,7,8],[10,11,12]]
a2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

print('原矩陣：')
for i in range(4):
  for j in range(3):
    print('%2d' %a1[i][j],end=' ')
  print()

#a1矩陣順時針旋轉90度後，轉成a2矩陣

for k in range(3):
  for h in range(4):
    a2[k][h] = a1[4-h-1][k]

print()
print('旋轉後：')
for i in range(3):
  for j in range(4):
    print('%2d' %a2[i][j],end=' ')
  print()
