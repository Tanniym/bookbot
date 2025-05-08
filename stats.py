
def words_in_book(text):
    words = text.split()
    wordcount = len(words)
    return wordcount


def chars_in_book(text):
    text = text.lower()

    result = {}
    for c in set(text):
        result[c] = text.count(c)

    return result


def sort_on(dict):
    dict = list(dict.values())
    return dict[0]


def sort_chars(input_data):
    input_data = input_data.items()
    result = []

    for item in input_data:
        result.append({item[0]: item[1]})
    
    result.sort(reverse=True, key=sort_on)

    return result