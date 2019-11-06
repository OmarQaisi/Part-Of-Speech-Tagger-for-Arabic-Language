from tokenizer import Tokenizer
from tagger import Tagger


test = "Corpus\\Sports\\الرياضة و شهر رمضان المبارك.txt"

token = Tokenizer(test)
result = token.tokenize()
tagger = Tagger()
tags = tagger.tag(result)
for i in range(0,len(result)):
    print(result[i]+" "+tags[i])

print(len(result))
print(len(tags))
print(tags)
