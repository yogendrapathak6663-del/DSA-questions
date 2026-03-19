def pythagorean_triplets(limit):
    triplets = []
    for a in range(1, limit):
        for b in range(a, limit):
            c = (a**2 + b**2)**0.5
            if c.is_integer() and c < limit:
                triplets.append((a, b, int(c)))
    return triplets

print(pythagorean_triplets(20))  # [(3,4,5), (5,12,13), (6,8,10), (8,15,17), (9,12,15), (12,16,20)]
