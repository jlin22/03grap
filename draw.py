from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    index = 0
    while (index < len(matrix[0])) :
        draw_line(matrix[0][index], matrix[1][index], matrix[0][index+1], matrix[1][index+1], screen, color)
        index += 2
    pass

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)
    pass

def add_point( matrix, x, y, z=0 ):
    (matrix[0]).append(x)
    (matrix[1]).append(y)
    (matrix[2]).append(z)
    (matrix[3]).append(1)
    pass

#def plot( screen, color, x, y ):
#0=(dy)x-(dx)y+(dx)b
#0=Ax+By+C
def draw_line( x0, y0, x1, y1, screen, color ):
    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt
        
    dy = y1-y0
    dx = x1-x0
    A = dy
    B = -dx
    x = x0
    y = y0

    # 0 < dy/dx < 1 
    # Octant 1
    if (0 < dy < dx): 
        d= 2*A+B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d>0):
                y+=1    
                d+=2*B
            x+=1
            d+=2*A


    # 1 < dy/dx 
    # Octant 2
    elif (dx < dy):
        d = A+2*B
        while (y <= y1):
            plot(screen, color, x, y)
            if (d<0):
                x+=1    
                d+=2*A
            y+=1
            d+=2*B



    # -1 < dy/dx < 0
    # Octant 8
    elif (-dx < dy < 0):
        d = 2*A-B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d<0):
                y-=1
                d-=2*B
            x+=1
            d+=2*A



    # dy/dx < -1
    # Octant 7
    elif (dy < -dx):    
        d = A-2*B
        while (y >= y1):
            plot(screen, color, x, y)
            if (d>0):
                x+=1
                d+=2*A
            y-=1
            d-=2*B

    # dy/dx = 1
    elif (dy == dx):    
        while (x <= x1):
            plot(screen, color, x, y)
            x+=1
            y+=1


    # dy/dx = -1
    elif (dy == -dx):
        while (x <= x1):
            plot(screen,color, x,y)
            x+=1
            y-=1

    # dy/dx = 0
    elif (dy == 0) :
        while (x<=x1):
            plot(screen, color, x,y)
            x+=1


    # dy/dx = infinity
    elif (dx== 0 and dy > 0):
        while (y<=y1):
            plot(screen,color,x,y)
            y+=1


    # dy/dx = -infinity 
    elif (dx == 0 and dy < 0):
        while (y>=y1):
            plot(screen,color,x,y)
            y-=1


    pass

