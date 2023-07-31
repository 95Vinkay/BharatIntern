import textdistance

def autocorrect(word, dictionary):
    corrected_word = word
    min_distance = float('inf')

    for entry in dictionary:
        distance = textdistance.levenshtein.normalized_distance(word, entry)
        if distance < min_distance:
            corrected_word = entry
            min_distance = distance

    return corrected_word


# Example
word = "phne"
dictionary = ["phone", "correct", "word", "autocorrect"]
corrected_word = autocorrect(word, dictionary)
print(f"Autocorrected: {corrected_word}")