import pygame as p 

class Bar(): 
    def __init__(self, width, height, y, color): 
        self.width = width 
        self.height = height 
        self.y = y - self.height 
        self.color = color 

    def render(self, screen, x): 
        p.draw.rect(screen, self.color, (x, self.y, self.width, self.height)) 