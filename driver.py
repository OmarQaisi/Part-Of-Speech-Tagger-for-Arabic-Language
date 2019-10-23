from tokenizer import Tokenizer

test = "Corpus//Sports//sports1.txt"
token = Tokenizer(test)
result = token.tokenize()
for word in result:
    print(word)
