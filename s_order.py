import numpy as np
from euler import solve_ivp_euler
from typing import Iterable

def solve_2nd_order_ivp(func, y0, yp0, t0, t1, dt, **kwargs):
    if isinstance(y0, Iterable):
        dim = len(np.array(y0))
        reduced_func = lambda t, *vars: np.array(
            [*vars[dim:], *func(t, *vars)]
        )
    else:
        reduced_func = lambda t, y, yp: np.array(
            [yp, func(t, y, yp)]
        )
    reduced_y0 = np.array([y0, yp0]).flatten()

    t_values, y_values = solve_ivp_euler(
        func=reduced_func,
        dt=dt,
        t0=t0,
        t1=t1,
        y0=reduced_y0.tolist(),
        **kwargs
    )

    return t_values, y_values