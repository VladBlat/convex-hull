import numpy as np

def polar_angle(prev_end_point: np.ndarray, end_point: np.ndarray, new_point: np.ndarray) -> float:
    import math

    # if new_point[1] == end_point[1]:
    #     return math.pi
    # elif new_point[1] > end_point[1]:
    #     return math.acos(np.dot(np.array([1, 0]), new_point - end_point)
    #                      / (np.linalg.norm(np.array([1, 0])) * np.linalg.norm(new_point - end_point)))
    # elif new_point[1] < end_point[1]:
    #     return math.pi + math.acos(np.dot(np.array([-1, 0]), new_point - end_point)
    #                      / (np.linalg.norm(np.array([-1, 0])) * np.linalg.norm(new_point - end_point)))
    #

    convex_hull_edge = prev_end_point - end_point
    new_edge = new_point - end_point

    return (2 * math.pi) - math.acos(np.dot(convex_hull_edge, new_edge)
                     / (np.linalg.norm(convex_hull_edge) * np.linalg.norm(new_edge)))
#
# from math import degrees
#
# print(degrees(polar_angle(np.array([6, 12]), np.array([2, 10]), np.array([3, 6]))))
