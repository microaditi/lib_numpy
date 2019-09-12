import numpy as n
'''
z=n.eye(3)
print(z)
#to print identity matrix

z=n.random.random((3,3))
print(z)

#created a 3X3 matrix and filled it with random numbers
z=n.random.random((10,10))
zmin,zmax=z.min(),z.max()
print(zmin,zmax)
#to find min and max element of an array


z=n.random.random(30)
m=z.mean()
print(z)
print(m)

#created a vector of size 30 and found its mean value
'''
z=n.ones((10,10))
print(z)

z[1:-1,1:-1]=0
print(z)
