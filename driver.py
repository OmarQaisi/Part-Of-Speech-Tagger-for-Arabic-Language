from tokenizer import Tokenizer
from tagger import Tagger

test = "Corpus\\Technology\\تقنية بلوك تشين2.txt"
token = Tokenizer(test)
result = token.tokenize()
for word in result:
    print(word)
tagger = Tagger()
tags = tagger.tag(result)
for t,v in tags.items():
    print(t,v)
print(len(result))
print(len(tags))
