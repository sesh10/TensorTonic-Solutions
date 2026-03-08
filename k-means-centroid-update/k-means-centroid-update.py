import numpy as np

def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    # Write code here
    points = np.array(points)
    dim = points.shape[1]
    centroids = []

    for i in range(k):
        cluster_points = points[np.array(assignments) == i]

        if len(cluster_points) == 0:
            centroids.append([0.0] * dim)
        else:
            mean_point = np.mean(cluster_points, axis=0)
            centroids.append(mean_point.tolist())

    return centroids