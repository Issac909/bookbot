def word_count(text):
    count = 0

    count = text.split()

    return len(count)

def character_count(text):
    characters = {}

    for character in text.lower():
        if character in characters:
            characters[character] += 1

        else:
            characters[character] = 1

    return characters

def sorted_dictionary(dictionary):
    sorted_list = []

    for char in dictionary:
        sorted_list.append({"char": char, "num": dictionary[char]})

    sorted_list.sort(reverse=True, key=lambda char: char["num"])

    return sorted_list
