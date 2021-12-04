input= [line.strip() for line in open('Day_4_input.txt')]
numbers=list(map(int,list(input[0].split(','))))
#numbers=input[0].split(',')
board_count=int((len(input)-1)/6)
print("numery="+str(numbers))
print("liczba plansz="+str(board_count))

boards=input[1:]
lines_to_remove=[0,*range(6,6*(board_count),6)]

#print("lines_to_remove="+str(lines_to_remove))
for i in sorted(lines_to_remove, reverse=True):
    boards.pop(i)
#print(len(boards))

for i in range(0,len(boards)):
    boards[i]=boards[i].strip()
    boards[i]=" ".join(boards[i].split())
    boards[i]=boards[i].split()
    for j in range(0, len(boards[i])):
        boards[i][j]=int(boards[i][j])

def chunk_using_generators(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def flatten(t):
    return [item for sublist in t for item in sublist]

boards=list(chunk_using_generators(boards, 5))
#print(boards)

def if_all_X(li,a):
    for i in li:
        if i!=a:
            return False
    return True

def if_all_Y(li,c,a):
    for i in li:
        if i[c]!=a:
            return False
    return True

stop=False
for n in numbers:
    #print(n)
    for b in boards:
        #print(b)
        for r in b:
            #print(r)
            for c in r:
                #print(c)
                if c==n:
                    c0=r.index(c)
                    boards[boards.index(b)][b.index(r)][r.index(c)] = 'X'
                    if if_all_X(boards[boards.index(b)][b.index(r)], 'X'):
                        stop = True
                        break
                    if if_all_Y(boards[boards.index(b)], c0, 'X'):
                        stop = True
                        break
            if stop==True:
                break
        if stop==True:
            winning_board=b
            break
    if stop==True:
        winning_number=n
        break

flatten_board=flatten(winning_board)
flatten_board.remove('X')

occurrences = lambda s, lst: (i for i,e in enumerate(lst) if e == s)
list(occurrences('X',flatten_board))
for i in sorted(list(occurrences('X',flatten_board)), reverse=True):
    flatten_board.pop(i)
winning_sum=sum(flatten_board)

print(winning_number)
print(winning_sum)
print(winning_number*winning_sum)



