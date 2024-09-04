"""
Create a program to count the number of occurrences of a word within a song lyrics. 
Use as an example the file Exercise9.1.txt, which contains the lyrics of Kylie Minogue’s song 
“I Should Be So Lucky” (1988). 
The program must receive a word from the user and must calculate its number of occurrences, 
writing the result on the screen. For instance, if the user wants to count the number of occurrences 
of the word ‘Lucky’, the program must show on the screen:

The word LUCKY is repeated 53 times

Remember to match uppercase and lowercase letters to make a correct count 
(e.g.: if you want to count the number of occurrences of ‘lucky’, words such as ‘Lucky’, ‘LUCKY’ etc. 
must also be counted).
"""

file_path = "17_lesson/file.txt"
user_word = input("Enter the word to count in the lyrics: ")

# 'r' for read
with open(file_path, 'r') as file:
    # prevrushtame vsichki dumi vuv fail-a v lowercase
    content = file.read().lower()
    # prevrushtame dumata na user-a sushto v lowercase
    user_word = user_word.lower()
    occurrences = content.count(user_word)
    print(f"The word {user_word} is repeated {occurrences} times.")
