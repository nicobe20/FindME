from sqlite3 import Row
import pygame, sys
from pathfinding.core.grid import Grid as gd
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

class Pathfinder:
    def __init__(self,matrix):
        self.matrix = matrix
        self.gd = gd(matrix = matrix)
        self.select_surf = pygame.image.load('desktop/items/selector.png').convert_alpha()
        self.path = []

    def moused(self):
        mousep = pygame.mouse.get_pos()
        Row = mousep[1] // 32
        col = mousep[0] // 32
        loc = self.matrix[Row][col]
        if loc == 1:
            xy = pygame.Rect((col * 32, Row * 32),(32,32))
            pantalla.blit(self.select_surf,xy)

    def path(self):
        inix, iniy = [1,1]
        ini = self.gd.node(inix,iniy)

        mousep = pygame.mouse.get_pos()
        finx = mousep[1] // 32
        finy = mousep[0] // 32
        fin = self.gd.node(finx,finy)



        Finder = AStarFinder(diagonal_movement= DiagonalMovement.always)
        self.pathf,_ = Finder.find_path(ini,fin,self.gd)
        print(self.path)
        


    def update(self):
        self.moused()



matrix = [ 
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0],
    [0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0],
    [0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0],
    [0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0],
    [0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]
pygame.init()
pantalla = pygame.display.set_mode((960,640))
clock = pygame.time.Clock()
pathfinder = Pathfinder(matrix)
#setup




fondo = pygame.image.load('desktop/items/map.png').convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pathfinder.path()
    pantalla.blit(fondo,(0,0))
    pathfinder.moused()
    pygame.display.update()
    clock.tick(60)
