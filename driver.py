from tokenizer import Tokenizer
from tagger import Tagger


test = "Corpus\\Sports\\ظاهرة العنف والتعصب الرياضي.txt"

token = Tokenizer(test)
result = token.tokenize()
tagger = Tagger()
tags = tagger.tag(result)
for i in range(0,len(result)):
    print(result[i]+" "+tags[i])

print(len(result))
print(len(tags))
print(tags)
import pandas as pd
list = [None] * len(result)
for i in range(len(result)):
    list[i] = ([result[i], 'N'])

df = pd.DataFrame(list)
df.to_csv("ظاهرة العنف والتعصب الرياضي.csv", index=False, header=False)