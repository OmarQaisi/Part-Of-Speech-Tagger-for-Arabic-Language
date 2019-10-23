from tokenizer import Tokenizer

test = "Corpus//Sports/ظاهرة العنف والتعصب الرياضي.txt"
token = Tokenizer(test)
result = token.tokenize()
for word in result:
    print(word)
