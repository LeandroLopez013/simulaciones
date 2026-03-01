from euler import solve_ivp_euler
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib.colors import Normalize
from matplotlib import cm


dt = 1e-3
a = 10
b = 28
c = 8/3

r01 = [
    1.1,
    0,
    0
]

r02 = [
    1.3,
    1,
    -1
]


def lorenz_func(t, x, y, z):
    return [
        a * (y - x),
        x * (b - z) - y,
        x*y - c*z
    ]


t_values1, y_values1 = solve_ivp_euler(
    func=lorenz_func,
    dt=dt,
    t0=0,
    y0=r01,
    t1=100
)

t_values2, y_values2 = solve_ivp_euler(
    func=lorenz_func,
    dt=dt,
    t0=0,
    y0=r02,
    t1=100
)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

n = min(len(t_values1), len(y_values1))

x = y_values1[:n, 0]
y = y_values1[:n, 1]
z = y_values1[:n, 2]

x1 = y_values2[:n, 0]
y1 = y_values2[:n, 1]
z1 = y_values2[:n, 2]

ax.plot(x, y, z, color='royalblue', linewidth=2)
ax.plot(x1, y1, z1, color='red', linewidth=2)
ax.set_title('Hélice 3D')
plt.show()