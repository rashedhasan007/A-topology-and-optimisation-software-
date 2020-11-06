import numpy as np
from matplotlib import colors
import matplotlib.pyplot as plt
import matplotlib.cm as cm
data = np.load('data.npy')
print(data)
xPhys=data.copy()
v=xPhys.reshape((150,100)).T
plt.ion() # Ensure that redrawing is possible
fig,ax = plt.subplots()
im = ax.imshow(v, cmap='Blues',
        interpolation='nearest',norm=colors.Normalize(vmin=0,vmax=1))

#plt.show()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors

a =np.array([[156, 138, 156],
             [1300, 137, 156],
             [138, 138, 1300],
             [137, 137, 137]])

ca = np.array([[15,20,00,200],
               [13,10,25,25],
               [13,208,10,40],
               [10,6,15,76]])

u, ind = np.unique(a, return_inverse=True)
b = ind.reshape((a.shape))
print(b)

colors = ca[ca[:,0].argsort()][:,1:]/255.
cmap = matplotlib.colors.ListedColormap(colors)
norm = matplotlib.colors.BoundaryNorm(np.arange(len(ca)+1)-0.5, len(ca))
print(cmap)
print(colors)
plt.imshow(v, cmap=cmap, norm=norm)

cb = plt.colorbar(ticks=np.arange(len(ca)))
cb.ax.set_yticklabels(np.unique(ca[:,0]))

plt.show()
