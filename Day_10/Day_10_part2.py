#input= [line.strip() for line in open('Day_10_test_input_2.txt')]
input= [line.strip() for line in open('Day_10_input.txt')]

start=['(','[','{','<']
anty={')':'(',']':'[','}':'{','>':'<'}
score_tab={'(':1,'[':2,'{':3,'<':4}
input2=[]

for i in input:
    st = []
    jj=-1
    for j in i:
        jj+=1
        if j in start:
            st.append(j)
        else:
            if len(st)>0:
                if st[-1] == anty[j]:
                    st.pop(-1)
                else:
                    break
        if jj==len(i)-1:
            input2.append(st)
        #print(st)

scores=[]

for i in input2:
    i.reverse()
    score=0
    for j in i:
        score=score*5+score_tab[j]
        #print(score)
    scores.append(score)

scores=sorted(scores)
win_ind=int(len(scores)/2-0.5)
winner=scores[win_ind]
print(scores)
print(winner)

'''
input3=[]
ii=0
for i in input2:
    jj=0
    inp=[]
    for j in start:
        inp.append(i.count(j))
    input3.append(inp)

for i in input3:
    scores.append(((i[1]*2*5+i[0]*1)*5+i[2]*3)*5+i[3]*4)



print(input3)
print(input2)
print(scores)
print(winner)

'''
