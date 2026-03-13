import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x = np.asarray(x)
    sigm = 1 / (1 + np.exp(-x))
    return x*sigm