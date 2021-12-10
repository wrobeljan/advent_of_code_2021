import itertools

input= [line.strip() for line in open('Day_8_test_input_2.txt')]
#input= [line.strip() for line in open('Day_8_input.txt')]

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
licz_2=0

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
#print(len(input))



dic=[]
for i in range(0,len(input)):
    dic.append({'a':'X','b':'X','c':'X','d':'X','e':'X','f':'X','g':'X'})

occ = lambda s, lst: (i for i,e in enumerate(lst) if e == s)
#list(occ('X',flatten_board))

def czyst(a,b):
    for i in b:
        if i in a:
            a=a.replace(i,'')
    return a

ii=0
lenx=[]
for i in output_1:
    for j in i:
        lenx.append(len(j))
        ala=sum(j)

    print(ala)
    sum_0_9=sum(j)

    cf_1=i[list(occ(2,lenx))[0]]
    bcdf_4=i[list(occ(4,lenx))[0]]
    acf_7=i[list(occ(3,lenx))[0]]
    abcdefg_8=i[list(occ(7,lenx))[0]]

    dic[ii]['a']=czyst(acf,cf)





    #print(list(occ(2,lenx))[0])

    ii+=1
print(dic)
print(acf)

'''
r_dic=[]
for i in range(0,len(dic)):
    r_dic.append({v: k for k, v in dic[i].items()})

ile=0
for i in sl:
    for j in sl:
        dic[ile][i]=j
'''


'''
sl=('a','b','c','d','e','f','g')

perm=itertools.permutations(sl)
perm_list=list(perm)

dlu=len(perm_list)





permy=[]

ii=0
for i in perm_list:
        diki=dict(zip(sl,i))
        permy.append(diki)
        ii+=1
#print(permy)
#print(len(permy))

for i in output_2:
    for j in i:
        if len(j) == 2:
            licz += 1
        elif len(j) == 3:
            licz += 1
        elif len(j) == 4:
            licz += 1

print(licz)
'''


