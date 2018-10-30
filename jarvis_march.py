import numpy as np

# gift wrapping algorithm
def jarvis(points: np.ndarray) -> np.ndarray:
    # find 1st point of convex hull
    # this point has lowest y & biggest x, if their many
    from endpoint import endpoint

    convex_hull = [endpoint(points)]
    # point for start vector
    convex_hull.insert(0, convex_hull[0] - np.array([-1, 0]))

    # k - idx of 1st non added point
    k = 0
    while True:
        # take 1st nonadded point as endpoint
        new = points[k]
        idx = None #  this idx needed for swap array elements

        from polar import polar_angle

        for i in range(k+1, points.shape[0]):
            # if polar angle of i-point below new polar angle -> new = point[i]
            if polar_angle(convex_hull[-2], convex_hull[-1], points[i])\
                    < polar_angle(convex_hull[-2], convex_hull[-1], new):
                new, idx = points[i], i
            # if polar angle of i-point equal new polar angle
            elif polar_angle(convex_hull[-2], convex_hull[-1], points[i])\
                    == polar_angle(convex_hull[-2], convex_hull[-1], new):
                # if i-point is farther then new -> new = point[i]
                if np.linalg.norm(points[i] - convex_hull[-1]) > np.linalg.norm(new - convex_hull[-1]):
                    new, idx = points[i], i

        # if founded ponint is not start point
        if not np.array_equal(new, convex_hull[1]):
            # add point to convex hull & swap points in array for points[k] = new & k++
            convex_hull.append(np.copy(new))
            points[[k, idx]] = points[[idx, k]]
            k += 1
        else:
            convex_hull.append(np.copy(new))
            break

    convex_hull.pop(0)
    return np.array(convex_hull)