import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-5, 5)

line1, = ax.plot([], [], 'r-', linewidth=1)   # rastro
point1, = ax.plot([], [], 'ro', markersize=10)

line2, = ax.plot([], [], 'b-', linewidth=1)   # rastro
point2, = ax.plot([], [], 'bo', markersize=10)

dt = 1e-1
t1 = 10
amount = int(t1/dt)
k= 1
m = 1
y1, y2 = 1, 0
a1, a2 = 0, 0
v1, v2 = 0, 0

x_data, y_data1, y_data2 = [], [], []

def init():
    point1.set_data([0], [y1])
    point2.set_data([0], [y2])
    return point1, point2,

def update(frame):
    global y1, y2, v1, v2
    x_val = frame * dt
    
    y1_old = y1
    y2_old = y2

    # aceleraciones
    a1 = (-2*(k/m)*y1_old + (k/m)*y2_old)
    a2 = ((k/m)*y1_old - 2*(k/m)*y2_old)

    # integrar
    v1 += a1 * dt
    v2 += a2 * dt

    y1 += v1 * dt
    y2 += v2 * dt

    x_data.append(x_val)
    y_data1.append(y1)
    
    y_data2.append(y2)

    line1.set_data(x_data, y_data1)
    point1.set_data([x_val], [y1])

    line2.set_data(x_data, y_data2)
    point2.set_data([x_val], [y2])

    return line1, point1 ,line2, point2,

ani = FuncAnimation(fig, update, frames=amount,
                               init_func=init, interval=30, blit=True,
                               repeat=False)
plt.show()