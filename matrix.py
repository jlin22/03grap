import math


def print_matrix( matrix ):
	a = ""
	for c in matrix:
		for i in range(len(c)):
			a += str((c[i])) + " "
			if (i == len(c) - 1):
				a += "\n"
	print(a)
 
#m1 * m2 -> m2   
def ident( matrix ):
	for c in range(len(matrix)):
		for r in range(len(matrix[c])):
			if c == r :
				matrix[c][r] = 1
			else:
				matrix[c][r] = 0
	return matrix

    



def matrix_mult( m1, m2 ):
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

#testing
m = new_matrix()
m = ident(m)
print_matrix(m)
