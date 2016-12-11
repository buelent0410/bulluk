# -*- encoding: utf-8 -*-

import codecs
import re


class TextVerarbeitung():
    def __init__(self):
        pass

    def remove_entities(self, text):
        text = text.replace('<br />','')
        text = text.replace('&#34;','"')
        text = text.replace('&eacute;','e')
        text = text.replace('&egrave;','E')
        text = text.replace('&#60;','<')
        text = text.replace('&szlig;','ß')
        text = text.replace('&uuml;','ü')
        text = text.replace('&Auml;','Ä')
        text = text.replace('&quot;','"')
        text = text.replace('&nbsp;',' ')
        text = text.replace('&#62;','>')
        text = text.replace('&auml;','ä')
        text = text.replace('&ouml;','ö')
        text = text.replace('&Uuml;','Ü')
        text = text.replace('&Ouml;','Ö')
        text = text.replace('&gt;','<')
        text = text.replace('&agrave;','E')
        text = text.replace('&amp;','&')
        text = text.replace('&lt;','<')
        text = text.replace('&aacute;','á')
        text = text.replace('&iacute;','í')
        text = text.replace('&uacute;','ú')
        
        return text
    
    # Diese Funktion schreibt alle entities in der Datei aus.
    def check_text(self, content):
    
        for item in set(re.findall("&[a-zA-Z0-9#]+;", content)):
            print '%s' % (item)


    def open(self, filename):
        f = codecs.open(filename)
        content = f.read()
        f.close()
        
        return content
    
    def write(self, filename, content):
        g = codecs.open(filename, 'w', 'utf-8-sig')
        g.write(content.decode('utf-8'))
        g.close()

#===============================================================================
# def remove_entities_manually(filename):
#     f = codecs.open(filename)
#     a = f.read()
#     f.close()
#     #out = remove_entities(a)
#     a = a.replace('µ','u')
#     a = (a.replace('µ','µ')).decode('utf-8')
#     g = codecs.open(filename.split('.')[0]+'_sauber.csv', "w", "utf-8-sig")
#     g.write(a)
#     g.close()
# filenames = ['B00TX5O8WE.csv', 'B00TX5PG3E.csv', 'B01BTZFM0W.csv', 'B01BTZFSTC.csv']
# for filename in filenames:
#     remove_entities_manually(filename)
#===============================================================================