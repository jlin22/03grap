import math


def print_matrix( matrix ):
	a = ""
	for c in matrix:
		for i in range(len(c)):
			a += str((c[i])) + " "
			if (i == len(c) - 1):
				a += "\n"
	print(a)
 
  
def ident( matrix ):
	for c in range(len(matrix)):
		for r in range(len(matrix[c])):
			if c == r :
				matrix[c][r] = 1
			else:
				matrix[c][r] = 0
	return matrix

    


#m1 * m2 -> m2 
def matrix_mult( m1, m2 ):
	#m1 = r1 x c1
	#m2 = r2 x c2
	#ans = c1 x r2
	ans = new_matrix(rows = len(m1[0]), cols = len(m2))
	# arow is dim of row in answer, acol is dim of col in answer
	for arow in range(len(m1[0])):
		for acol in range(len(m2)):
			#ans[arow][acol] is what you are adding to
			for index in range(len(m1)):
				ans[arow][acol] += (m1[arow][index] * m2[index][acol])
	return ans


		
			



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m



