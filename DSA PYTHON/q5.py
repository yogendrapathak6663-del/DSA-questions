def calculate_tyres():
    n = int(input())
    for i in range(n):
        cars, bikes = map(int, input().split())
        tyres = cars * 4 + bikes * 2
        print(tyres)

calculate_tyres()
# Input: 3\n4 2\n4 0\n1 2 → Output: 20\n16\n8
