import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x = np.sort(np.asarray(x))
    q = np.asarray(q)
    n = len(x)
    
    results = []
    
    for el in q:
        pos = (el / 100) * (n - 1)
        lower = int(np.floor(pos))
        upper = int(np.ceil(pos))
        
        if lower == upper:
            results.append(x[lower])
        else:
            weight = pos - lower
            value = x[lower] + (x[upper] - x[lower]) * weight
            results.append(value)
    
    return np.array(results, dtype=float)