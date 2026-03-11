import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here

    ans = [a if a > 0 else alpha * a for a in x]
    return np.array(ans)