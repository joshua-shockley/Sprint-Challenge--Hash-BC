#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    """
    YOUR CODE HEREs

    first need to work with the tickets list of Ticket objects and find the first one
    --first one will have the source attribute == "NONE"

    --the next one will have the source attribute == to the previous tickets.destination

    -- that will continue until the very last one has a destination of "NONE"
    """
    for ob in tickets:
        hash_table_insert(hashtable, ob.source, ob.destination)
        # print(f"source: {ob.source}, destination: {ob.destination}\n")
    start = hash_table_retrieve(hashtable, "NONE")
    # print("start:", start)
    route[0] = start

    current = hash_table_retrieve(hashtable, start)
    next = ''
    # print("current destination: ", current)
    index = 0
    while current != "NONE":
        # print("current", current)
        route[index + 1] = current
        next = hash_table_retrieve(hashtable, current)
        # print("next: ", next)
        current = next
        index += 1

    route = [i for i in route if i != None]
    print("printing route ", route)

    return route
