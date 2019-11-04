import re


class Tagger:

    def tag(self, file):
        dic = {}
        conjunctions_noun = ["ليت", "و", "لعل", "كأن", "إِنَّ", "تحت", "وراء", "حيث", "دون", "حين", "صباح", "ظهر",
                             "أمام",
                             "فوق", "كل", "لي", "لها", "لنا", "لهم", "لك", "له", "أنا", "أنتما", "أنتم", "أنتن", "هو",
                             "هي", "هم", "أياي", "ايانا", "اياك", "اياكما", "اياكم", "اياكن", "اياه", "اياها", "اياهم",
                             "اياهن", "اياهما", "هن", "هما", "أنتما", "أنت", "نحن", "أي", "يا", "أيتها", "أيها", "هيا",
                             "أيا", "على", "إلى", "عن", "من", "في"]
        conjunctions_verb = ["أن", "لن", "كي", "حتى", "لم", "لما", "لا", "إن", "ما", "مهما", "متى", "أينما", "حيثما"]
        kan = ["ليس", "بات", "أمسى", "ظل", "أضحى", "أصبح", "صار", "كان"]
        nounprefix = ["ال", "لل", "فال", "كال", "بال"]
        verbprefix = ["سي", "سن", "ست", "سأ"]

        # to do: add suffixes

        verbpatterns = ["ا..وع.", "ا.ت..", "است..."]
        nounpatterns = ["م...", "م..ا.", "..ا.ة", "م...ة", "...ى", "..ي."]
        for i in range(0, len(file)):
            if file[i] in conjunctions_noun:
                dic.update({file[i]: "P"})
                dic.update({file[i + 1]: "N"})
                i += 1
                continue
            elif file[i] in conjunctions_verb:
                dic.update({file[i]: "P"})
                dic.update({file[i + 1]: "V"})
                dic.update({file[i + 2]: "N"})
                i += 2
                continue
            elif file[i] in kan:
                dic.update({file[i]: "V"})
                dic.update({file[i + 1]: "N"})
                i += 1
                continue
            else:
                flag = True
                if flag:
                    for pattern in verbpatterns:
                        if re.match(pattern, file[i]):
                            dic[file[i]] = "V"
                            dic[file[i + 1]] = "N"
                            i += 1
                            flag = False
                            break
                if flag:
                    for pattern in nounpatterns:
                        if re.match(pattern, file[i]):
                            dic[file[i]] = "N"
                            flag = False
                            break
                if flag:
                    for prefix in nounprefix:
                        if file[i].startswith(prefix):
                            dic[file[i]] = "N"
                            flag = False
                            break
                if flag:
                    for prefix in verbprefix:
                        if file[i].startswith(prefix):
                            dic[file[i]] = "V"
                            dic[file[i + 1]] = "N"
                            i += 1
                            flag = False
                            break
                if flag:
                    dic[file[i]] = "N"

        return dic
