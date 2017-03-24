# Monte Carlo Method
'''
Function To Calculate Pi through
use of Random Stochastic Monte Carlo Method
'''
>>> import random
>>> import math
>>> def findPie(n):
	lessThan = 0
	x_Coords = []
	y_Coords = []
	for i in range (n):
		x_Coords.append(random.uniform(-1,1))
		y_Coords.append(random.uniform(-1,1))
	#print x_Coords
	#print y_Coords
	for i in range (n):
		if math.sqrt(x_Coords[i]*x_Coords[i] + y_Coords[i]*y_Coords[i]) <= 1:
			lessThan = lessThan+1
 	print lessThan
	return (float((4*lessThan))/n)

'''
Calculates Golden Mean
through use of Fibinnacci Numbers
'''
#GoldenMean
>>> def goldenMean(n):
	return float (fib(n+1))/float(fib(n))

 '''
Non-Recursive Fibinocci Sequence
'''
##Fibinocci Numbers
def fib(n):
	a = -1
	b = 1
	c = 0
	add = 0
	for i in range(n+1):
		c = a+b
		add = add+c
		a= b
		b = c
	return add

#Square Root of 2
'''
Finding Square Root of 2 Through
Newton-Raphson Method
'''
>>> def findRoot(error, guess):
	if guess*guess >= 2-error and guess*guess <= 2+error:
		return guess
	else:
		print guess
		guess = .5*(guess + 2/guess)
		return findRoot(error, guess)
>>> print findRoot(.01, 2)

#Continued Fraction Expansion Program
'''
Function that Caclulates
Continued Fraction Expansion
'''
>>> def contFraction(i, precision):
        getcontext().prec = precision
	a = 1
	b = 2
	frac = float(a/b)
	while i > 0:
		frac = (a/(b+frac))
		i = i-1
	return Decimal(1+frac)

#Newton Raphson Method for Golden Mean
>>> def goldenNewt(begin,step):
	if begin > 1.61803398874989480 and begin < 1.61803398874989489:
		print "Step" + str(step)
		step = step +1
		return Decimal(begin)
	else:
		print "Step " + str(step)
		step = step +1
		print Decimal(begin)
		begin =begin - ((math.pow(begin,2)-begin-1)/((2*begin)-1))
		return goldenNewt(begin, step)
	
##### Cont Frac PI
	'''Continued Fraction Expansion
           To Calculate Pi
           '''
>>> def contFracPi(n):
	val = float((n**2)/(2*n+1))
	while n>1:
	     n = n-1
	     val = val + (2*n+1)
	     val = (n**2)/val
	val = val + 1
	return (4/val

##### Euler Pi
                '''
                  Eulers Method of Pi
                  '''
>>> def eulerPi(n):
	total = 0
	float(total)
	below = 1
	while n > 0:
		add = float(1/float((below**2)))
		total = total + (1/float((below**2)))
		n = n-1
		below = below + 1
	total = total*6
	total = math.sqrt(total)
	return total
