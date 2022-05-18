import random
def comp_move(j, n):
    '''Computes the computers turn'''
    random.shuffle(j)
    result = []
    for i in range(0, len(j), n):
        result.append(j[i:i + n])
    return result

jam = [1,2,3,4,5,6,7,8,9]
print(comp_move(jam,1))

