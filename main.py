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

matrix = new_matrix(rows=4, cols=4)
add_edge(matrix, 240, 40, 0, 260, 40, 0)
add_edge(matrix, 240, 40, 0, 240, 250, 0)
add_edge(matrix, 260, 40, 0, 260, 250, 0)
add_edge(matrix, 215, 250, 0, 285, 250, 0)
add_edge(matrix, 215, 250, 0, 215, 350, 0)
add_edge(matrix, 285, 250, 0, 285, 350, 0)
i = 10
while 215 + i < 285:
	add_edge(matrix, 215+i, 260, 0, 215+i, 350, 0)
	i+= 10
i = 0
while 215 + i < 265:
	add_edge(matrix, 215+i, 350, 0, 225+i, 350, 0)
	add_edge(matrix, 225+i, 260, 0, 235+i, 260, 0)
	i+=20
add_edge(matrix, 275, 350, 0, 285, 350, 0)

draw_lines(matrix, screen, color )
display(screen)