class Sp2_class:
    def __init__(self, param1, param2):
        self.par1 = param1
        self.par2 = param2


    # Private data property getters & setters
    @property
    def par1(self):
        return self._par1

    @par1.setter
    def par1(self, param1):
        self._par1 = param1

    def __str__(self):
        return "Sb2 Class: private _par1 = \"{0}\", private _par2 = \"{1}\"".format(self.par1, self.par2)