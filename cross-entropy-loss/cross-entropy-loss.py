import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    assert y_true.shape[0] == y_pred.shape[0], "y_true and y_pred must have matching shapes"
    n = len(y_pred)
    
    correct_probs = y_pred[np.arange(len(y_true)), y_true]
    loss = -np.mean(np.log(correct_probs))
    return loss    