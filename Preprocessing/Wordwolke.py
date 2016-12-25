# -*- encoding: utf-8 -*-

'''
Created on 25 Dec 2016

@author: jogin
'''

import codecs
import re
import wordcloud

class Wordwolke():
    def __init__(self):
        pass
    
    from wordcloud import WordCloud, STOPWORDS
    import matplotlib.pyplot as plt
    
    #Convert all the required text into a single string here 
    #and store them in word_string
    
    #you can specify fonts, stopwords, background color and other options
    
    wordcloud = WordCloud(font_path='/Users/kunal/Library/Fonts/sans-serif.ttf',
                              stopwords=STOPWORDS,
                              background_color='white',
                              width=1200,
                              height=1000
                             ).generate(word_string)
    
    
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()