from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
m1 = new_matrix()
m2 = new_matrix()

print("identity function")
ident(m1)
print_matrix(m1)
print("zero matrix")
print_matrix(m2)
m3 = matrix_mult(m1, m2)
print("product of identity and zero")
print_matrix(m3)	

edge = new_matrix(rows=4, cols=4)
print("add points (500,500,0) and (0,0,0)")
add_point(edge, 500, 500, 0)
add_point(edge, 0, 0, 0)
print_matrix(edge)
print("add edge (250,0,0), (250,500,0)")
add_edge(edge, 250, 0, 0, 250, 500, 0)
print_matrix(edge)
draw_lines(edge, screen, color )
save_ppm(screen, "image.ppm")
#display(screen)