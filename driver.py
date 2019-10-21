from tokenizer import Tokenizer

test = "Corpus//Technology//tech1.txt"
token = Tokenizer(test)
result = token.tokenize()
for word in result:
    print(word)