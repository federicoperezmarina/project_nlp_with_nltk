import nltk

input = """At eight o'clock on Thursday morning Arthur didn't feel very good.
			My cat is beautiful.
			I love my car."""

for sentence in nltk.sent_tokenize(input):
	print(nltk.word_tokenize(sentence))