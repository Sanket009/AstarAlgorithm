import pygame
pygame.init()

CanvasLength = 560
CanvasBreadth = 560 
margin = 5
GameRun = True
win = pygame.display.set_mode((CanvasLength,CanvasBreadth))
pygame.display.set_caption("A*Algorithm")
color = (255,255,255)
flag = ''
win.fill(0)
font = pygame.font.SysFont('dejavuserif',10)
text = font.render('HelloWorld',True,(0,255,0))

win.blit(text,(560/2,560/2))
pygame.display.update()