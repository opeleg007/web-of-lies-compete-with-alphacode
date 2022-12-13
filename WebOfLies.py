# Step 1: Read input line args
# Step 2: Define and initialize the data structures
# Step 3: Run Queries
import copy


class NobleNode:
    power: int
    friends: list
    friend_count: int
    weakest_friend: int

    def __init__(self, power, n):
        self.power = power
        self.friends = [None for _ in range(n)]
        self.weakest_friend = 0
        self.friend_count = 0

    def add_friend(self, friend):
        self.friends[friend] = 1
        self.friend_count += 1

    def remove_friend(self, friend):
        self.friends[friend] = None
        self.friend_count -= 1

    def update_weakest(self):
        if self.friend_count == 0:
            self.weakest_friend = -1
        else:
            for i in range(0, len(self.friends)):
                if self.friends[i] == 1:
                    self.weakest_friend = i
                    break

    def is_vulnerable(self):
        if self.friend_count > 0 and self.weakest_friend >= self.power:
            return True
        return False


class NobleLinkedList:
    nobles: [NobleNode]

    def __init__(self, n: int, m: int, friendships: [()]):
        self.nobles = [NobleNode(i, n) for i in range(n)]
        self.init_friendships(friendships)

    def init_friendships(self, friendships: [()]):
        for friendship in friendships:
            u, v = friendship
            self.add_friendship(u - 1, v - 1)

    def add_friendship(self, u: NobleNode, v: NobleNode):
        self.nobles[u].add_friend(v)
        self.nobles[v].add_friend(u)

    def remove_friendship(self, u: NobleNode, v:NobleNode):
        self.nobles[u].remove_friend(v)
        self.nobles[v].remove_friend(u)

    def update_weakest_for_all(self):
        for noble in self.nobles:
            if noble is not None:
                noble.update_weakest()

    def kill_noble(self, noble: int):
        for friend_ind in range(len(self.nobles)):
            friend = self.nobles[noble].friends[friend_ind]
            if friend is not None:
                self.remove_friendship(friend_ind, noble)
        self.nobles[noble] = None

    def game_of_thrones(self):
        self.update_weakest_for_all()
        count_kills = 0
        # for noble in self.nobles:
            # if noble is not None:
                # print(f'noble {noble.power}')
                # print('-------------------')
                # print(f'friends: {noble.friends}')
                # print(f'weakest friend: {noble.weakest_friend}')
                # print(f'vulnerable? {noble.is_vulnerable()}')
                # print('-------------------')
        for noble in self.nobles:
            if noble is not None and noble.is_vulnerable():
                self.kill_noble(noble.power)
                count_kills += 1
                # print('-------------------')
                # print(f'End of round: {count_kills} nobles killed')
                # print('-------------------')
        self.update_weakest_for_all()
        if count_kills == 0:
            print(f'Game Over, {len([i for i in self.nobles if i is not None])} nobles have won the game')
            return
        else:
            self.game_of_thrones()


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


def init_data_structure(n:int, m:int, friendships:list[tuple]):
    noble_linked_list = NobleLinkedList(n, m, friendships)
    return noble_linked_list


def main():
    file_path = "input.txt"
    n, m, friendships, queries = read_input_line_args(file_path)
    noble_linked_list = init_data_structure(n, m, friendships)
    for query in queries:
        if len(query) == 1 and query[0] == 3:
            copy_of_noble_linked_list = copy.deepcopy(noble_linked_list)
            print("-------------------")
            print("Lest Play The Game Of Thrones")
            print("-------------------")
            copy_of_noble_linked_list.game_of_thrones()
        else:
            operation, u, v = query
            if operation == 1:
                noble_linked_list.add_friendship(u - 1, v - 1)
            else:
                noble_linked_list.remove_friendship(u - 1, v - 1)
    return


if __name__ == '__main__':
    main()
    pass
