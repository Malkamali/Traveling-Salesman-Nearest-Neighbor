from math import sqrt

with open('test.txt', 'r') as reader:
    W = [x for x in reader.readline()]
    file = reader.read().split('\n')
    v = []
    for f in file:
        temp = f.split(' ')
        v.append((float(temp[1]), float(temp[2])))
for i in v:
    print(i)


def distance(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


def empty(lis):
    if not lis:
        return True
    else:
        return False


def tsp(v):
    first_city = v[0]
    current_city = first_city
    cost = 0
    del(v[0])
    while len(v) > 0:
        dist = 999999
        nxt_index = 999999
        for ii, city in enumerate(v):
            tmp_dist = distance(current_city, city)
            if tmp_dist < dist:
                dist = tmp_dist
                nxt_index = ii
        cost += dist
        current_city = v[nxt_index]
        del v[nxt_index]
    cost += distance(current_city, first_city)
    return cost


print(tsp(v))
