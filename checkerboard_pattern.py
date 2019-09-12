import numpy as np
z=np.zeros((8,8),dtype=int)
z[1::2,::2]=1
z[::2,1::2]=1
print(z)
