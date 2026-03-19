def move_hash_to_front(s):
    hashes = s.count('#')
    non_hashes = s.replace('#', '')
    return '#' * hashes + non_hashes
