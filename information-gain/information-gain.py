import numpy as np

def _entropy(y):
    """
    Helper: Compute Shannon entropy (base 2) for labels y.
    """
    y = np.asarray(y)
    if y.size == 0:
        return 0.0
    vals, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum()) if p.size else 0.0

def information_gain(y, split_mask):
    """
    Compute Information Gain of a binary split on labels y.
    Use the _entropy() helper above.
    """
    # Write code here
    ent = _entropy(y)

    y_left = []
    y_right = []
    for i in range(len(split_mask)):
        if split_mask[i]:
            y_left.append(y[i])
        else:
            y_right.append(y[i])

    ent_left = _entropy(y_left)
    ent_right = _entropy(y_right)

    p_left = len(y_left) / len(y)
    p_right = len(y_right) / len(y)

    info_gain = ent - (p_left*ent_left) - (p_right*ent_right)
    
    return info_gain