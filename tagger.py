class Tagger:

    def tag(self,file):
        dic = {}
        conjunctions = ["تحت","وراء","حيث","دون","حين","صباح","ظهر","","أمام","فوق","كل","لي","لها","لنا","لهم","لك","له","أنا","أنتما","أنتم","أنتن","هو","هي","هم","أياي","ايانا","اياك","اياكما","اياكم","اياكن","اياه","اياها","اياهم","اياهن","اياهما","هن","هما","أنتما","أنت","نحن","أي","يا","أيتها","أيها","هيا","أيا","على","إلى","عن","من","قي"]
        patterns= [["فعل"]]
        nounPrefix = ["ال","لل","فال","كال","بال"]
        for i in range(0,len(file)):
            if file[i] in conjunctions:
                dic.update({file[i] : "P"})
                continue
            for prefix in nounPrefix:
                if file[i].startswith(prefix):
                    dic[file[i]] = "N"
                    break
        return dic