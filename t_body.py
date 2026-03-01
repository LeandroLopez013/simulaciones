import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from s_order import solve_2nd_order_ivp

t1 = 60
m1 = 1
m2 = 1
m3 = 1
G = 1

def dist(r1, r2):
    return np.linalg.norm(r1-r2)

f1 = lambda r1, r2, r3: -G * m2 * (r1-r2)/dist(r1, r2)**3 - G * m3 * (r1-r3)/dist(r1, r3)**3

f2 = lambda r1, r2, r3: -G * m1 * (r2-r1)/dist(r2, r1)**3 - G * m3 * (r2-r3)/dist(r2, r3)**3

f3 = lambda r1, r2, r3: -G * m1 * (r3-r1)/dist(r3, r1)**3 - G * m2 * (r3-r2)/dist(r3, r2)**3

def three_body_func(t, r1x , r1y , r2x , r2y , r3x , r3y, r1px, r1py, r2px, r2py, r3px, r3py):
    r1 = np.array([r1x, r1y])
    r2 = np.array([r2x, r2y])
    r3 = np.array([r3x, r3y])

    return [
        *f1(r1, r2, r3),
        *f2(r1, r2, r3),
        *f3(r1, r2, r3)
    ]


y0 = [
    1, 0,
    -1, 0,
    0, 1
]
yp0 = [
    1, 1,
    0, 1,
    1, 0
]


t_values, y_values = solve_2nd_order_ivp(
    func=three_body_func,
    y0=y0,
    yp0=yp0,
    t0=0,
    t1=t1,
    dt=1e-2
)

y_values = y_values.T

x1 = y_values[0]
y1 = y_values[1]

x2 = y_values[2]
y2 = y_values[3]

x3 = y_values[4]
y3 = y_values[5]

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

line1, = ax.plot([], [], 'r-', linewidth=1)   # rastro
point1, = ax.plot([], [], 'ro', markersize=10)

line2, = ax.plot([], [], 'g-', linewidth=1)   # rastro
point2, = ax.plot([], [], 'go', markersize=10)

line3, = ax.plot([], [], 'b-', linewidth=1)   # rastro
point3, = ax.plot([], [], 'bo', markersize=10)

def init():
    point1.set_data([], [])
    point2.set_data([], [])
    point3.set_data([], [])
    return point1, point2, point3,

def update(frame):
    point1.set_data([x1[frame]], [y1[frame]])
    line1.set_data(x1[:frame], y1[:frame])
    point2.set_data([x2[frame]], [y2[frame]])
    line2.set_data(x2[:frame], y2[:frame])
    point3.set_data([x3[frame]], [y3[frame]])
    line3.set_data(x3[:frame], y3[:frame])
    return line1, point1, line2, point2, line3, point3


ani = FuncAnimation(fig, update, frames=5000,
                               init_func=init, interval=1, blit=True,
                               repeat=False)
plt.show()