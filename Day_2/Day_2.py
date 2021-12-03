commends = [line.strip() for line in open('Day_2_input.txt')]

for commend in commends:
    commends[commends.index(commend)]=[commend[:-2],commend[-1:]]
print(commends)

X=0
Y=0
for i in commends:
    if i[0] == "forward":
        X = X + int(i[1])
    elif i[0] == "up":
        Y = Y + int(i[1])
    elif i[0] == "down":
        Y = Y - int(i[1])
print(X)
print(Y)
print(X*abs(Y))
