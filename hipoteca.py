#import math
from math import sqrt


def interes(h, i, n):

	r = (i/(100 * 12))
	v1 = (h * r)
	v2 = -(12 * n)
	v3 = (1 + r)
	m = (v1 / (1 - (v3 ** v2 )))
	m = '{0:.2f}'.format(m)
	return m

#s = 0
#m = 0 
#print(area_triangulo(1, 3, 25, s, m))
#print('{0:.2f}'.format(interes(150000, 4.75, 15))

#print(s)

print(interes(150000, 4.75, 15))