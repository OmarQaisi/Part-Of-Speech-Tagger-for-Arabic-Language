from tokenizer import Tokenizer
from tagger import Tagger

test = "Corpus\\Sports\\الرياضة و الصحة النفسية.txt"
token = Tokenizer(test)
result = token.tokenize()
tagger = Tagger()
tags = tagger.tag(result)
for word in result:
    try:
        tag = tags[word]
    except:
        tag = "?"
    print(word, " ", tag)

print(len(result))
print(len(tags))
