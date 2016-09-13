import pygame as p 
import random 
import time 
import sys 
from bar import * 

p.init() 
p.display.set_caption('Bubble Sort') 

BLACK = (0, 0, 0) 
RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 
YELLOW = (255, 255, 0) 
COLORS = [] 
w_s = w_w, w_h = 1600, 640 
screen = p.display.set_mode(w_s) 
num_bars = 145 
bar_height = 200 

def bubble_sort(l): 
    for o in range(len(l)-1, 1, -1): 
        for i in range(0, o): 
            if l[i].height > l[i+1].height: 
                t1 = l[i] 
                t2 = l[i+1] 
                l[i] = t2 
                l[i+1] = t1 
        break 
            
def create_array(): 
    return [Bar(random.randint(1, bar_height)*3, w_h-10, random.choice(COLORS)) for i in range(num_bars)]
def create_colors(): 
    global COLORS 
    COLORS = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for i in range(5)] 

create_colors() 
bars = create_array() 
clock = p.time.Clock() 
done = False 
s = 1 
while not done: 
    p.event.pump() 
    for e in p.event.get(): 
        if e.type == p.QUIT: 
            sys.exit() 
        if e.type == p.KEYDOWN: 
            if e.key == p.K_ESCAPE: 
                sys.exit() 
            if e.key == p.K_BACKSPACE: 
                create_colors() 
                bars = create_array() 
                s = 1 
                
    screen.fill(BLACK) 
    for b in range(len(bars)): 
        bars[b].render(screen, ((bars[b].width+1)*b))
    p.display.flip() 
    if s == 1: 
        time.sleep(0.5) 
    else: 
        time.sleep(0.1) 
    bubble_sort(bars) 
    if s < 10: 
        s += 1 
    clock.tick(60) 

p.quit() 
