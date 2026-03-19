def get_season(month):
    if month < 1 or month > 12:
        return "Invalid Month Entered"
    
    if 3 <= month <= 5:
        return "Spring Season"
    elif 6 <= month <= 8:
        return "Summer Season"
    elif 9 <= month <= 11:
        return "Autumn Season"
    else:
        return "Winter Season"
