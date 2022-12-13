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


def unpack_queries_from_line_args(all_queries: list):
    queries = []
    for query in all_queries:
        pack = []
        for literal in query:
            pack += [int(literal[0])]
        queries.append(pack)
    return queries


def read_input_line_args(file_path: str):
    f = open(file_path, "r")
    n, m = map(lambda x: int(x), f.readline().split(' '))
    all_uv = [map(lambda x: int(x), f.readline().split(' ')) for _ in range(m)]
    friendships = [(u, v) for u, v in all_uv]
    query_amount = int(f.readline())
    all_queries = [f.readline().split(' ') for _ in range(query_amount)]
    queries = unpack_queries_from_line_args(all_queries)
    f.close()
    return n, m, friendships, queries


def init_data_structures(n:int, m:int, frienships:list[tuple], queries:list[tuple]):
    return #noble_linked_list, queries


def main():
    file_path = "input.txt"
    n, m, friendships, queries = read_input_line_args(file_path)
    noble_linked_list, queries = init_data_structures(n, m, friendships, queries)


if __name__ == '__main__':
    main()
