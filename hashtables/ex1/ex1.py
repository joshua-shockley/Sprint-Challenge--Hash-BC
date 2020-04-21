#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    """
    YOUR CODE HERE
    """
    # limit is the number in which is the weight request
    if length < 2:
        return None
    if length == 2:
        for item in weights:
            if sum(weights) == limit:
                answer = (1, 0)
                return answer

    else:
        for item in weights:
            print("item:", item)
            print("limit: ", limit)
            if item <= limit and item != "None":
                index = weights.index(item)
                hash_table_insert(ht, item, index)
                print(f"index: {index}, item in weights: {item}")
                # print(
                #     f"key: {ht.storage[item[0]]}")
                for item2 in weights:
                    if weights.index(item2) != weights.index(item) and limit - item == item2:

                        index2 = weights.index(limit-item)
                        if index > index2:
                            bigger = index
                            smaller = index2
                        else:
                            bigger = index2
                            smaller = index
                        answer = (bigger, smaller)
                        print(answer)
                        return answer


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
