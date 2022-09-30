def find_farthest_orbit(tup):
    pi = 3.14
    list1 = []
    result = ()
    for i in tup:
        a, b = i
        if a != b:
            list1.append(a)
            list1.append(b)
    max_s = max([pi * list1[i] * list1[i + 1] for i in range(0, len(list1), 2)])
    for i in range(0, len(list1), 2):
        if pi * list1[i] * list1[i + 1] == max_s:
            result = list1[i], list1[i + 1]
    return result


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
