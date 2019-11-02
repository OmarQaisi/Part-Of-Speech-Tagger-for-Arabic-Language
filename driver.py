from tokenizer import Tokenizer

test = "Corpus\\Technology\\تقنية بلوك تشين2.txt"
token = Tokenizer(test)
result = token.tokenize()
for word in result:
    print(word)
