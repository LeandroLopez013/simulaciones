import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from s_order import solve_2nd_order_ivp

m1 = 1
m2 = 1
l1 = 3
l2 = 3
g = 9.81

v10 = -2
v20 = 3
T10 = np.pi/4
T20 = 1.2*np.pi/4

t1 = 50

def double_pend_rhs(t, T1, T2, T1p, T2p):
    alpha = m2/(m1+m2) * l2/l1
    beta = l1/l2
    dt = T1 - T2

    R1 = -alpha * T2p**2 * np.sin(dt) - g/l1 * np.sin(T1)
    R2 = beta * T1p**2 * np.sin(dt) - g/l2 * np.sin(T2)
    D = 1 - alpha * beta * np.cos(dt)**2

    return [
        (R1 - alpha * R2 * np.cos(dt))/D,
        (R2 - beta * R1 * np.cos(dt))/D,
    ]


t_values, y_values = solve_2nd_order_ivp(
    func=double_pend_rhs,
    y0 = [T10, T20],
    yp0 = [v10, v20],
    t0=0,
    t1=t1,
    dt=1e-2
)

y_values = y_values.T

theta1 = y_values[0]
theta2 = y_values[1]

x1 = l1 * np.sin(theta1)
y1 = -l1 * np.cos(theta1)

x2 = x1 + l2 * np.sin(theta2)
y2 = y1 - l2 * np.cos(theta2)

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-6, 5)

line1, = ax.plot([], [], 'b-', linewidth=1)   # rastro
point1, = ax.plot([], [], 'ro', markersize=10)

line2, = ax.plot([], [], 'y-', linewidth=1)   # rastro
point2, = ax.plot([], [], 'go', markersize=10)

def init():
    point1.set_data([], [])
    point2.set_data([], [])
    return point1, point2,

def update(frame):
    point1.set_data([x1[frame]], [y1[frame]])
    line1.set_data([0, x1[frame]], [0, y1[frame]])
    point2.set_data([x2[frame]], [y2[frame]])
    line2.set_data([x1[frame], x2[frame]], [y1[frame], y2[frame]])
    return line1, point1, line2, point2


ani = FuncAnimation(fig, update, frames=5000,
                               init_func=init, interval=1, blit=True,
                               repeat=False)
plt.show()