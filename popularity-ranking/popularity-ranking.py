def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    # Write code here
    pop_rank = []
    for item in items:
        fact_1 = (item[1]* item[0] / (item[1]+min_votes)) 
        fact_2 = (min_votes* global_mean / (item[1]+min_votes)) 
        pop_rank.append(fact_1+fact_2)

    return pop_rank
        

    