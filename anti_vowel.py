def anti_vowel(text):
    vowel_string= "AEIOUaeiou"

    for v in vowel_string:
        text= text.replace(v, "")

    return text

print(anti_vowel("Bart is a modern hero"))