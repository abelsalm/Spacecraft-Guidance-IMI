import numpy as np

# constants
n = 2 * np.pi / (24 * 60 * 60)  # Earth angular's velocity (rad/s)
m = 3000  # mass (kg)
dt = 20 * 60  # dt in seconds
total_time = 7 * 24 * 60 * 60  # total time of one week in seconds
num_steps = int(total_time / dt)  # iterations


# function to calculate the next state, necassary for gymnasium step function
def next_state(t, s, control, dt):
    x, y, z, x_dot, y_dot, z_dot, q1, q2, q3, q4, w1, w2, w3 = s

    Fx, Fy, Fz, Lx, Ly, Lz = control(t)

    x_ddot = 3 * n**2 * x + 2 * n * y_dot + Fx / m
    y_ddot = -2 * n * x_dot + Fy / m
    z_ddot = -n**2 * z + Fz / m

    # flake8: noqa
    s_dot = np.array([x_dot, y_dot, z_dot, x_ddot, y_ddot, z_ddot, 0, 0, 0, 0, 0, 0, 0])

    return s + dt * s_dot
