import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    ans = 0.0
    cnt = {}
    for c in y:
        if c not in cnt:
            cnt[c] = 1
        else:
            cnt[c] += 1
            
    for p in cnt:
        prob = cnt[p]/len(y)
        if prob > 0:
            ans -= prob * np.log2(prob)
    return ans