input= [line.strip() for line in open('Day_5_input.txt')]

for i in range(0,len(input)):
    input[i]=input[i].replace(" -> ", ",")

for i in range(0,len(input)):
    input[i]=list(map(int,list(input[i].split(','))))


maxim=0
for i in range(0,len(input)):
    for j in range(0,len(input[i])):
        if input[i][j]>maxim:
            maxim=input[i][j]
maxim=maxim+1

matrix = [[0]]* maxim
for i in range(0,maxim):
    matrix[i]=[0] * maxim

print(matrix)


for y in range(0,len(input)):
    #print(y)
    if input[y][0]==input[y][2]:
        #print('pion')
        #print(input[y][0]==input[y][2])
        mini=min(input[y][1],input[y][3])
        maxi=max(input[y][1],input[y][3])+1
        for y2 in range(mini, maxi):
            #print(range(mini, maxi))
            matrix[y2][input[y][0]]+=1

    elif input[y][1]==input[y][3]:
        #print('poziom')
        #print(input[y][1]==input[y][3])
        mini=min(input[y][0],input[y][2])
        #print(mini)
        maxi=max(input[y][0],input[y][2])+1
        #print(maxi)
        #print(input[y][1])
        for x2 in range(mini, maxi):
            #print(range(mini, maxi))
            matrix[input[y][1]][x2]+=1

    else:
        if abs(input[y][0]-input[y][2])==abs(input[y][1]-input[y][3]):
            #print('skos')
            #print(input[y][1]==input[y][3])
            minix = input[y][0]
            maxix = input[y][2]
            #print(minix,maxix)
            miniy = input[y][1]
            maxiy = input[y][3]
            #print(miniy,maxiy)
            #print(maxi)
            #print(input[y][1])
            i=0
            yy=list(range(miniy, maxiy, int((input[y][3]-input[y][1])/abs(input[y][3]-input[y][1]))))+[maxiy]
            xx=list(range(minix, maxix, int((input[y][2]-input[y][0])/abs(input[y][2]-input[y][0]))))+[maxix]

            for y2 in yy:
                #print(int((input[y][3]-input[y][1])/abs(input[y][3]-input[y][1])))
                #print(y2)
                #print(xx)
                matrix[y2][xx[i]]+=1
                i+=1


kielo=0
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[i])):
        if matrix[i][j]>1:
            kielo+=1


print(matrix)
print(kielo)