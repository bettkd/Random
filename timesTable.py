def times_table(s):
    n=int(input('Please enter a positive integer between 1 and 15: '))
    for row in range(n+1):
        s = ''
    	for col in range(n+1):
        	s += '{:3} '.format(row * col)
   	print(s)

times_table(10)
