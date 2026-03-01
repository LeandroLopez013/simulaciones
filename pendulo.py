import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from s_order import solve_2nd_order_ivp

m = 2
l = 3
g = 9.81
gamma = 1.5

T0 = np.pi/4
TP0 = 0

def pend_func(t, T, TP):
    return -g/l * np.sin(T) - gamma/(m*l**2) * TP


t_values, y_values = solve_2nd_order_ivp(
    func=pend_func,
    y0=T0,
    yp0=TP0,
    t0=0,
    t1=10,
    dt=1e-2
)

y_values = y_values.T

theta = y_values[1]

x = l * np.sin(theta)
y = -l * np.cos(theta)

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

line, = ax.plot([], [], 'b-', linewidth=1)   # rastro
point, = ax.plot([], [], 'ro', markersize=10)

def init():
    point.set_data([], [])
    return point,

def update(frame):
    point.set_data([x[frame]], [y[frame]])
    line.set_data([0, x[frame]], [0, y[frame]])
    return line, point,


ani = FuncAnimation(fig, update, frames=1000,
                               init_func=init, interval=5, blit=True,
                               repeat=False)
plt.show()