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

def char_dict_to_sorted_list(dict):
    sorted_list = []
    for char,num in dict.items():
        sorted_list.append({"char":char ,"num": num})
    sorted_list.sort(reverse = True, key = lambda dict: dict["num"])
    return sorted_list


    