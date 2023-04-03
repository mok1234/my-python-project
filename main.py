board = {'1':'-','2':'-','3':'-',
         '4':'-','5':'-','6':'-',
         '7':'-','8':'-','9':'-'
}
player = 'x'
computer = 'o'
def check_blank(pos):
    if board[pos] == '-':
        return False
    return True
def check_win():
    if board['1'] == board['2'] and board['1'] == board['3'] and board['1']!='-':
        return True
    if board['4'] == board['5'] and board['4'] == board['6'] and board['4']!='-':
        return True
    if board['7'] == board['8'] and board['7'] == board['9'] and board['7']!='-':
        return True
    if board['1'] == board['5'] and board['1'] == board['9'] and board['1']!='-':
        return True
    if board['3'] == board['5'] and board['3'] == board['7'] and board['3']!='-':
        return True
    if board['1'] == board['4'] and board['1'] == board['7'] and board['1']!='-':
        return True
    if board['2'] == board['5'] and board['2'] == board['8'] and board['2']!='-':
        return True
    if board['3'] == board['6'] and board['3'] == board['9'] and board['3']!='-':
        return True
def insert(side,pos):
    if pos == '':
        print('Error insert again')
        insert(side,input())
        return
    if int(pos)>9 or int(pos)<1:
        print('Error insert again')
        insert(side,input())
        return
    if check_blank(pos):
        print('Already occupied insert again.')
        insert(side,input())
        return
    
    board[pos] = side
def print_board():
    print(f'{board["1"]} | {board["2"]} | {board["3"]}')
    print('--+---+--')
    print(f'{board["4"]} | {board["5"]} | {board["6"]}')
    print('--+---+--')
    print(f'{board["7"]} | {board["8"]} | {board["9"]}')
def check_draw():   
    if board['1'] != '-' and board['2'] != '-' and board['3'] != '-' and board['4'] != '-' and board['5'] != '-' and board['6'] != '-' and board['7'] != '-' and board['8'] != '-' and board['9'] != '-' :
        return True
    return False
def comp_move():
    best_score = -800
    best_move = 0
    for i in board:
        if board[i] == '-':
            board[i] = computer
            score = minimax(board,False)
            board[i] = '-'
            if score>best_score:
                best_score = score
                best_move = i
    insert(computer,best_move)
    return
def minimax(board,ismaximizing):
    if checkwhichmarkwon(computer):
        return 1
    if checkwhichmarkwon(player):
        return -1
    if check_draw():
        return 0
    if ismaximizing:
        best_score = -800
        for i in board:
            if board[i] == '-':
                board[i] = computer
                score = minimax(board,False)
                board[i] = '-'
                if score>best_score:
                    best_score = score
        return best_score
    else:
        best_score = 800
        for i in board:
            if board[i] == '-':
                board[i] = player
                score = minimax(board,True)
                board[i] = '-'
                if score<best_score:
                    best_score = score
        return best_score
def checkwhichmarkwon(mark):
    if board['1'] == board['2'] and board['1'] == board['3'] and board['1']==mark:
        return True
    if board['4'] == board['5'] and board['4'] == board['6'] and board['4']==mark:
        return True
    if board['7'] == board['8'] and board['7'] == board['9'] and board['7']==mark:
        return True
    if board['1'] == board['5'] and board['1'] == board['9'] and board['1']==mark:
        return True
    if board['3'] == board['5'] and board['3'] == board['7'] and board['3']==mark:
        return True
    if board['1'] == board['4'] and board['1'] == board['7'] and board['1']==mark:
        return True
    if board['2'] == board['5'] and board['2'] == board['8'] and board['2']==mark:
        return True
    if board['3'] == board['6'] and board['3'] == board['9'] and board['3']==mark:
        return True
def play():
    print_board()
    while True:
        print('player1 round')
        insert(player,input())
        print_board()
        if check_win():
            print(player+' Win')
            break
        if check_draw():
            print('draw')
            break
        comp_move()
        print_board()
        if check_win():
            print(computer+' Win')
            break

while True:
    play()
    print("play again write y close the game write n")
    a = input().lower()
    while a!= 'y' and a!='n':
        print('error write again')
        a = input()
    if a == 'n':
        break
    if a == 'y':
        board ={'1':'-','2':'-','3':'-',
         '4':'-','5':'-','6':'-',
         '7':'-','8':'-','9':'-'
        }
