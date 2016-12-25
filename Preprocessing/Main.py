'''
Created on 10.12.2016

@author: Aydin
'''

class Main():
    def __init__(self):
        #self.datenabzug()
        #self.textverarbeitung()
        self.wordwolke()
        pass
        
    def datenabzug(self):
        import Datenabzug as D
        D.Datenabzug().get_amazon()
    
    def textverarbeitung(self):
        import TextVerarbeitung as T
        content = T.TextVerarbeitung().open('galaxy_s7.csv')
        content = T.TextVerarbeitung().remove_entities(content)
        print 'Verbliebene Entities:'
        T.TextVerarbeitung().check_text(content)
        T.TextVerarbeitung().write('galaxy_s7_sauber.csv', content)

    def wordwolke(self):
        import Wordwolke as W
        pass

Main()