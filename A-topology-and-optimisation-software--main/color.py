#plt.show()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
data = np.load('data.npy')
print(data)
xPhys=data.copy()
v=xPhys.reshape((150,150)).T


ca=np.array([[000,000,1,1],
             [000,000,1,.8],
             [00,00,1,.7],
             [000,.5,00,1],
             [000,.5,000,.8],
             [000,.5,000,.7],
             [1,1,000,1],
             [1,1,000,.8],
             [1,1,000,.7],
             [1,000,000,1],
             [1,000,000,1],
             [1,000,000,1]])


colors = ca[ca[:,0].argsort()][:,1:]/1.
cmap = matplotlib.colors.ListedColormap(ca)
#channel=np.arange(len(ca)+1)-0.5
channel=[0.000,.0010,.0050,.0080,.010,.070,.1,.3,.5,.7,.8,1]
#channel=[1,.8,.7,.5,.3,.1,.05,.010,.0080,.0050,.0010,.0001]
norm = matplotlib.colors.BoundaryNorm(channel, len(ca))

plt.imshow(v, cmap=cmap, norm=norm)

cb = plt.colorbar(ticks=np.arange(len(ca)))
cb.ax.set_yticklabels(np.unique(ca[:,0]))

fig=plt.show()