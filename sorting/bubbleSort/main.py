import pygame as p 
import random 
import time 
import sys 
from bar import * 

p.init() 
p.display.set_caption('Bubble Sort') 

BLACK = (0, 0, 0) 
GREEN = (0, 255, 0) 

w_s = w_w, w_h = 640, 640 
screen = p.display.set_mode(w_s) 

bars = [Bar(random.randint(1, 100)*3, 400, GREEN) for i in range(20)]
def bubble_sort(l): 
    for o in range(len(l)-1, 1, -1): 
        for i in range(0, o): 
            if l[i].height > l[i+1].height: 
                t1 = l[i] 
                t2 = l[i+1] 
                l[i] = t2 
                l[i+1] = t1 
        break 
                
clock = p.time.Clock() 
done = False 
while not done: 
    p.event.pump() 
    for e in p.event.get(): 
        if e.type == p.QUIT: 
            sys.exit() 
        if e.type == p.KEYDOWN: 
            if e.key == p.K_ESCAPE: 
                sys.exit() 
            if e.key == p.K_SPACE: 
                bubble_sort(bars) 
                
    screen.fill(BLACK) 
    for b in range(len(bars)): 
        bars[b].render(screen, (bars[b].width+30*b))
    p.display.flip() 
    clock.tick(60) 

p.quit() 
