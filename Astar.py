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

font = pygame.font.SysFont('dejavuserif',10)

nodes = [] #nodes[0] is ending node (red) and node[1] starting node (green) 
OpenList = [] #contains lists that need to be checked , here checked means if they have the shortest path 
ClosedList = [] #contains lists that have been checked 
parents = []  
children = [] #children color is light blue (3, 252, 202)
values = {} 

for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)
        values.update({(row,column) : []})


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
            print("Clicked at ",pos,"and",row,column)
            
    
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
                elif len(nodes) >=1:
                    values.update({(row,column):[( abs(row - nodes[0][0]) + abs(column - nodes[0][1]) )] })
                


                pygame.draw.rect(win,color,((margin + gap)*column + margin,
                (margin + gap)*row + margin,
                gap,
                gap))
                
                if values[(row,column)] != []:   #Checking if the values has some h,g,f values
                    text = font.render( str(values[(row,column)][0]),True,(0,0,0) )
                    win.blit(text,( (margin + gap)*column + margin + gap - 20,
                    (margin + gap)*row + margin  ) )

                
                pygame.display.update()

                #Algorithm Starts Here

                while OpenList != []:
                    CurrentNode = 0 
                    
                    if len(OpenList) == 1:
                        CurrentNode = OpenList[len(OpenList) - 1 ]
                    else:
                        for a in range(len(OpenList) - 1):
                            if OpenList[a] < OpenList[a+1]:
                                OpenList[a+1] , OpenList[a] = OpenList[a] , OpenList[a+1] #Swapping
                        CurrentNode = OpenList[len(OpenList) - 1 ]
                    
                    #Now that we have CurrentList , We need to evaluate the Children of it
                    for a in range(-1,2):
                        for b in range(-1,2):
                            if a == 0 and b == 0:
                                 continue
                            else:
                                children.append((CurrentNode[0] + a , CurrentNode[1] + b))
                                grid[CurrentNode[0] + a ][CurrentNode[1] + b] = 4

                    break



                    
                            
                
                    
pygame.quit()

