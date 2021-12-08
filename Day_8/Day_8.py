#input= [line.strip() for line in open('Day_8_test_input.txt')]
input= [line.strip() for line in open('Day_8_input.txt')]

'''
for i in range(0,len(input),2):
    #print(i)
    dlu=len(input[i])
    input[i]=input[i][:dlu-2]
'''
output_1=[]
output_2=[]


for i in range(0,len(input)):
    output_1.append(input[i][:58])
for i in range(0,len(output_1)):
    output_1[i]=list(map(str,list(output_1[i].split(' '))))

#print(output_1)

for i in range(0,len(input)):
    output_2.append(input[i][61:len(input[i])])
for i in range(0, len(output_2)):
    output_2[i] = list(map(str, list(output_2[i].split(' '))))
#print(output_2)

#print(output_1)
licz=0


for i in output_2:
    for j in i:
        if len(j) == 2:
            licz += 1
        elif len(j) == 3:
            licz += 1
        elif len(j) == 4:
            licz += 1
        elif len(j) == 7:
            licz += 1
print(licz)
