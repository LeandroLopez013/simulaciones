import numpy as np
from typing import Iterable


def solve_ivp_euler(func, dt, t0, t1, y0, **kwargs):
    if isinstance(y0, Iterable):
        y0 = np.array(y0)
        func_ = lambda t, ys: np.array(object=func(t, *ys))
    else:
        func_ = func
    t_values = np.arange(t0, stop=t1 , step=dt)
    y_values = [y0]
    y_curr = y0

    for t in t_values:
        y_next = y_curr + dt*func_(t, y_curr)
        y_values.append(y_next)
        y_curr = y_next
    
    return t_values, np.array(y_values)