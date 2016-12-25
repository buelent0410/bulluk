# -*- encoding: utf-8 -*-

'''
Created on 08.12.2016

@author: Aydin
'''
"""
import os
from nltk.parse import stanford

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


"""
# HIER IST DIE SPRACHERKENNUNG.
from langdetect import detect
import codecs
filename = "B00TX5O8WE_sauber.csv"
f = codecs.open(filename, 'r', "utf-8-sig")
for line in f.readlines():
    print detect(line)
f.close()
"""

"""
# HIER IST DIE MEHRZEICHENERSETZUNG.
import re
text = "Das ist aber uuuuuuuunglllllaubbbblllllliccccch!"
text = re.sub(r'(\w)\1{2,}',r'\1\1',text)
print text
"""

# HIER IST DIE SPEELING KORREKTUR.
sentence = "Ich bin sher zufrieden mit dem Gerät und finde dass es zu den besten der Galaxy Reihe gehört. Auch die Grüne Farbe ist sehr anschaulich und sieht unglaublich gut aus.Kamera:Die Kamera macht einen sehr guten Eindruck und schießt mit 16MP Bilder bis zu UHD-Qualität (16:9).Auch Nachts kann sich die Kamera sehen lassen, denn die Blende nimmt das Licht gut auf, so dass Fotos auch Nachts gut aussehen. Auch die Frontkamera mit ihren 5MP kann sich sehen lassen. Nur in der Nacht ist es etwas schwer damit Selfies zu schießen.Ausstattung:Eine gute Wahl finde ich, dass Samsung sich gegen den SD810 entschieden hat und stattdessen den hauseigenen Exynos7420 Prozessor verbaut. Dieser zeigt eine sehr gute Leistung und läuft selbst bei aufwändigen Prozessen ohne jegliche Ruckler.System:Sasmung integriert in das System sshr viele Positive seiten. Es sieht einfach gut aus und ist leicht zu bedienen.Wem dass Samsung-Design nicht gefällt, kann sich weitere Designs aus dem Samsung Theme Store beziehen.Auch der Edge Bereich wird beim neuen Marshmallow Update sehr gut ausgenutzt.Akku:Leider ist der Akku mit nur 2.600mah knapp bemessen, hält aber bei mäßiger Nutzung gut einen Tag durch. Nur für intensiv Nutzer wird es schwer über die Runde zu kommen, da dann nach ungefähr 6 Stunden Schluss. Dafür legt Samsung ein 2 Ampere stecker bei, womit der Akku innerhalb von einer Stunde wieder vollständig geladen ist.Es bietet aber leider nicht so eine gute Akkulaufzeit wie dei Sony Xperia Z Reihe.Design:Das Samsung Galaxy S6 Edge gefällt mir sehr gut. Mit den abgerundeten Kanten sieht es nicht nur gut aus, sondern liegt auch gefühlt stabiler in der Hand, als das Samsung Galaxy S6. Die Glasrückseite verpasst dwm Gerät einen edlen Look, nur Rate ich zu einer Schutzhülle, da diese sehr anfällig für Fingerabdrücke ist.Empfang:Ich habe mit dem Samsung Galaxy S6 Edge wenig bis keine Einschränkungen im Mobilfunknetz. Verglichen mit einem Sony Xperia Z3 bietet es einen sehr guten Empfang. Nur im EDGE und GPRS Netz ist dass Internet nicht gerade schnell und reicht oftmals nur für WhatsApp Nachrichten.Sound:Der Lautsprecher bietet einen schönen und harmonischen Klang mit einem kleinen Hauch Bass. Selbst auf voller Lautstärke ist kein Krachen zu hören.Die Kopfhörer hingegen lassen viele Geräusche durch. Somit ist es bei geringer Lautstärke schwer Musik zu hören.Ich persönlich Empfehel das Gerät weiter."
import enchant
d = enchant.Dict("de")
sentence_new = ""
for word in sentence.split(" "):
    print d.check(word), word, d.suggest(word)
    if not d.check(word) and d.suggest(word):
        sentence_new = sentence_new + d.suggest(word)[0] + ' '
    else: sentence_new = sentence_new + word + ' '
print sentence_new