L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

def sup_doublons(L):
    n_list = []
    for i in L:
        if not any(x == i for x in n_list):
            n_list = n_list + [i]
    return n_list
print(sup_doublons(L))