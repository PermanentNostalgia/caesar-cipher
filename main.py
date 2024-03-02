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
        
def encrypt(plain, rotations):
    plain_tokens = StringTokens(plain)
    syllables = []

    for index, word in enumerate(plain):
        if HanSyllable.isHangul(word):
            syllables.append([index,HanSyllable(word)])

    for word in syllables:
        index = word[0]
        syllable = word[1]
    
        offsets = syllable.getOffsets()
        offsets[2] += 1 # 종성의 오프셋의 경우 1 작게 설정되어 있음
        
        offsets[0] = (offsets[0] + rotations[0]) % 19
        offsets[1] = (offsets[1] + rotations[1]) % 21
        offsets[2] = (offsets[2] + rotations[2]) % 28 - 1

        syllable.setOffsets(offsets)

        plain_tokens.editToken(index, str(syllable))

    return plain_tokens.toStr()

while True:
    name = input("암호화할 파일의 이름을 입력하세요: ")
    enc_name = input("암호문을 저장할 파일의 이름을 입력하세요: ")
    r1 = int(input("초성의 회전수를 입력하세요: "))
    r2 = int(input("중성의 회전수를 입력하세요: "))
    r3 = int(input("종성의 회전수를 입력하세요: "))

    file = open(name, "r", encoding="UTF-8")

    plain = file.read()
    file.close()
    
    encrypted = encrypt(plain, [r1,r2,r3])

    new_file = open(enc_name, "w", encoding="UTF-8")
    new_file.write(encrypted)

    new_file.close()
    print("--암호화 성공--")
