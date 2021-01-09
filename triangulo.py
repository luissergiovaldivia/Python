#import math
from math import sqrt


def area_triangulo(a, b, c):
	s = (a + b + c) / 2
	#s = 14.5
	m = float((s*(s-a)*(s-b)*(s-c)))
	return  sqrt(s*(s-a)*(s-b)*(s-c))

#s = 0
#m = 0 
#print(area_triangulo(1, 3, 25, s, m))
print(area_triangulo(1, 3, 2.5))

print(s)
