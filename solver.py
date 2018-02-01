import pickle
with open('words.pickle', 'rb') as f:
    dict = pickle.load(f)
    
def sort_letters(a):
    return "".join(sorted(list(a)))


def solver(a):
    sorted_a = sort_letters(a)
    if sorted_a in dict:
        return dict[sorted_a]
    else:
        return None