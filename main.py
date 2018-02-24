from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
m1 = new_matrix()
m2 = new_matrix()

ident(m1)
print_matrix(m2)
m3 = matrix_mult(m1, m2)
print_matrix(m3)	


#draw_lines( matrix, screen, color )
#display(screen)