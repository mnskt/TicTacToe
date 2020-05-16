theboard = {
    'topLeft': ' ', 'topMid': ' ', 'topRight': ' ',
    'midLeft': ' ', 'midMid': ' ', 'midRight': ' ',
    'botLeft': ' ', 'botMid': ' ', 'botRight': ' '
}

def boardPrint(board):
    print(board['topLeft'] + '|' + board['topMid'] + '|' + board['topRight'])
    print('------')
    print(board['midLeft'] + '|' + board['midMid'] + '|' + board['midRight'])
    print('------')
    print(board['botLeft'] + '|' + board['botMid'] + '|' + board['botRight'])

isRunning = True

while isRunning:
    choice = input("Please enter the position where you want to place 'X'\nAvailable options: topLeft, topMid, topRight, midLeft, midMid, midRight, botLeft, botMid, botRight ")
    theboard[choice] = 'X'
    boardPrint(theboard)
    break