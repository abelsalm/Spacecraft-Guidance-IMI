import numpy as np

# constants
n = 2 * np.pi / (24 * 60 * 60)  # Earth angular's velocity (rad/s)
m = 3000  # mass (kg)
dt = 20 * 60  # dt in seconds
total_time = 7 * 24 * 60 * 60  # total time of one week in seconds
num_steps = total_time//dt  # iterations
R = 1.5  # radius of the chaser
H = 8  # height of the chaser
J = [[m * ((R ** 2) / 4 + (H ** 2) / 12), 0, 0], [0, m * ((R ** 2) / 4 + (H ** 2) / 12), 0], [0, 0, m * R ** 2 / 2]]  # inertia matrix
# we took it as the chaser is a cylinder, homogenous and full of mass


# discretized clohessy-wiltshire equations
def clohessy_wiltshire(r, v, dt, F):
    # finite differences
    ax = (v[0] - 2*n*v[1]) / dt + F[0] / m
    ay = (v[1] + 2*n*v[0]) / dt + F[1] / m
    az = (v[2] - n**2*r[1]) / dt + F[2] / m

    a = np.array([ax, ay, az])

    new_r = r + v*dt + 0.5*a*dt**2
    new_v = v + a*dt

    return np.array([new_r, new_v])


# discretize the evolution of q, the rotation quaternion
def next_q(q, dt):
    qx, qy, qz, qw = q
    Omega = np.array([[-qx, -qy, -qz], [qw, -qz, qy], [qz, qw, -qx], [-qy, qx, qw]])
    # finite differences
    q_dot = 0.5 * np.dot(Omega, q)
    new_q = q + q_dot*dt
    return new_q


# discretize the evolution of w, the angular speed of the chaser
def next_w(w, L, dt):
    # finite differences
    w_dot = np.dot(np.linalg.inv(J), L-np.dot(w, np.dot(J, w)))
    new_w = w + w_dot*dt
    return new_w
