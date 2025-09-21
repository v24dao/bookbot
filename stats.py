from collections import defaultdict

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    counts = defaultdict(int)
    for char in text:
        lowered = char.lower()
        counts[lowered] += 1
    return dict(counts)


