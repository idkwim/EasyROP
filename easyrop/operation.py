class Operation:
    def __init__(self, name):
        self.__name = name
        self.__sets = []

    def setDst(self, dst):
        if dst:
            for s in self.__sets:
                s.setDst(dst)

    def setSrc(self, src):
        if src:
            for s in self.__sets:
                s.setSrc(src)

    def setAux(self, aux):
        if aux:
            for s in self.__sets:
                s.setAux(aux)

    def setAddress(self, address):
        if address:
            for s in self.__sets:
                s.setAddress(address)

    def addSet(self, s):
        self.__sets += [s]

    def getSets(self):
        return self.__sets

    def __str__(self):
        string = ''
        for s in self.__sets:
            string += str(s) + '\n'
        return string
