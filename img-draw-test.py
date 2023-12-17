#!/usr/bin/env python3

from PIL import Image,ImageDraw
from calc_colors import cc
colors = cc()
vertical_divider=10

def coords2R(w,dimensions_of_a_screen):
    x0,y0  ,x1,y1 = w
    x_shift =  dimensions_of_a_screen[0] + vertical_divider
    x0_ = x0 + x_shift
    x1_ = x1 + x_shift
    return((x0_,y0,x1_,y1))

def coords2L(w,dim):
    return(w)

def coords2(mode,w,d):
    if mode == "thing":
        return(coords2L(w,d))
    elif mode == "thing2":
        return(coords2R(w,d))

def get_screen_dim(layout_info):
    dim_x=0
    dim_y=0
    for win in layout_info:
        x, y, w, h = win
        dim_x=max(x+w,dim_x)
        dim_y=max(y+h,dim_y)
    return (dim_x,dim_y)

def gen_images(testname):
    global colors
    with open(f'output_test_{testname}','rt') as f:
        data0 = eval(f.read())
    screen_dim  = get_screen_dim(data0[0]['thing' ])
    screen_dim2 = get_screen_dim(data0[0]['thing2'])
    if not screen_dim == screen_dim2:
        from sys import exit
        from sys import stderr
        stderr.write(f"ERROR: dim: {screen_dim} != dim2 : {screen_dim2}  \n")
        from pprint import pprint
        pprint(data0[0],stream=stderr)

        exit(1)
    side_by_side_screen = screen_dim[0]*2+vertical_divider,screen_dim[1]
    print(f'screen_dim={screen_dim}')
    print(f'side_by_side={side_by_side_screen}')
    i=Image.new("RGBA",(side_by_side_screen), (255, 255, 255, 0)) 
    d=ImageDraw.Draw(i)
    
    count=0
    for t in data0:
        for k in t.keys():
            windows=t[k]
            for win in windows:
                x, y, w, h = win 
                x0=x ; y0=y
                x1=x+w ; y1=y+h
                win = coords2(k,(x0,y0,x1,y1),screen_dim)
                if len(colors) < 1:
                              colors = cc()
                d.rectangle(win,fill="#"+colors.pop())
        fname=f"./ratio_pictures/img_{testname}_{count}.png"
        print(f"writing file: {fname} ")
        i.save(fname)
        count+=1

gen_images('add_windows')
gen_images('resizing')
