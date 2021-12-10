#input= [line.strip() for line in open('Day_10_test_input.txt')]
input= [line.strip() for line in open('Day_10_input.txt')]

errory=[]
start=['(','[','{','<']
error_points={')':3,']':57,'}':1197,'>':25137}
anty={')':'(',']':'[','}':'{','>':'<'}

for i in input:
    st = []
    for j in i:
        if j in start:
            st.append(j)

        else:
            if len(st)>0:
                if st[-1] == anty[j]:
                    st.pop(-1)
                else:
                    errory.append(j)
                    break
        #print(st)

points=0
for i in errory:
    points=points+error_points[i]
print(errory)
print(points)
