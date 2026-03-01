import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-5, 5)

line, = ax.plot([], [], 'b-', linewidth=1)   # rastro
point, = ax.plot([], [], 'ro', markersize=10)

dt = 1e-1
t1 = 10
amount = int(t1/dt)
k = 1
m = 1
y = 1
a = 0
v = 0

x_data, y_data = [], []

def init():
    point.set_data([0], [y])
    return point,

def update(frame):
    global y, v
    x_val = frame * dt
    a = -k/m * y
    v += a*dt
    y += v*dt

    x_data.append(x_val)
    y_data.append(y)

    line.set_data(x_data, y_data)
    point.set_data([x_val], [y])
    return line, point,

ani = FuncAnimation(fig, update, frames=amount,
                               init_func=init, interval=30, blit=True,
                               repeat=False)
plt.show()