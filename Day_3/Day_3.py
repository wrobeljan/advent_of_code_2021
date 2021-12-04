report = [line.strip() for line in open('Day_3_test_input.txt')]

def string_change(old_string,place,value):
    string_list = list(old_string)
    string_list[place] = value
    new_string = "".join(string_list)
    return new_string

def gamma_epsilon(report):
    sum = [0] * len(report[0])
    half = len(report) / 2
    rest = half % 1
    for y in report:
        for x in range(0, len(str(y))):
            sum[x] = sum[x] + int(y[x])
    gamma_rate = ""
    epsilon_rate = ""
    for i in sum:
        if i>half:
            gamma_rate = gamma_rate + "1"
            epsilon_rate = epsilon_rate+"0"
        else:
            gamma_rate = gamma_rate + "0"
            epsilon_rate = epsilon_rate + "1"
    if rest == 0:
        for i in range(0, len(sum)):
            if sum[i] == half:
                gamma_rate = string_change(gamma_rate,i,"1")
                epsilon_rate = string_change(epsilon_rate,i,"0")
    return [gamma_rate,epsilon_rate]


gamma_rate=gamma_epsilon(report)[0]
epsilon_rate=gamma_epsilon(report)[1]

print(gamma_epsilon(report))
print(int(gamma_rate,2)*int(epsilon_rate,2))

'''
if rest==0:
    for i in range(0,len(sum)):
        if sum[i] == half:
            gamma_rate[i]="1"
            epsilon_rate[i]="1"

print(gamma_rate, epsilon_rate)
'''





'''
a=0
while len(oxygen_generator) > 1:
    for x in range(0, len(report[0])):
        for y in oxygen_generator:
            if y[x] != gamma_epsilon(oxygen_generator)[a][x]:
                oxygen_generator.remove(y)


a=1
while len(co2_scrubber) > 1:
    for x in range(0, len(report[0])):
        criteria=gamma_epsilon(co2_scrubber)[a][x]
        print(x)
        print(criteria)
        for y in range(0, len(co2_scrubber)):
            print(co2_scrubber[y])
            print(co2_scrubber[y][x])
            if co2_scrubber[y][x] != criteria:
                co2_scrubber.remove(co2_scrubber[y])
                print(co2_scrubber)
                

          '''


def ratio(rep,a):
    rating = rep
    while len(rating) > 1:
        for x in range(0, len(rep[0])):
            criteria=gamma_epsilon(rating)[a][x]
            print(x)
            print(gamma_epsilon(rating)[a])
            print(criteria)
            print(rating)
            to_remove = []
            for y in range(0, len(rating)):
                print(y)
                print(rating[y])
                print(rating[y][x])

                if rating[y][x] != criteria:
                    to_remove.insert(0,y)
                    print(to_remove)
            for r in to_remove: rating.pop(r)
            if len(rating) == 1:
                return rating[0]
            print(rating)
            print("x")


oxygen_generator,co2_scrubber=ratio(report,0),ratio(report,1)




#print(oxygen_generator)
print(co2_scrubber)
#print(int(oxygen_generator,2)*int(co2_scrubber,2))



