def read_adjacency_list(path):
    with open(path, mode='r') as file:
        adjacency_list = [line.strip().split('\t') for line in file]
    return adjacency_list
