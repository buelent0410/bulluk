'''
Created on 10.12.2016

@author: Aydin
'''

class Main():
    def __init__(self):
        #self.datenabzug()
        self.textverarbeitung()
        
    def datenabzug(self):
        import Datenabzug as D
        D.Datenabzug().get_amazon()
    
    def textverarbeitung(self):
        pass
        import TextVerarbeitung as T
        T.TextVerarbeitung().test()


Main()