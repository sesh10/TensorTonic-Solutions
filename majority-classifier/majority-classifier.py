import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    classItem, counts = np.unique(y_train, return_counts=True)
    majority_class = classItem[np.argmax(counts)]
    
    ans = np.full(len(X_test), majority_class)
    return ans