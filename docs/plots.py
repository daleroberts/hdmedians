import numpy as np
import hdmedians as hd
import matplotlib.pyplot as plt

def pcoord(X, c=None):
    n, p = X.shape
    dims = range(1, p+1)
    for obs in X:
        plt.plot(dims, obs, c=c)

from sklearn import datasets
iris = datasets.load_iris()
X = iris.data
y = iris.target
X1 = X[y==1]
plt.figure(figsize=(10,3), dpi=200)
pcoord(X1, c='#aaaaaa')
md = hd.medoid(X1, axis=0)
gm = hd.geomedian(X1, axis=0)
xx = np.arange(X.shape[1])+1
plt.plot(xx, md, c='m', ls='--', lw=2, label='Medoid')
plt.plot(xx, gm, c='r', ls='-', lw=2, label='Geometric Median')
plt.xticks(xx, iris.feature_names)
plt.title('Iris data set (' + iris.target_names[1].title() + ' class)')
plt.grid(color='k', ls=':', axis='x')
plt.legend(framealpha=1.0)
plt.savefig('docs/fig1.svg')


# n, p = (40, 20)
# loc1 = np.random.normal(1, 2.0, size=(p,))
# loc2 = loc1 + np.random.normal(1.0, 1.0, size=(p,))
# sd = np.random.uniform(0.1, 0.2, size=(p,))
# X1 = np.random.normal(loc=loc1, scale=sd, size=(n, p))
# X2 = np.random.normal(loc=loc2, scale=sd, size=(n, p))
# X = np.vstack([X1,X2])

# plt.figure(figsize=(8,4))
# pcoord(X2, c='#aaaaaa')
# md = hd.medoid(X2, axis=0)
# gm = hd.geomedian(X2, axis=0)
# plt.plot(range(1, X2.shape[1]+1), md, c='m', ls='--', lw=2)
# plt.plot(range(1, X2.shape[1]+1), gm, c='r', ls='--', lw=2)
# plt.savefig('docs/fig1.png')

# plt.figure(figsize=(8,4))
# pcoord(X1, c='#aaaaaa')
# pcoord(X2, c='#555555')
# m = hd.geomedian(X, axis=0)
# plt.plot(range(1, 7), m, c='m')
# plt.savefig('docs/fig2.png')
