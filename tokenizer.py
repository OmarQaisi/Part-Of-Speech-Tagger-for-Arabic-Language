class Tokenizer:
    def __init__(self, directory):
        self.directory = directory
        self.txt = open(directory,"r",encoding='utf-8')

    def tokenize(self):
        content = self.txt.read()
        result = content.split(" ")
        for i in range(0,len(result)):
            for j in range(0,len(result[i])):
                if result[i][j] in ["،",".","!",":",'""',"-","?","''"]:
                    result[i]=result[i][0:j]+result[i][j+1:]
        return result
