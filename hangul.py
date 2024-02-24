class HanSyllable:
    SYLLABLE_ENTRY = 0xAC00
    CHOSEONG_ENTRY = 0x1100
    JUNGSEONG_ENTRY = 0x1161
    JONGSEONG_ENTRY = 0x11A8
    
    def __init__(self, word):
        if not (len(word) == 1 and self.isHangul(word)):
            raise Exception("유효하지 않은 글자")

        offset = ord(word) - 0xAC00

        self.__jongseong = offset % 28 - 1
        self.__jungseong = offset // 28 % 21
        self.__choseong = offset // 28 // 21

    def printJamo(self):
        print(chr(self.__choseong + self.CHOSEONG_ENTRY), end='')
        print(chr(self.__jungseong + self.JUNGSEONG_ENTRY), end='')
        if self.__jongseong != -1:
            print(chr(self.__jongseong + self.JONGSEONG_ENTRY), end='')

    def printSyllable(self):
        print(chr(self.SYLLABLE_ENTRY + self.__choseong*28*21 + self.__jungseong*28 + self.__jongseong + 1), end='')
    
    def isHangul(self, word):
        code = ord(word)

        if code>=0xAC00 and code<=0xD7AF:
            return True
        else:
            return False

    def changeChoseong(self, offset):
        if not (offset >= 0 and offset <= 19):
            raise Exception("잘못된 오프셋")

        self.__choseong = offset

    def changeJungseong(self, offset):
        if not (offset >= 0 and offset <= 21):
            raise Exception("잘못된 오프셋")

        self.__jungseong = offset

    def changeJongseong(self, offset):
        if not (offset >= -1 and offset <= 27):
            raise Exception("잘못된 오프셋")

        self.__jongseong = offset
