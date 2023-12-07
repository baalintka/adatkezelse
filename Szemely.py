import datetime
class Szemely:
    def __init__(self,nev,szuldatum,szszam,nem):
        self.nev=nev
        self.szuldatum=szuldatum
        self.szszam=szszam
        self.nem=nem

    '''tagfüggvény, oszálymetódus'''
    def kor(self):
        x=datetime.datetime.now()
        return x.year-self.szdatum
