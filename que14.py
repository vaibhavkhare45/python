english_to_hindi = {
    "apple": "सेब",
    "banana": "केला",
    "cat": "बिल्ली",
    "dog": "कुत्ता",
}
def lookup(word):
    if word in english_to_hindi:
        return english_to_hindi[word]
    else:
        return "Translation not found"

print(lookup("cat"))
