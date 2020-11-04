#!/usr/bin/env python3

from linked_list import *
# TODO: is modifying recursion limit ok (Piazza post said ok but for other question)?
import sys
sys.setrecursionlimit(2000)


def get_list_of_sentences(chapter1='swansway-chapter1.txt'):
    def to_sentences(p):
        for delimiter in '.?!': p = p.replace(delimiter, '|')
        return [s.strip('\" ') for s in p.split('|')]
    with open(chapter1, 'r', encoding='UTF-8') as f:
        paragraphs = f.readlines()

    sentences = [s for p in paragraphs for s in to_sentences(p) if len(s) > 1]
    list_of_sentences = Nil()
    for s in sentences[::-1]:
        list_of_sentences = list_of_sentences.prepend(s)

    return list_of_sentences


def longest_sentence():
    list_of_sentences = get_list_of_sentences()
    # TODO: Debugging (remove later)
    # print(list_of_sentences)

    def word_count(sentence):
        return len(sentence.split())

    def higher(a, b):
        return a if a > b else b

    return list_of_sentences.for_each(word_count).reduce_right(higher)


# TODO: Debugging (erase / comment out later, i.e, no demo needed?)
# print(longest_sentence())
