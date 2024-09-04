"""
Create the Exercise11.7.py program in Python which defines the TextAnalysis class 
with the following characteristics:

in the constructor method:
    receives as a mandatory parameter the name of a txt file located in the same folder 
        as the code file (use Exercise11.7_text.txt as sample file)
    reads the document and saves it, divided into paragraphs, in the text attribute
    is equipped with methods that show on the screen, respectively, how many paragraphs, 
        words, characters, and punctuation marks the document is composed of. 
        Consider as punctuation marks, for simplicity, only: 
        comma, period, semicolon, colon, question and exclamation marks, 
        opening and closing round brackets

NB: to avoid problems in reading accented characters etc., add the argument encoding = 'utf-8' to the open() function.
"""

class TextAnalysis:
    # constructor
    def __init__(self, file_path):
        with open(file_path, 'r', encoding = 'utf-8') as file:
            self.text = file.read()
    
    # methods / functions
    def count_paragraphs(self):
        paragraphs = self.text.split('\n\n') # da razdelim teksta po novi redove i da go zapazim v paragrpahs promenlivata
        return len(paragraphs)
    
    def count_words(self):
        words = self.text.split()
        return len(words)
    
    def count_characters(self):
        return len(self.text)
    
    def count_punctuation_marks(self):
        punctuation_marks = ",.;:?!"
        return sum(self.text.count(mark) for mark in punctuation_marks)
    
file_path = "17_lesson\Exercise11.7_text.txt"
text_analysis = TextAnalysis(file_path)
print(f"Paragraphs: {text_analysis.count_paragraphs()}")