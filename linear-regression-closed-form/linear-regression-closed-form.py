import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)

    term1 = X.T @ X
    term2 = X.T @ y

    w = np.linalg.inv(term1) @ term2
    return np.array(w)