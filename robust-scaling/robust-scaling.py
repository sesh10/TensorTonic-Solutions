import numpy as np

def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    # Write code here
    values = np.asarray(values)
    sorted_vals = np.sort(values)
    n = len(sorted_vals)

    if n == 1:
        return [0.0]
    
    med_val = np.median(sorted_vals)
    
    if n % 2 == 0:
        lower = sorted_vals[:n // 2]
        upper = sorted_vals[n // 2:]
    else:
        lower = sorted_vals[:n // 2]
        upper = sorted_vals[n // 2 + 1:]
    
    q1 = np.median(lower)
    q3 = np.median(upper)
    
    iqr = q3 - q1
    
    if iqr == 0:
        scaled = values - med_val
    else:
        scaled = (values - med_val) / iqr
    
    return scaled.tolist()