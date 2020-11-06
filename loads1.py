import numpy as np
import math

class load2:
    def load1(nelx,nely,load_array):
        # Set load
        ndof = 2*(nelx+1)*(nely+1)
        # Solution and RHS vectors
        f=np.zeros((ndof,1))
        u=np.zeros((ndof,1))
        for i in range(len(load_array)):
            m=2*(int(load_array[i][1][0])*(2*int(load_array[i][1][1])))-101
            print(m)
            lods=int(load_array[i][0][0])
            print(lods)
            f[m,0]=lods
        return f
