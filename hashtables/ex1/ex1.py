def get_indices_of_item_weights(weights, length, limit):

    weights_dict = {}

    for i in range(0, length):
        
        if limit - weights[i] in weights_dict:
            return [i, weights_dict[limit - weights[i]]]
        
        if weights[i] not in weights_dict:
            weights_dict[weights[i]] = i

    return None

    #If we store each weight's list index as its value, we can then check to see if the hash table contains an entry for limit - weight. If it does, then we've found the two items whose weights sum up to the limit!
    # set empty weights dict to store weights
    # for each item in the length of weghts, see if limit - item is in the weight dict
    # if weight dict is none 
