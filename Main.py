import time, sys

cash = True
for i in range(len(sys.argv)):
    if(sys.argv[i] == "-c"):
        try:
            letter = sys.argv[i+1]
            if(letter == "F"):
                cash = False
            elif(letter == "T"):
                cash = True
            else:
                quit()
        except:
            print("Invalid Arguments")
            quit()

class Casher:
    def __init__(self):
        self.can_goto = {}
        self.get_goto = {}

    def add_can_goto(self, inputs, output):
        self.can_goto[inputs] = output

    def add_get_goto(self, inputs, output):
        self.get_goto[inputs] = output

    def get_get_goto(self, inputs):
        try:
            return self.get_goto[inputs]
        except:
            return None

    def get_can_goto(self, inputs):
        try:
            return self.can_goto[inputs]
        except:
            return None

class Tile:
    def __init__(self, position, state):
        self.state = state
        self.position = position

class Board:
    def __init__(self, dimensions):
        self.board = [[Tile((x, y), None) for y in range(dimensions[1])] for x in range(dimensions[0])]
        self.dimensions = dimensions

    def get_tile(self, x, y):
        return self.board[x][y]

    def is_solved(self):
        for x in range(self.dimensions[0]):
            for y in range(self.dimensions[1]):
                if(self.board[x][y].state == None):
                    return False
        return True

def print_board(board):
    dimensions = board.dimensions
    for y in range(dimensions[1]):
        text = ""
        for x in range(dimensions[0]):
            tile = board.get_tile(x, y)
            if(tile.state == 1):
                text += "+\t"
            elif(tile.state == 0):
                text += "-\t"
            else:
                text += "/\t"
        print(text)

def get_goto(source, board, can_goto):
    if(cash):
        x = cashing.get_get_goto(source)
        if(x):
            return x
    lista = []
    dim = board.dimensions
    for xd in range(dim[0]):
        for yd in range(dim[1]):
            tiled = board.get_tile(xd, yd)
            if(can_goto(source, (xd, yd))):
                lista.append(tiled)
    if(cash):
        cashing.add_get_goto(source, lista)
    return lista


def solve(board, can_goto, max_iterations):
    dim = board.dimensions
    i = 0
    while(i < max_iterations and (not board.is_solved())):
        i += 1
        for x in range(dim[0]):
            for y in range(dim[1]):
                tile = board.get_tile(x, y)
                if(tile.state == None):
                    best = 0
                    for tiled in get_goto((x, y), board, can_goto):
                        if(tiled.state == 1):
                            best = 1
                        elif(tiled.state == None):
                            if(best == 0):
                                best = None
                    if(best == 1):
                        tile.state = 0
                    elif(best == 0):
                        tile.state = 1
    return board

def can_goto_check(source, dest): #Rules
    if(cash):
        x = cashing.get_can_goto((source, dest))
        if(x):
            return x
    output = None
    # Start your rules here <--------------------------------------
    if(source == dest):
        output = False
    elif(source[0] == dest[0] and source[1] <= dest[1]):
        output = True
    elif(source[1] == dest[1] and source[0] <= dest[0]):
        output = True
    else:
        output = False
    if(dest[0] == 3 or dest[0] == 4):
        if(dest[1] == 3 or dest[1] == 4):
            output = False
    # End of the area for Rules <--------------------------------------
    if(cash):
        cashing.add_can_goto((source, dest), output)
    return output

cashing = Casher()
if __name__ == '__main__':
    start = time.time()
    print("\n----------------------------------------\n") # Start configuration <-----------------------------------------
    board = Board([8, 8]) # Select your board size
    board.board[7][7].state = 1 # Select the wining tile (can be changed to whatever)
    board = solve(board, can_goto_check, 30) # change if you want the last parameter, Maximun Iterations
    print_board(board)
    print("\n----------------------------------------\n") # End configuration <---------------------------------------------
    end = time.time()
    print("Start time = ", start * 1000, "ms")
    print("End time = ", end * 1000, "ms")
    print("Time ellapsed = ", (end-start) * 1000, "ms")
