import numpy as np


def dh_transform(a, alpha, d, theta):
    return np.array(
        [
            [
                np.cos(theta),
                -np.sin(theta) * np.cos(alpha),
                np.sin(theta) * np.sin(alpha),
                a * np.cos(theta),
            ],
            [
                np.sin(theta),
                np.cos(theta) * np.cos(alpha),
                -np.cos(theta) * np.sin(alpha),
                a * np.sin(theta),
            ],
            [0, np.sin(alpha), np.cos(alpha), d],
            [0, 0, 0, 1],
        ]
    )


def forward_kinematics(joint_angles, robot_params_a, robot_params_d):
    joint_angles = np.radians(joint_angles)
    dh_params = [
        [0, np.pi / 2, robot_params_d[0], joint_angles[0]],
        [robot_params_a[1], 0, 0, joint_angles[1]],
        [robot_params_a[3], 0, 0, joint_angles[2]],
        [0, np.pi / 2, robot_params_d[3], joint_angles[3]],
        [0, -np.pi / 2, 0, joint_angles[4]],
        [0, 0, robot_params_d[5], joint_angles[5]],
    ]

    T = np.eye(4)
    for param in dh_params:
        T = np.dot(T, dh_transform(*param))

    return T
