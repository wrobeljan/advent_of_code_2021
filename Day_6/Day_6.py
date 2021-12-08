
'''
input= [line.strip() for line in open('Day_6_input.txt')]

for i in range(0,len(input)):
    input[i]=list(map(int,list(input[i].split(','))))
input=input[0]
#input=[1,1,3,1,3,2,1,3,1,1,3,1,1,2,1,3,1,1,3,5,1,1,1,3,1,2,1,1,1,1,4,4,1,2,1,2,1,1,1,5,3,2,1,5,2,5,3,3,2,2,5,4,1,1,4,4,1,1,1,1,1,1,5,1,2,4,3,2,2,2,2,1,4,1,1,5,1,3,4,4,1,1,3,3,5,5,3,1,3,3,3,1,4,2,2,1,3,4,1,4,3,3,2,3,1,1,1,5,3,1,4,2,2,3,1,3,1,2,3,3,1,4,2,2,4,1,3,1,1,1,1,1,2,1,3,3,1,2,1,1,3,4,1,1,1,1,5,1,1,5,1,1,1,4,1,5,3,1,1,3,2,1,1,3,1,1,1,5,4,3,3,5,1,3,4,3,3,1,4,4,1,2,1,1,2,1,1,1,2,1,1,1,1,1,5,1,1,2,1,5,2,1,1,2,3,2,3,1,3,1,1,1,5,1,1,2,1,1,1,1,3,4,5,3,1,4,1,1,4,1,4,1,1,1,4,5,1,1,1,4,1,3,2,2,1,1,2,3,1,4,3,5,1,5,1,1,4,5,5,1,1,3,3,1,1,1,1,5,5,3,3,2,4,1,1,1,1,1,5,1,1,2,5,5,4,2,4,4,1,1,3,3,1,5,1,1,1,1,1,1]
days=0
ile_dni=1

while days<ile_dni:
        for i in range(0,len(input)):
            if input[i]==0:
                input[i]=6
                input.append(8)
            elif input[i]>0:
                input[i]-=1
        days+=1

'''
#part_2
input= [line.strip() for line in open('Day_6_input.txt')]

for i in range(0,len(input)):
    input[i]=list(map(int,list(input[i].split(','))))
input=input[0]

days=0
ile_dni=256
licznik=[0]*9
sztuki=[0]*9
#print(licznik)


for i in range(0,len(input)):
    for j in range(0, len(licznik)):
        if input[i]==j:
            licznik[j]+=1

#print(licznik)

licznik_2=[0]*9

while days<ile_dni:
    for i in [1,2,3,4,5,6,7,8]:
        #print(i)
        licznik_2[i]=0
        licznik_2[i-1]=licznik[i]

    licznik_2[8]=licznik_2[8]+licznik[0]
    licznik_2[6]=licznik_2[6]+licznik[0]
    #print(licznik_2)
    licznik=licznik_2
    licznik_2 = [0] * 9
    days+=1

su=sum(licznik)
print(days)
print(su)
