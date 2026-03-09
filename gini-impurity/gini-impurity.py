import numpy as np

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    # Write code here
    nl = len(y_left)
    nr = len(y_right)
    n = nl + nr

    if nl == 0 and nr == 0:
        return 0.0

    leftel, leftct = np.unique(y_left, return_counts=True)
    rightel, rightct = np.unique(y_right, return_counts=True)

    gini_left = 1
    gini_right = 1

    for i in range(len(leftel)):
        gini_left -= (leftct[i]/nl) ** 2
        
    for i in range(len(rightel)):
        gini_right -= (rightct[i]/nr) ** 2

    gini_split = (nl/n)*gini_left + (nr/n)*gini_right

    return gini_split
    