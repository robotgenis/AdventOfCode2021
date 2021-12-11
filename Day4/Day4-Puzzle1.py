

lines = open("Day4\\Day4.txt", "r").readlines()


call = list(map(int,lines[0].split(",")))

data = lines[1:]


def winner(board, marked, lastNum):
    print(board)
    print(marked)
    
    total = 0
    for x in range(5):
        for y in range(5):
            if marked[y][x] == 0:
                total += board[y][x]
    print(total, lastNum)
    print(total * lastNum)
    exit()


board = []
marked = []

for i in range(0, len(data), 6):
    
    a = data[i+1:i+6]
    
    for k in range(0, len(a)):
        a[k] = list(map(int,a[k][:-1].split()))
    board.append(a)
    marked.append([[0 for i in range(5)] for k in range(5)])

for num in call:
    
    for k in range(len(board)):
        for x in range(5):
            for y in range(5):
                if board[k][y][x] == num:
                    marked[k][y][x] = 1
    #x axis
    for k in range(len(board)):
        for x in range(5):
            for y in range(5):
                if marked[k][y][x] == 0:
                    break
            else:
                winner(board[k], marked[k], num)
    #y axis
    for k in range(len(board)):
        for y in range(5):
            for x in range(5):
                if marked[k][y][x] == 0:
                    break
            else:
                winner(board[k], marked[k], num)
    


