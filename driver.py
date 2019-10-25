from tokenizer import Tokenizer

test = "Corpus//Sports/رياضة تحت الماء.txt"
token = Tokenizer(test)
result = token.tokenize()
for word in result:
    print(word)
