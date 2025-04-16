from .dh import forward_kinematics
import numpy as np


def lerp(start, end, t):
    return start + (end - start) * t


def interpolate_joints(start_angles, end_angles, steps=100):
    start = np.array(start_angles)
    end = np.array(end_angles)
    trajectory = [lerp(start, end, t) for t in np.linspace(0, 1, steps)]
    return trajectory


def get_interpolated_matrix_data(start_angles_deg, end_angles_deg):
    interpolated_data = []
    start_angles_rad = np.radians(start_angles_deg)
    end_angles_rad = np.radians(end_angles_deg)

    trajectory = interpolate_joints(start_angles_rad, end_angles_rad, steps=20)

    for i, angles in enumerate(trajectory):
        T = forward_kinematics(angles)
        interpolated_data.append(T.tolist())

    return interpolated_data


# start_angles_deg = [0, 0, 0, 0, 0, 0]
# end_angles_deg = [30, 45, -30, 60, -45, 90]
# get_interpolated_matrix_data(start_angles_deg, end_angles_deg)
