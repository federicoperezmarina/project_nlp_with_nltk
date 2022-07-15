import nltk

input = """At eight o'clock on Thursday morning Arthur didn't feel very good.
            My cat is beautiful.
            I love my car."""

tokens = nltk.word_tokenize(input)

print(tokens)