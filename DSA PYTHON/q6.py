def min_discount_item():
    n = int(input())
    min_disc = float('inf')
    min_item = ""
    
    for _ in range(n):
        item, price, disc = input().split(',')
        price, disc = int(price), int(disc)
        discount_amount = (disc * price) / 100
        
        if discount_amount < min_disc:
            min_disc = discount_amount
            min_item = item
    
    print(min_item)

min_discount_item()
