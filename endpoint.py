import numpy as np

# function that find 1st point of convex hull
def endpoint(points: np.ndarray) -> np.ndarray:
#     find all points with lowes y
    idxs_of_minimal_y = np.argwhere(points == np.min(points))[:,0]
    points_with_min_y = np.array([points[idx] for idx in idxs_of_minimal_y])
#     select from end_point_try point with max x
    idx_of_endpoint = np.argmax(points_with_min_y, axis=0)[0]

    return points_with_min_y[idx_of_endpoint]
