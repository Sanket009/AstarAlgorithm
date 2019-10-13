import pygame
pygame.init()
GameMode = True
margin = 5
gap = 50
win = pygame.display.set_mode((560,560))
pygame.display.set_caption('AstarAlgorithm')
color = (255,255,255)
flag = ''
grid = []
count = 0
font = pygame.font.SysFont('dejavuserif',10)
nodes = [] #nodes[0] is ending node (red) and node[1] starting node (green) 
OpenList = [] #contains lists that need to be checked , here checked means if they have the shortest path 
ClosedList = [] #contains lists that have been checked 
parentAndChild = {}  
children = {} 
values = {} #OpenListValues
#ChildValues = {}  
CurrentNode = (0,0)
l = []
Obstacles = []


#Function for extracting the paths
def checkIf(node):
    for a in range(1,len(parentAndChild)):
        x = list(parentAndChild.keys())[-a]
        if node not in parentAndChild[x]: continue
        l.append(x)
        grid[x[0]][x[1]] = 4 #setting the path color to lightBlue
        
        if node == nodes[1]: break
        checkIf(x)

#Generating 9x9 Grids
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)
        values.update({(row,column) : [0,0,0]})

while GameMode:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameMode = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                flag = 'e'
                print('pressed e')
            elif event.key == pygame.K_s:
                flag = 's'
                print('pressed s') 
            elif event.key == pygame.K_o:
                print('pressed o')
                flag = 'o'
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (gap + margin)
            row = pos[1] // (gap + margin)
            if flag == 'e':
                grid[row][column] = 1
                nodes.append((row,column))  #adds starting node to nodes[0]
            elif flag == 's':
                grid[row][column] = 2
                nodes.append((row,column))  #adds starting node to nodes[1]
                values.update({(row,column) : [0,0,0]}) #setting the StartingNode to 0,0,0
                OpenList.append((row,column))  #adding starting node to the open list
            elif flag == 'o':
                grid[row][column] = 3
                Obstacles.append((row,column))
    
    for row in range(10):
            for column in range(10):
                
                color = (255,255,255)
                if grid[row][column] == 1:
                    color = (255,0,0)
                elif grid[row][column] == 2:
                    color = (0,255,0)
                elif grid[row][column] == 3:
                    color = (247,230,69)
                elif grid[row][column] == 4:
                    color = (3,252,202)
                elif len(nodes) == 1:
                    values.update({(row,column):[( abs(row - nodes[0][0]) + abs(column - nodes[0][1]) ),0,0] })
                
                pygame.draw.rect(win,color,((margin + gap)*column + margin,
                (margin + gap)*row + margin,
                gap,
                gap))
                
                if values[(row,column)] != []:   #Checking if the values has some h,g,f values
                    text = font.render( str(values[(row,column)][0]),True,(0,0,0) )
                    win.blit(text,( (margin + gap)*column + margin + gap - 15,
                    (margin + gap)*row + margin  ) )

                    text1 = font.render( str(values[(row,column)][1]),True,(0,0,0) )
                    win.blit(text1,( (margin + gap)*column + margin + gap - 45,
                    (margin + gap)*row + margin  ) )

                    text2 = font.render( str(values[(row,column)][2]),True,(0,0,0) )
                    win.blit(text2,( (margin + gap)*column + margin + gap - 30,
                    (margin + gap)*row + margin + gap - 30 ) )

                
                pygame.display.update()

    #Algorithm Starts Here
    while OpenList != []:
        count +=1
        CurrentNode = (0,0) 
                    
        if len(OpenList) == 1:
            CurrentNode = OpenList[len(OpenList) - 1 ]
        else: 
            for a in range(len(OpenList) - 1):
                if values[OpenList[a]][2] < values[OpenList[a+1]][2]:
                    OpenList[a] , OpenList[a+1] = OpenList[a+1] , OpenList[a] #Swapping
            CurrentNode = OpenList[-1]
        
        #Final Line Breaks Here
        if CurrentNode == nodes[0]:

            print('The count is : ',count)
            OpenList.clear()
            break
        
        
        parentAndChild.update({CurrentNode : []})
        OpenList.remove(CurrentNode)
        ClosedList.append(CurrentNode)
                        
        #Now that we have CurrentNode , We need to evaluate the Children of it
        for a in range(-1,2):
            for b in range(-1,2):
                if a == 0 and b == 0: continue
                else:
                    x = CurrentNode[0] + a
                    y = CurrentNode[1] + b
                    if ( x >=0 and x<= 9) and (y >=0 and y <=9):
                        #if (x,y) in Obstacles: continue
                        #if abs( x - CurrentNode[0] ) + abs( y - CurrentNode[1] ) == 2:

                        children.update({(x,y) : [values[(x,y)][0],0,0]})
                        #grid[x][y] = 4
                    
        for child in children:
            if child in ClosedList : continue
            z = 14 if abs( child[0] - CurrentNode[0] ) + abs( child[1] - CurrentNode[1] ) == 2 else 10
            children[child][1] = values[CurrentNode][1] + z
            children[child][2] = children[child][0] + children[child][1] # F Cost
            #Skip if there's any obstacle
            if child in Obstacles:
                continue
            if abs( child[0] - CurrentNode[0] ) + abs( child[1] - CurrentNode[1] ) == 2:
                if ((child[0] - 1) and (child[0] - 1)) in Obstacles: 
                    continue
                if ((child[0] + 1) and (child[0] + 1)) in Obstacles:
                    continue
                 
            if child in OpenList:
                if children[child][1] >= values[child][1]: continue

            #adding child to the OpenList
            OpenList.append(child)
            values[child] = children[child]            
            parentAndChild[CurrentNode].append(child) 

        children.clear()
        checkIf(nodes[0])
                        
pygame.quit()

