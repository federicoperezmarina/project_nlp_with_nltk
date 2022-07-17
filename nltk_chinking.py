from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk import RegexpParser
from nltk import Tree

sentence = "It's a dangerous business, Frodo, going out your door."

print("Sentence: ")
print(sentence)

words = word_tokenize(sentence)
print("Words of the sentence: ")
print(words)

words_pos_tags = pos_tag(words)
print("Word pos tag: ")
print(words_pos_tags)

grammar = """
Chunk: {<.*>+}
       }<JJ>{"""
chunk_parser = RegexpParser(grammar)
tree = chunk_parser.parse(words_pos_tags)
print("Tree chinking: ")
print(tree)
tree.draw()