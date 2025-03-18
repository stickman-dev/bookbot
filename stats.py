def get_book_words(text):
    words = text.split()
    return len(words)

def get_book_char(text):
    char_count = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_count:
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1
    return char_count

def sort_list(char_count):
    def sort_on(dict):
        return dict["count"]
    sorted_list = []
    for key, value in char_count.items():
        sorted_list.append({"char": key, "count": value})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list