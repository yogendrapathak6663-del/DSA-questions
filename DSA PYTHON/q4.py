def solve_equation(a, b):
    return a**3 + a**2*b + 2*a**2*b + 2*a*b**2 + a*b**2 + b**3

a, b = map(int, input().split())
print(solve_equation(a, b))
