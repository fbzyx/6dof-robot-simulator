import numpy as np


def dh_transform(a, alpha, d, theta):
    """
    Create the Denavit-Hartenberg transformation matrix.
    a: Link length
    alpha: Link twist
    d: Link offset
    theta: Joint angle
    """
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


def forward_kinematics(joint_angles):
    """
    Compute forward kinematics for a 6-DOF robot arm.
    joint_angles: List or array of 6 joint angles [θ1, θ2, ..., θ6] in radians
    Returns the overall 4x4 transformation matrix of the end effector.
    """

    joint_angles = np.radians(joint_angles)
    # Define DH parameters for each joint
    # Format: [a, alpha, d, theta]
    a2, a3 = 0.3, 0.3
    d1, d4, d6 = 0.2, 0.2, 0.1

    dh_params = [
        [0, np.pi / 2, d1, joint_angles[0]],
        [a2, 0, 0, joint_angles[1]],
        [a3, 0, 0, joint_angles[2]],
        [0, np.pi / 2, d4, joint_angles[3]],
        [0, -np.pi / 2, 0, joint_angles[4]],
        [0, 0, d6, joint_angles[5]],
    ]

    # Multiply all transformation matrices
    T = np.eye(4)
    for param in dh_params:
        T = np.dot(T, dh_transform(*param))

    return T
