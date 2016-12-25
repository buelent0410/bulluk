# -*- encoding: utf-8 -*-

'''
Created on 08.12.2016

@author: Aydin
'''
import os
from nltk.parse import stanford
"""
os.environ['STANFORD_PARSER'] = 'C:\Users\Aydin\Downloads\StanfordCoreNLPjars.de\inst\java'
#os.environ['STANFORD_MODELS'] = '/path/to/standford/jars'

parser = stanford.StanfordParser(model_path="C:\Users\Aydin\Downloads\StanfordCoreNLPjars.de\inst\java")


sentences = parser.raw_parse_sents(("Hello, My name is Melroy.", "What is your name?"))
print sentences

# GUI
for line in sentences:
    for sentence in line:
        sentence.draw()
"""

# HIER IST DIE SPRACHERKENNUNG.
from langdetect import detect
import codecs
filename = "B00TX5O8WE_sauber.csv"
f = codecs.open(filename, 'r', "utf-8-sig")
for line in f.readlines():
    print detect(line)
f.close()
