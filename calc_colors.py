#!/usr/bin/env python3

def cc():
    colors=[]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                colors.append(f'{i*0x40*2**16+j*0x40*2**8+k*0x40:06x}')
    return colors
