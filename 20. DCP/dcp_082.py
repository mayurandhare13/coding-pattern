class FileRead:
    def __init__(self, content):
        self.content = content
        self.offset = 0
        self.buffer = ''

    def read7(self):
        start = self.offset
        end = min(start + 7, len(self.content))

        self.offset = end
        return self.content[start:end].strip()

    def readN(self, n):
        while len(self.buffer) < n:
            nextChars = self.read7()
            if not nextChars:
                break
            self.buffer += nextChars
        
        nChars = self.buffer[:n]
        self.buffer = self.buffer[n:]

        return nChars


if __name__ == '__main__':
    content = "Hello world"
    fr = FileRead(content)

    print(fr.readN(3))
    print(fr.readN(3))
    print(fr.readN(3))
    print(fr.readN(3))

    print('-' * 10)
    
    content2 = "Hello world"
    fr2 = FileRead(content2)
    print(fr2.read7())
    print(fr2.read7())
    print(fr2.read7())

