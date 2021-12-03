measures = [int(line.strip()) for line in open('Day_1_input.txt')]

'''with open('Day_1_input.txt') as inputFile:
    for i in inputFile:
        measures.append(int(i))
'''

'''
count = [count+1 for measure in measures if measure > measures[measures.index(measure)]]

print(count)
'''

def how_many_bigger(measures):
    count = -1
    prev_measure = 0
    for measure in measures:
        if measure > prev_measure: count += 1
        prev_measure = measure
    return count

print(how_many_bigger(measures))

'''
places = [0, 1]
for place in places:
    measures.insert(place, 0)
'''

group_measures = []
count_2=2
for measure in range(count_2,len(measures)):
    group_measures.append(measures[count_2]+measures[count_2-1]+measures[count_2-2])
    count_2 += 1

print(how_many_bigger(group_measures))
