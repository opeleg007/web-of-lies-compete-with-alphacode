# Step 1: Read input line args
# Step 2: Define and initialize the data structures
# Step 3: Run Queries

class QueryList:
    def __init__(self):
        pass


class NobleNode:
    def __init__(self):
        pass

    def is_vulnerable(self):
        pass


class NobleLinkedList:
    def __init__(self):
        pass

    def add_friendship(self, u: NobleNode, v: NobleNode):
        pass

    def remove_friendship(self, u: NobleNode, v:NobleNode):
        pass

    def game_of_thrones(self):
        pass


def read_input_line_args():
    return n, m, friendships, queries


def init_data_structures(n:int, m:int, frienships:list[tuple], queries:list[tuple]):
    return noble_linked_list, queries


if __name__ == '__main__':
    n, m, friendships, queries = read_input_line_args()
    noble_linked_list, queries = init_data_structures(n, m, friendships, queries)
