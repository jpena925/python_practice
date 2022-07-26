#using Translator module found in pypi 

#found this in the docs, creating the translator to korean
from translate import Translator
translator = Translator(to_lang="ko")

#opening a file i have currently
try:
    with open('../translate.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        #creating a new file that will write a translation of the other file into korean
        with open('../test-ko.txt', mode="w") as my_file2:
            my_file2.write(translation)
except FileNotFoundError:
    print('Check file path')