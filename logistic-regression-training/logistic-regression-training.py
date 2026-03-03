import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    N, D = X.shape
    
    w = np.zeros(D)
    b = 0.0

    for _ in range(steps):
        z = X @ w + b            
        y_hat = _sigmoid(z)        

        loss = -np.mean(
            y * np.log(y_hat) +
            (1 - y) * np.log(1 - y_hat)
        )

        # weight = weight - (learning rate) * (slope of loss func)
        error = y_hat - y          # shape (N,)
        dw = (X.T @ error) / N     # shape (D,)
        db = np.sum(error) / N     # scalar
        
        # Update
        w -= lr * dw
        b -= lr * db

    return w, float(b)

        
    