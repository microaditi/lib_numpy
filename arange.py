import numpy as n

'''
z=n.arange(10,50)
print(z)
#vector with values ranging from 10mto 49

z=n.arange(50)
print(z)
#printing vector from 0 to 49
z=z[::-1]
print(z)
#printing vector in reverse order

z=n.arange(9).reshape(3,3)
print(z)
#reshaping array of size 9 into shape (3,3)
'''

nz = n.nonzero([1,2,0,0,4,0])
print(nz)


