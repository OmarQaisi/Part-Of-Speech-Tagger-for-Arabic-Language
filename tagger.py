import re


class Tagger:

    def tag(self, file):
        result = []
        conjunctions_noun = ["ليت", "و", "لعل", "كأن", "إِنَّ", "تحت", "وراء", "حيث", "دون", "حين", "صباح", "ظهر",
                             "أمام", "إما", "إلا", "أو","بعد",
                             "فوق", "كل", "لي", "لها", "لنا", "لهم", "لك", "له",
                             "أياي", "ايانا", "اياك", "اياكما", "اياكم", "اياكن", "اياه", "اياها", "اياهم",
                             "اياهن", "اياهما", "هن", "هما", "أي", "يا", "أيتها", "أيها", "هيا",
                             "أيا", "على", "إلى", "عن", "من", "في"]
        conjunctions_verb = ["أن", "لن", "كي", "حتى", "لم", "لما", "لا", "إن", "ما", "مهما", "متى", "أينما", "حيثما",
                             "قد"]
        kan = ["ليس", "بات", "أمسى", "ظل", "أضحى", "أصبح", "صار", "كان"]
        nounprefix = ["ال", "لل", "فال", "كال", "بال"]  # check first
        verbprefix = ["سي", "سن", "ست", "سأ"]

        # to do: add suffixes

        verbpatterns = ["ا..وع.", "ا.ت..", "است..."]
        nounpatterns = ["م...", "م..ا.", "..ا.ة", "م...ة", "...ى", "..ي."]

        i = -1
        while i < len(file) - 1:
            i += 1
            if file[i] in conjunctions_noun:
                result.append("P")
                result.append("N")
                i += 1
                continue
            elif file[i] in conjunctions_verb:
                result.append("P")
                result.append("V")
                result.append("N")
                i += 2
                continue
            elif file[i] in kan:
                result.append("V")
                result.append("N")
                i += 1
                continue
            else:
                flag = True
                if flag:
                    for prefix in nounprefix:
                        if file[i].startswith(prefix):
                            result.append("N")
                            flag = False
                            break

                if flag:
                    for prefix in verbprefix:
                        if file[i].startswith(prefix):
                            result.append("V")
                            result.append("N")
                            i += 1
                            flag = False
                            break

                if flag:
                    for pattern in verbpatterns:
                        if re.match(pattern, file[i]):
                            result.append("V")
                            result.append("N")
                            i += 1
                            flag = False
                            break

                if flag:
                    for pattern in nounpatterns:
                        if re.match(pattern, file[i]):
                            result.append("N")
                            flag = False
                            break
                if flag:
                    result.append("N")

        return result
