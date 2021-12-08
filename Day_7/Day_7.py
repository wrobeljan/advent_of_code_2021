input= [line.strip() for line in open('Day_7_input.txt')]

for i in range(0,len(input)):
    input[i]=list(map(int,list(input[i].split(','))))
    input=input[0]
input.sort()
input0=input
#print(input)

minx=min(input)
maxx=max(input)
dlu=[0]*len(input)

for i in range(0,len(dlu)):
    for j in input:
        dlu[i]+=abs(input[i]-j)

print(min(dlu))

#part2


def sumo(z):
    a=0
    for i in range(0,z+1):
        a+=i
    return a

input=input0
dlu=[0]*maxx

for i in range(0,maxx):
    for j in input:
        #print(j)
        dlu[i]+=sumo(abs(j-i))
#print(input)
#print(dlu)
print(min(dlu))

'''
cel=input[dlu.index(min(dlu))]
indices = [i for i, x in enumerate(input) if x == cel]
#print(cel)
#print(indices)

for i in sorted(indices,reverse=True):
    input.remove(input[i])
    #dlu.remove(dlu[i])
#print(dlu)

sumaa=0
for i in input:
    sumaa+=sumo(abs(i-cel))

print(sumaa)
'''
