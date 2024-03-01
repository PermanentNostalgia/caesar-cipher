from hangul import HanSyllable

class StringTokens:
    def __init__(self, string):
        self.__tokens = list(string)

    def getTokens(self):
        return list(self.__tokens)

    def editToken(self, index, token):
        self.__tokens[index] = token

    def toStr(self):
        string = ""

        for token in self.__tokens:
            string += token

        return string
        

plain = input("암호화할 문자열을 입력해주세요: ")
plain_tokens = StringTokens(plain)
syllables = []

for index, word in enumerate(plain):
    if HanSyllable.isHangul(word):
        syllables.append([index,HanSyllable(word)])

rotation = int(input("회전시킬 바퀴수를 입력하세요: "))

for word in syllables:
    index = word[0]
    syllable = word[1]
    
    offsets = syllable.getOffsets()
    offsets[2] += 1 # 종성의 오프셋의 경우 1 작게 설정되어 있음

    offsets[0] = (offsets[0] + rotation) % 19
    offsets[1] = (offsets[1] + rotation) % 21
    offsets[2] = (offsets[2] + rotation) % 28 - 1

    syllable.setOffsets(offsets)

    plain_tokens.editToken(index, str(syllable))

print(plain_tokens.toStr())
