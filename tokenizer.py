class Tokenizer:
    def __init__(self, directory):
        self.directory = directory
        self.txt = open(directory,"r",encoding='utf-8')

    def tokenize(self):
        content = self.txt.read()
        for i in range(0,len(content)):
            if content[i] in ['”','“',"،",".","!",":",'"',"-","؟","?","''",';','؛',')','(',",",'/',"\\","0","1","2","3","4","5","6","7","8","9","٠","١","٢","٣","٤","٥","٦","٧","٨","٩"]:
                content=content[0:i]+" "+content[i+1:]
        result = content.split(" ")
        i = 0
        while True:
            if result[i] == "":
                result.pop(i)
            else:
                i=i+1
            if i == len(result):
                break 
        return result

