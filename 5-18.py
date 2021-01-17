#5.7檢測(一)
name = ['' for x in range(5)]
score = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
#enter the data:
for i in range(5):
    print('enter %dth student\'s name:' %(i+1),end='')
    name[i] = input()
    print('enter CHINESE\'s grade:' ,end=' ')
    score[i][0] =eval(input())
    print('enter ENGLISH\'s grade:', end=' ')
    score[i][1]= eval(input())
    score[i][2] = (score[i][0] + score[i][1])/2
    
#bubble sort:
for loop in range(1,5):
    for index in range(0,(5-loop)):
        if score[index][2]< score[index+1][2]:
            temp = score[index]
            score[index] = score[index +1]
            score[index+1]= temp
            ntemp =name[index]
            name[index] = name[index+1]
            name[index+1] = ntemp
#tale LIST:
print()
print('name       CHINESE     english     average')
print('==========================================')
for p in range(5):
    print(name[p],end='     ')
    print(score[p][0], end='     ')
    print(score[p][1], end='     ')
    print(score[p][2])
    
