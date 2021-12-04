report = [line.strip() for line in open('Day_3_input.txt')]


def string_change(old_string, place, value):
    string_list = list(old_string)
    string_list[place] = value
    new_string = "".join(string_list)
    return new_string


def gamma_epsilon(re):
    su = [0] * len(re[0])
    half = len(re) / 2
    rest = half % 1
    gamma_rate = ""
    epsilon_rate = ""
    for y in re:
        for x in range(0, len(str(y))):
            su[x] = su[x] + int(y[x])

    for i in su:
        if i > half:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"
    if rest == 0:
        for i in range(0, len(su)):
            if su[i] == half:
                gamma_rate = string_change(gamma_rate, i, "1")
                epsilon_rate = string_change(epsilon_rate, i, "0")
    return [gamma_rate, epsilon_rate]


gamma = gamma_epsilon(report)[0]
epsilon = gamma_epsilon(report)[1]

print(gamma_epsilon(report))
print(int(gamma, 2) * int(epsilon, 2))


def ratio(rep, a):
    rating = rep
    while len(rating) > 1:
        for x in range(0, len(rep[0])):
            criteria = gamma_epsilon(rating)[a][x]
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
                    to_remove.insert(0, y)
                    print(to_remove)
            for r in to_remove:
                rating.pop(r)
            print(rating)
            print("x")
            if len(rating) == 1:
                return rating[0]

#oxygen_generator = ratio(report, 0)
co2_scrubber = ratio(report, 1)

#print(oxygen_generator)
print(co2_scrubber)
#print(int(oxygen_generator,2))
print(int(co2_scrubber,2))