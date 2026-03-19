def counting_valleys(path):
    level = 0
    valleys = 0
    
    for step in path:
        if step == 'U':
            level += 1
        else:
            level -= 1
        
        if level == 0 and step == 'U':
            valleys += 1
    
    return valleys
