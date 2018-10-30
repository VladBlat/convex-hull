import numpy as np

def polar_angle(prev_end_point: np.ndarray, end_point: np.ndarray, new_point: np.ndarray) -> float:
    import math

    convex_hull_edge = prev_end_point - end_point
    new_edge = new_point - end_point

    return (2 * math.pi) - math.acos(np.dot(convex_hull_edge, new_edge)
                     / (np.linalg.norm(convex_hull_edge) * np.linalg.norm(new_edge)))
