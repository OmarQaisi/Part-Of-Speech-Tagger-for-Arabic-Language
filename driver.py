from tokenizer import Tokenizer

test = "file1.txt"
token = Tokenizer(test)
result = token.tokenize()
for word in result:
    print(word)
        
    
