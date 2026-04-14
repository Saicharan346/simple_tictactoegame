board = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']

wins = [(0,4,8),(2,4,6),(0,3,6),(1,4,7),
        (2,5,8),(0,1,2),(3,4,5),(6,7,8)]

outputs = [1,2,3,4,5,6,7,8,9]
count = 0
found = False

def print_board():
    print(board[0],'|',board[1],'|',board[2])
    print('---------')
    print(board[3],'|',board[4],'|',board[5])
    print('---------')
    print(board[6],'|',board[7],'|',board[8])

def check_win():
    for a,b,c in wins:
        if board[a]==board[b]==board[c]=='X':
            return "X"
        elif board[a]==board[b]==board[c]=='O':
            return "O"
    

print_board()

while count < 9:
    us1 = int(input("Enter first user input: "))
    if us1 not in outputs or us1 < 1 or us1 > 9:
        print("Invalid move")
        continue

    board[us1-1] = 'O'
    outputs.remove(us1)
    print_board()
    count += 1

    winner = check_win()
    if winner == 'O':
        print("The winner is first user!!!")
        break

    if count == 9:
        print("Match is Draw!!!")
        break

    us2 = int(input("Enter second user input: "))
    if us2 not in outputs or us2 < 1 or us2 > 9:
        print("Invalid move")
        continue

    board[us2-1] = 'X'
    outputs.remove(us2)
    print_board()
    count += 1

    winner = check_win()
    if winner == 'X':
        print("The winner is second user!!!!")
        break

else:
    print("Match is Draw!!!")