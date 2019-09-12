import numpy as np

w=np.diag(1+np.arange(4),k=-1)
print(w)
#to print values 1,2,3,4 just below the diagonal
print("\n")
z=np.diag(1+np.arange(6),k=1)
print(z)
#to print values 1,2,3,4,5,6 just above the diagonal
