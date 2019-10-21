from tokenizer import Tokenizer

test = "Corpus\\Technology\\علم تكنولوجيا المعلومات.txt"
token = Tokenizer(test)
result = token.tokenize()
for word in result:
    print(word)
        
    
