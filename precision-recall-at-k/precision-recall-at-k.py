def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    cnt = 0
    for i in range(k):
        if recommended[i] in relevant:
            cnt+=1

    prec = cnt / k
    rec = cnt / len(relevant)
    return [prec, rec]