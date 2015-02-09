#! usr/bin/Python
# Author: Dominic Bett
# Script: Multiplication of two matrices
# Feb 9, 2015

class IncompatibilityError(RuntimeError):
   pass

def multiplymatrix(A, B):
	cA =len(A[0])
	cB = len(B[0])
	rA = len(A)
	rB = len(B)

	if (cA != rB):
		raise IncompatibilityError('Oops! Cannot multiply the two matrices!')
	else:
		#initialize AXB to 0
		AB = [[0 for i in range(cB)] for i in range(rA)]

		#Calculate AXB
		for i in range(rA):
			for j in range(cB):
				for k in range(rB):
					AB[i][j] += A[i][k] * B[k][j]			
		return AB

def main():
	A = [[-1, 3],
		[4, -2],
		[5, 0]] #3X2 matrix

	B = [[-3, 2],
		[-4, 1]] #2X2 matrix

	try:
		AB = multiplymatrix(A, B)

		for m in AB:
			print (m)
	except Exception, e:
		print e.args
	

if __name__ == '__main__':
	main()