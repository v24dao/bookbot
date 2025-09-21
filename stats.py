def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    counts = {}
    for char in text:
        lowered = char.lower()
        if lowered not in counts:
            counts[lowered] = 0
        counts[lowered] += 1
    return counts