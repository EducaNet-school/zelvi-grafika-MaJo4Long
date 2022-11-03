from string import ascii_letters


def counting_letters(text):
    dictionary = {}
    for i in text:
        if i in ascii_letters:
            dictionary[i] = text.count(i)
    return dictionary


textconvert = input("Write something to count your words: ")

text = textconvert.lower()

print(counting_letters(text))
