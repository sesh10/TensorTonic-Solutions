import numpy as np

def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here
    assign_clusters = []
    for i in range(len(points)):
        ind = -1
        ans = 1e9
        for j in range(len(centroids)):
            eucl_dist = np.sum((np.array(points[i]) - np.array(centroids[j])) ** 2)
            if eucl_dist < ans:
                ans = eucl_dist
                ind = j
        assign_clusters.append(ind)

    return assign_clusters