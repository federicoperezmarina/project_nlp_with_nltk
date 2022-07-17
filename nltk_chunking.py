from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk import RegexpParser
from nltk import Tree

sentence = "I have a very nice car. My car is a ferrari and it is red. I will never buy a Porche."

print("Sentence: ")
print(sentence)

words = word_tokenize(sentence)
print("Words of the sentence: ")
print(words)

words_pos_tags = pos_tag(words)
print("Word pos tag: ")
print(words_pos_tags)

grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = RegexpParser(grammar)
tree = chunk_parser.parse(words_pos_tags)
tree.draw()