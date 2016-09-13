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
num_bars = 144 
bar_height = 200 

def bubble_sort(l, i): 
    if l[i].height > l[i+1].height: 
        t1 = l[i] 
        t2 = l[i+1] 
        l[i] = t2 
        l[i+1] = t1 
    
def render(bars): 
    screen.fill(BLACK) 
    for bar in bars: 
        bar.render(screen) 
    p.display.flip() 
            
def create_array(): 
    return [Bar(random.randint(1, bar_height)*3, w_h-10, random.choice(COLORS)) for i in range(num_bars)] 

def create_colors(): 
    global COLORS 
    for i in range(num_bars): 
        c = (random.randint(50, 250), random.randint(50, 250), random.randint(50, 250)) 
        if not c in COLORS: 
            COLORS.append(c) 
        else: 
            c = (random.randint(50, 250), random.randint(50, 250), random.randint(50, 250)) 

create_colors() 
bars = create_array() 
clock = p.time.Clock() 
done = False 
s = 1 
o = num_bars - 1 
i = 0 
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
                o = num_bars - 1 
                i = 0 
    screen.fill(BLACK) 
    for b in range(len(bars)): 
        bars[b].render(screen, 11*b) 
    p.display.flip() 
    
    if s == 1: 
        time.sleep(0.5) 
    #else: 
        #time.sleep(0.1) 
    if o > 1 and i < o: 
        bubble_sort(bars, i) 
        i += 1 
    if i >= o: 
        i = 0 
        o -= 1 
    if s < 10: 
        s += 1 
    #clock.tick(60) 

p.quit() 
