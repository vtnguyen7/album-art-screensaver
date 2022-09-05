#!/usr/bin/env python

import os
import time
import random
import pygame
import json

def get(js, value, default):

    try:
        return(js[value])
    except:
        return(default)

def fetch_images(directory, filetypes, keyword, exword):

    i = []

    for f in os.listdir((os.path.expanduser(directory))):

        ext = f.split(".")[-1]
        
        if ext in filetypes and f.__contains__(keyword) and not(f.__contains__(exword)):

            i.append(directory + f)

    return i

def make_positions(x, y, imagex, imagey):

    p = []

    colnum = x//imagex + 1
    rownum = y//imagey + 1

    for c in range(colnum):

        for r in range(rownum):

            p.append((c*imagex, r*imagey))

    return(p)

def fetch_init(positions, imgs):

    a = []
    b = []

    for p in positions:

        new = random.choice(imgs)

        while new in b:

            new = random.choice(imgs)

        a.append([p, new])
        b.append(new)

    return(a, b)

def array_replace(arr, ims, c_u, c, r):

    for i in arr:

        if (i[0][0] == c*cover_size) and (i[0][1] == r*cover_size):

            new = random.choice(ims)

            while new in c_u:

                new = random.choice(imgs)
            
            l = i[0]
            c_u.remove(i[1])
            i[1] = new
            c_u.append(i[1])

    return(arr, c_u, l)

def draw_array(array):

    for tup in array:
        
        impos = tup[0]
        im = pygame.image.load(os.path.expanduser(tup[1]))

        try:

            if impos == last:

                im = im.convert_alpha()
                im.fill((255, 255, 255, 196), special_flags=pygame.BLEND_RGBA_MULT)

        except:

            pass

        display_surface.blit(pygame.transform.smoothscale(im, (cover_size, cover_size)), tup[0])

if __name__ == "__main__":

    try:
        sett = json.load(open(os.path.expanduser('~/.config/album-art-screensaver/album-art-screensaver.json')))
    except:
        sett = {}

    cover_size = get(sett, "cover size", 150)
    w = get(sett, "width", 1920)
    h = get(sett, "height", 1080)
    directory = get(sett, "image directory", "~/.cache/lollypop/")
    keyword = get(sett, "keyword", "200")
    exword = get(sett, "excluded word", "ROUNDED")
    exts = get(sett, "extensions", ["jpg", "png"])

    pygame.init()
    display_surface = pygame.display.set_mode((w, h), pygame.FULLSCREEN)
    pygame.mouse.set_visible(False)
    
    positions = make_positions(w, h, cover_size, cover_size)
    imgs = fetch_images(directory, exts, keyword, exword)
    [array, currently_used] = fetch_init(positions, imgs)
    tick_change = [0, 0]

    while True:
        
        # number of ms after init
        ticks = pygame.time.get_ticks()
        
        # this just makes sure that we only change the image once, when we transition from 3 seconds to 0 seconds mod 4
        tick_change[1] = tick_change[0]
        tick_change[0] = ticks//1000
    
        # change the image if it's been 4 seconds
        if (tick_change[0] % 4 == 0) and (tick_change[0] != tick_change[1]):
            
            r = random.choice(range((w//cover_size) + 1))
            c = random.choice(range((h//cover_size) + 1))
    
            [array, currently_used, last] = array_replace(array, imgs, currently_used, r, c)
        
        # draw the array
        
        draw_array(array)

        # if the arrays aren't equal, draw another one on top of the old one
    
        for event in pygame.event.get():
            if event.type in (
                pygame.QUIT,
                pygame.KEYDOWN,
                pygame.KEYUP,
                pygame.MOUSEBUTTONDOWN,
                pygame.MOUSEBUTTONUP,
                pygame.MOUSEWHEEL
            ):
                pygame.quit()
                quit()
        pygame.display.update()
