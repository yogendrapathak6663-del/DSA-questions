def length_of_longest_substring(s):
    char_set = set()
    left = right = 0
    max_length = 0
    
    while right < len(s):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
        right += 1
    
    return max_length
