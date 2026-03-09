import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    # Write code here
    predictions = np.asarray(predictions)
    
    n_samples = predictions.shape[1]
    votes = []
    
    for i in range(n_samples):
        counts = np.bincount(predictions[:, i])
        votes.append(np.argmax(counts))
    
    return votes