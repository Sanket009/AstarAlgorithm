import pygame

GameMode = True
margin = 5
gap = 50
win = pygame.display.set_mode((560,560))
pygame.display.set_caption('AstarAlgorithm')
color = (255,255,255)
flag = ''
grid = []

for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)

nodes = [] #contains starting node and ending node 


while GameMode:
    pygame.time.delay(60)
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
                nodes.append((row,column))  #adds starting node to nodes[1]

            elif flag == 's':
                grid[row][column] = 2
                nodes.append((row,column))  #adds starting node to nodes[0]
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
                

                pygame.draw.rect(win,color,((margin + gap)*column + margin,
                (margin + gap)*row + margin,
                gap,
                gap))
                
                pygame.display.update()
                    
 
pygame.quit()



