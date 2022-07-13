import nltk

s = "Good muffins cost $3.88\nin New York.  Please buy me\ntwo of them.\n\nThanks."
print("Original Sentence")
print(s)

print("\nSplit: basic & \\n")
print(s.split())
print(s.split('\n'))

print("\nwordpunct_tokenize()")
print(nltk.wordpunct_tokenize(s))

print("\nword_tokenize()")
print(nltk.word_tokenize(s))

print("\nsent_tokenize()")
print(nltk.sent_tokenize(s))

print("\nSpaceTokenizer & split blank")
print(s.split(' '))
print(nltk.SpaceTokenizer().tokenize(s))

print("\nWhitespaceTokenizer")
print(nltk.WhitespaceTokenizer().tokenize(s))

print("\nWhitespaceTokenizer with span_tokenize")
print(list(nltk.WhitespaceTokenizer().span_tokenize(s)))

print("\nTreebankWordTokenizer")
tokens =  nltk.TreebankWordTokenizer().tokenize(s)
print(tokens)
s2 = "They'll save and invest more. hi, my name can't hello,"
tokens2 = nltk.TreebankWordTokenizer().tokenize(s2)
print(tokens2)

print("\nTreebankWordDetokenizer")
print(nltk.treebank.TreebankWordDetokenizer().detokenize(tokens))
print(nltk.treebank.TreebankWordDetokenizer().detokenize(tokens2))


