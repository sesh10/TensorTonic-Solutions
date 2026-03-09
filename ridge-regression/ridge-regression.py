import numpy as np

def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)
    term1 = X.T @ X
    term2 = lam * np.identity(X.shape[1], dtype=float)
    term3 = X.T @ y

    w = np.linalg.inv(term1 + term2) @ term3

    return w