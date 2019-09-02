import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
from sys import exit
import ConwayMain
 
class Cube():

    def __init__(self, surface, pos, width, rows, color):
        self.surface = surface
        self.pos = pos
        self.width = width
        self.rows = rows
        if color == "white":
            self.color = (255,255,255)
        else:
            self.color = (0,0,0)
 
    def draw(self):
        dis = self.width // self.rows
        i = self.pos[0]
        j = self.pos[1]
 
        pygame.draw.rect(self.surface, self.color, (i*dis+1, j*dis+1, dis-1, dis-1))

class GUI():
    
    def __init__(self, width, rows):
        self.width = width
        self.rows = rows
        self.surface = pygame.display.set_mode((width, width))
 
    def draw_init(self):
        pygame.display.set_caption("Conway's Game of Life")
        self.surface.fill((0,0,0))
        self.draw_grid()
    
    def draw_grid(self):
        sizeBtwn = self.width // self.rows
        x = 0
        y = 0
        for l in range(self.rows):
            x = x + sizeBtwn
            y = y + sizeBtwn
    
            pygame.draw.line(self.surface, (255,255,255), (x, 0),(x, self.width))
            pygame.draw.line(self.surface, (255,255,255), (0, y),(self.width, y))
    
    def draw_cube(self, pos):
        cube = Cube(self.surface, pos, self.width, self.rows, "white")
        cube.draw()
        pygame.display.update()
    
    def remove_cube(self, pos):
        cube = Cube(self.surface, pos, self.width, self.rows, "black")
        cube.draw()
        pygame.display.update()


def main():
    # INIT for conwayMain
    start_positions = []

    # Something wrong with row/column
    start_obj = [[3,3],[4,3],[5,3],[5,2],[4,1]]
    for obj in start_obj:
        start_positions.append(ConwayMain.Position(obj[0], obj[1]))
    
    world_width = 20
    world_height = 20
    world = [[False for x in range(world_width)] for y in range(world_height)]

    con_handler = ConwayMain.Conway_handler(start_positions, world)

    # Init for GUI
    width = 500
    rows = world_width
    gui = GUI(width, rows)
    gui.draw_init()

    # Draw starting cells
    for i in range (len(con_handler.world)):
        for j in range (len(con_handler.world[0])):
            if (world[i][j]):
                gui.draw_cube([i,j])

    clock = pygame.time.Clock()

    while True:
        # If X button is called, close game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        con_handler.spawn_new_conways()
        con_handler.update_conwoys()

        for i in range (len(con_handler.world)):
            for j in range (len(con_handler.world[0])):
                if (world[i][j]):
                    gui.draw_cube([i,j])
                else:
                    gui.remove_cube([i,j])

        pygame.time.delay(100)
        clock.tick(10)     
 
if __name__ == '__main__':
    main()