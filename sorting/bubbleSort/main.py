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
WHITE = (255, 255, 255)
COLORS = []

print("How tall do you want the window to be?  Can't be less than 400")
w_h = int(input())
if w_h < 400:
    w_h = 400
print("How many bars do you want to sort?  Recommended to keep the number fairly low (10 - 50).  ")
num_bars = int(input())
print("How long do you want to wait between each iteration?  Lower numbers causes the program to go faster.  \nEnter 0 for no delay.  \nRecommended delay is 0.1 for small numbers of bars, 0 for larger numbers.  ")
wait = float(input())
print("How wide do you want the bars to be?  ")
bar_width = int(input())
print("How tall do you want to cap the bars at?  Must be between 50 and window height.  ")
bar_height = int(input())
if bar_height < 50:
    bar_height = 50
if bar_height >= w_h:
    bar_height = w_h - 10
print("How far apart do you want the bars to be, in pixels?  ")
spacing = int(input())
if spacing < 1:
    spacing = 1
# w_h = 400
# num_bars = 10
# wait = 0.4
# bar_width = 10
# bar_height = 350
# spacing = 5
w_w = ((bar_width + spacing) * num_bars)
w_s = w_w, w_h
screen = p.display.set_mode(w_s)

def bubble_sort(l, i):
    if l[i].height > l[i+1].height:
        t1 = l[i]
        t2 = l[i+1]
        l[i].color = WHITE
        l[i+1].color = WHITE
        l[i] = t2
        l[i+1] = t1

def render(bars):
    screen.fill(BLACK)
    for b in range(len(bars)):
        bars[b].render(screen, (bar_width+spacing)*b)
    p.display.flip()

def create_array():
    return [Bar(bar_width, random.randint(50, bar_height), w_h-1, GREEN) for i in range(num_bars)]

def create_worst_case():
    return [Bar(bar_width, bar_height - (i * 5), w_h-1, GREEN) for i in range(num_bars)]

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
sorted = 0
while not done:
    p.event.pump()
    for e in p.event.get():
        if e.type == p.QUIT:
            sys.exit()
        if e.type == p.KEYDOWN:
            if e.key == p.K_ESCAPE:
                sys.exit()
            if e.key == p.K_SPACE:
                create_colors()
                bars = create_worst_case()
                s = 1
                o = num_bars - 1
                i = 0
                sorted = 0
            if e.key == p.K_BACKSPACE:
                create_colors()
                bars = create_array()
                s = 1
                o = num_bars - 1
                i = 0
                sorted = 0
            if e.key == p.K_a:
                num_bars *= 2
                w_w = ((bar_width + spacing) * num_bars)
                w_s = w_w, w_h
                screen = p.display.set_mode(w_s)
                create_colors()
                bars = create_array()
                s = 1
                o = num_bars - 1
                i = 0
                sorted = 0

    render(bars)

    if s == 1:
        time.sleep(0.5)
        start_time = p.time.get_ticks()
    else:
        time.sleep(wait)
    if o > 0 and i < o:
        bubble_sort(bars, i)
        render(bars)
        bars[i].color = GREEN
        bars[i+1].color = GREEN
        i += 1
    if i >= o:
        i = 0
        o -= 1
    if o <= 0:
        sorted += 1
    if sorted == 1:
        print("\nTook {0:.2f}s to finish sorting".format((p.time.get_ticks() - start_time)/1000))
    if s < 10:
        s += 1
    clock.tick(60)

p.quit()
