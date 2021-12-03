report = [line.strip() for line in open('Day_3_input.txt')]

sum=[0]*len(report[0])

for y in report:
    for x in range(0,len(str(y))):
        sum[x]=sum[x]+int(y[x])
print(sum)

half=len(report)/2

gamma_rate=""
epsilon_rate=""
for i in sum:
    if i>half:
        gamma_rate=gamma_rate+"1"
        epsilon_rate=epsilon_rate+"0"
    else:
        gamma_rate = gamma_rate + "0"
        epsilon_rate = epsilon_rate + "1"

print(gamma_rate,epsilon_rate)
print(int(gamma_rate,2)*int(epsilon_rate,2))