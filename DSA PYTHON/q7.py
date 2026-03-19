def find_factors(n):
    n = abs(n)
    if n == 0:
        return "No Factors"
    
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(str(i))
    return ','.join(factors)

print(find_factors(54))  # 1,2,3,6,9,18,27,54
