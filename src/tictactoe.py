'''
Created on Apr 6, 2014

@author: shoulongli
'''
import random
# use board[0 - 9] as board
'''
board[0]  board[1]  board[2]
board[3]  board[4]  board[5]
board[6]  board[7]  board[8]
'''
def isWinner(board , c):
    return ((board[0] == c and board[1] == c and board[2] == c) or
    (board[3] == c and board[4] == c and board[5] == c) or
    (board[6] == c and board[7] == c and board[8] == c) or
    (board[0] == c and board[3] == c and board[6] == c) or
    (board[1] == c and board[4] == c and board[7] == c) or
    (board[2] == c and board[5] == c and board[8] == c) or
    (board[0] == c and board[4] == c and board[8] == c) or
    (board[2] == c and board[4] == c and board[6] == c))

def displayBoard(board):
    print('   |   |')
    print(' '+board[0]+' |'+' '+board[1]+' |'+' '+board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+board[3]+' |'+' '+board[4]+' |'+' '+board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+board[6]+' |'+' '+board[7]+' |'+' '+board[8])
    print('   |   |')

def isSpaceFree(board, i):
    return board[i] == ' '

def isBoardFull(board):
    for i in range(0,10):
        if isSpaceFree(board, i):
            return False
    return True

def makeMove(board ,move, c):
    board[move] = c

def getPlayerMove(board):
    move = ' '
    while not (move in '1234567890'.split() and isSpaceFree(board,int(move))):
        print('what is your next move')
        move = input()
        return int(move)

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #first check if computer can win
    for i in range(0,9):
        if isSpaceFree(board,i) and checkWin(board, computerLetter, i):
            return i

    #check if player can win, then block
    for i in range(0,9):
        if isSpaceFree(board, i) and checkWin(board, playerLetter,i):
            return i

    #take one of the corneres
    if isSpaceFree(board, 0):
        return 0
    elif isSpaceFree(board, 2):
        return 2
    elif isSpaceFree(board, 6):
        return 6
    elif isSpaceFree(board, 8):
        return 8

    #try to take center
    if isSpaceFree(board,4):
        return 4

    #try to take sides
    if isSpaceFree(board, 1):
        return 1
    elif isSpaceFree(board,3):
        return 3
    elif isSpaceFree(board, 5):
        return 5
    elif isSpaceFree(board, 7):
        return 7



#use checkWin or use getDuplicateBoard() and isWinner

def getDuplicateBoard(board):
    duplicate = []
    for ch in board:
        duplicate.append(ch)

    return duplicate

def checkWin(board, letter, i):
    return {
            0: zero(board,letter),
            1: one(board,letter),
            2: two(board,letter),
            3: three(board,letter),
            4: four(board,letter),
            5: five(board, letter),
            6: six(board,letter),
            7: seven(board, letter),
            8: seven(board, letter)}[i]

def zero(board,letter):
    return ((board[1] == letter and board[2] == letter) or
            (board[3] == letter and board[6] == letter) or
            (board[4] == letter and board[8] == letter))

def one(board, letter):
    return ((board[0] == letter and board[2] == letter) or
            (board[4] == letter and board[7] == letter))

def two(board, letter):
    return ((board[0] == letter and board[1] == letter) or
            (board[5] == letter and board[8] == letter) or
            (board[4] == letter and board[6] == letter))

def three(board, letter):
    return ((board[0] == letter and board[6] == letter ) or
            (board[4] == letter and board[5] == letter))

def four(board, letter):
    return ((board[1] == letter and board[7] == letter) or
           ( board[3] == letter and board[5] == letter ) or
           (board[0] == letter and board[8] == letter) or
           (board[2] == letter and board[6] == letter))

def five(board, letter):
    return ((board[2] == letter and board[8] == letter ) or
            (board[3] == letter and board[4] == letter))

def six(board, letter):
    return ((board[0] == letter and board[3] == letter) or
            (board[7] == letter and board[8] == letter) or
            (board[2] == letter and board[4] == letter))

def seven(board ,letter):
    return ((board[6] == letter and board[8] == letter) or
            (board[1] == letter and board[4] == letter))

def eight(board , letter):
    return ((board[0] == letter and board[4] == letter) or
            (board[2] == letter and board[5] == letter) or
            (board[7] == letter and board[8] == letter))


def whoGoesFirst():
    if 0 == random.randint(0,1):
        return 'computer'
    else:
        return 'player'

def playAgain():
    print('do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print(' do you want to be X or O ?')
        letter = input().upper();

    if 'O' == letter:
        return ['O','X']
    else:
        return ['X','O']

# board = 'XXXOOOOOO'
# displayBoard(board)

def mainLoop():



    print('Tic Tac Toe')
    while True:
        board = [' ']*9
        playerLetter, computerLetter = inputPlayerLetter()
        print('Player is: '+playerLetter+" Computer is: "+computerLetter)
        turn = whoGoesFirst()
        print('The '+turn+" will go first")
        gameOver = False
        displayBoard(board)

        while not gameOver:
            if turn == 'player':
                move = getPlayerMove(board)
                makeMove(board,move,playerLetter)
                displayBoard(board)
                if isWinner(board, playerLetter):
                    print('Hooray! You have won the game!')
                    gameOver = True
                else:
                    if isBoardFull(board):
                        print('The game is a tie!')
                        gameOver = True
                        break
                    else:
                        turn = 'computer'

            else:
                move = getComputerMove(board,computerLetter)
                makeMove(board, move, computerLetter)
                displayBoard(board)
                if isWinner(board, computerLetter):
                    print('The computer has beaten you! You lose.')
                    gameOver = True
                else:
                    if isBoardFull(board):
                        print('The game is a tie!')
                        gameOver = True
                        break
                    else:
                        turn = 'player'


        if not playAgain():
            break

mainLoop()
