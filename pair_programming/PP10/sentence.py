#!/usr/bin/env python3

#Coder: Moriya Dechtiar
#Sharer: Gerald Arocena
#Listener: Kaiwen Li

import reprlib

# def wordGen(words):
#     for word in words:
#         yield word
            
class Sentence:
    def __init__(self, text): 
        self.text = text
        self.words = text.split()

    def __iter__(self):
        # return wordGen(self.words)
        for word in self.words:
            yield word

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


line = Sentence("This is my sentence")
for i in line:
    print(i)

check = iter(line)
print(next(check))
print(next(check))
print(next(check))
print(next(check))
# print(next(check))       # This should return an error