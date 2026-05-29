def is_anagram(s, t):
    if len(s) != len(t):
        return False

    char_count = {}

    for ch in s:
        char_count[ch] = char_count.get(ch, 0) + 1

    for ch in t:
        if ch not in char_count:
            return False

        char_count[ch] -= 1

        if char_count[ch] < 0:
            return False

    return True

# Example
print(is_anagram("listen", "silent"))