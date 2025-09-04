def split_text(text):
    return text.split()

def word_count(text_array):
    return len(text_array)

def get_word_count(text):
    text_array = split_text(text)
    return word_count(text_array)



def count_characters(text):
    characters = {}
    for char in text:
        lower=char.lower()
        if lower in characters:
            characters[lower] += 1
        else:
            characters[lower] = 1
    return characters

def sort_on(items):
    return items["num"]

def character_sorted(char_dict):
    dict_list = []
    for char in char_dict:
        dict_list.append({"char":char, "num":char_dict[char]})
    dict_list.sort(reverse=True, key=sort_on) 
    return dict_list
