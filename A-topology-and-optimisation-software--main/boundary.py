import numpy as np
class BC:
    def fixed(nelx,nely):
        # BC's and support
        dofs=np.arange(2*(nelx+1)*(nely+1))
        #fixed=np.union1d(np.array([80]),dofs[8050:8060:1])
        #fixed=np.union1d(dofs[0:2*(nely+1):2],np.array([2*(nelx+1)*(nely+1)-1]))
        fixed=np.union1d(dofs[0:2*(nely+1):1],[0])
        return fixed
