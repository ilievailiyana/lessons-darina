# String - tretirai go kato list
word = "HELLo"

for character in word:
    print(character)

print("Kolko simvola ima v dumata:", len(word))

vowel_count = 0
for char in word:
    # character.lower() - pravi go na malka bukva ako e bila golqma
    if char.lower() in "aeiou":
        vowel_count = vowel_count + 1
print(f"{word} has {vowel_count} vowels.")

# za da prevurnem character v golqma bukva:
character = 'a'
print(character.upper())

print(word[0])
print(word[-1])

if word[0].isupper():
    print("ITS UPPER", word[0])

if word[-1].islower():
    print("ITS LOWER", word[-1])