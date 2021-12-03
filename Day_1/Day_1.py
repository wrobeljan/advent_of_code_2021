measures=[int(line.strip()) for line in open('Day_1_input.txt')]

'''with open('Day_1_input.txt') as inputFile:
    for i in inputFile:
        measures.append(int(i))
'''

count=-1;
count = [count+1 for measure in measures if measure > measures[measures.index(measure)]]

print(count)
'''
count=-1
prev_measure=0
for measure in measures:
for
    if measure>prev_measure: count+=1
    prev_measure=measure
print(count)
'''

