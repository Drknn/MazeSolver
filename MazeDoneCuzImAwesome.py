class Node:
    def __init__(self, state, parent = None, action = None):
        self.state = state
        self.parent = parent
        self.action = action

#Maze
Labirinto = [['#',' ',' ',' '],
             [' ',' ','X',' '],
             [' ','#','#',' '],
             [' ',' ',' ','#'],
             [' ',' ',' ','O']]

#Finding X

posy = -1
posygoal = -1

for m in Labirinto:

    posy = posy + 1

    for n in m:

        if n == 'X':
            firstpos = [m.index('X'),posy]

#Finding O

for q in Labirinto:

    posygoal = posygoal + 1

    for w in q:
        if w == 'O':
            goalpos = [q.index('O'),posygoal]


frontier = [Node(firstpos)]
Nodinho = frontier[0]

#creating loop and defining possible actions

while Nodinho.state != goalpos:

    Nodinho = frontier[0]
    possibleactions = ['up', 'left', 'right', 'down']

    #removing actions from walls and maze limits

    if Nodinho.state[0] == 0:
        possibleactions.remove('left')

    elif Labirinto[Nodinho.state[1]][Nodinho.state[0]-1] == "#":
        possibleactions.remove('left')

    if Nodinho.state[0] >= len(Labirinto[0])-1:
        possibleactions.remove('right')
    
    elif Labirinto[Nodinho.state[1]][Nodinho.state[0]+1] == "#":
        possibleactions.remove('right')

    if Nodinho.state[1] == 0:
        possibleactions.remove('up')
    
    elif Labirinto[Nodinho.state[1]-1][Nodinho.state[0]] == "#":
        possibleactions.remove('up')

    if Nodinho.state[1] >= len(Labirinto)-1:
        possibleactions.remove('down')
    
    elif Labirinto[Nodinho.state[1]+1][Nodinho.state[0]] == "#":
        possibleactions.remove('down')



    #defining next node, using the current node as parent and appending to the frontier

    for i in possibleactions:
        if i == 'up':
            nextpos = [Nodinho.state[0],Nodinho.state[1]-1]

        if i == 'down':
            nextpos = [Nodinho.state[0],Nodinho.state[1]+1]
        
        if i == 'right':
            nextpos = [Nodinho.state[0]+1,Nodinho.state[1]]
        
        elif i == 'left':
            nextpos = [Nodinho.state[0]-1,Nodinho.state[1]]

        frontier.append(Node(nextpos, (Nodinho), i))

    frontier.pop(0)


#Going backwards from the node that arrived in the end and painting the path with '*'


while Nodinho.state != firstpos:
    Nodinho = Nodinho.parent
    if Labirinto[Nodinho.state[1]][Nodinho.state[0]] == 'X':break
    Labirinto[Nodinho.state[1]][Nodinho.state[0]] = '*'
  

for l in Labirinto:
    print (l)
