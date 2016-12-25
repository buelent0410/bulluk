# -*- encoding: utf-8 -*-

import codecs
import re
import requests
from langdetect import detect


class Datenabzug():
    
    def __init__(self):
        pass
    
    def get_amazon(self):
    
        review_URLs = ['https://www.amazon.de/product-reviews/B00TX5O8WE/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&showViewpoints=1&sortBy=recent&pageNumber=',\
                        'https://www.amazon.de/product-reviews/B00TX5PG3E/ref=cm_cr_dp_see_all_btm?ie=UTF8&reviewerType=all_reviews&showViewpoints=1&sortBy=recent&pageNumber=',\
                        'https://www.amazon.de/product-reviews/B01BTZFM0W/ref=cm_cr_dp_see_all_btm?ie=UTF8&reviewerType=all_reviews&showViewpoints=1&sortBy=recent&pageNumber=',\
                        'https://www.amazon.de/product-reviews/B01BTZFSTC/ref=cm_cr_dp_see_all_btm?ie=UTF8&reviewerType=all_reviews&showViewpoints=1&sortBy=recent&pageNumber=' \
                       ]
        
    
        delim = '<#!#>'
        for review_URL in review_URLs:
            a = 0
            filename = review_URL.split('product-reviews/')[1].split('/')[0]+'.csv'
            f = codecs.open(filename, 'w', "utf-8-sig")
            f.write('id%sstars%stopic%susername%sdate%scontent\n' % (delim, delim, delim, delim, delim))
            
            for i in range(1,10000):
    
                # URL Variabledefinition
                review_URLx = review_URL+str(i-a)
                dividing_tag = '<i data-hook="review-star-rating"'
    
                div_tag_text_start = '<span data-hook="review-body" class="a-size-base review-text">'
                div_tag_text_end = '</span>'
                
                div_tag_stars_start = '<span class="a-icon-alt">'
                div_tag_stars_end = '</span>'
        
                div_tag_topic_1 = '<a data-hook="review-title"'
                div_tag_topic_2 = '</a>'
                div_tag_topic_3 = '>'
        
                div_tag_username_1 = '<a data-hook="review-author"'
                div_tag_username_2 = '</a>'
                div_tag_username_3 = '>'
        
                div_tag_date_start = 'review-date">'
                div_tag_date_end = '</span>'
    
    
                # Abzug des HTML-Quellcodes von der oben definirten URL
                headers = {'User-agent': 'Mozilla/5.0'}
                r = requests.get(review_URLx, headers=headers)
                print "%s: %s wurde abgezogen, Status: %s, Encoding: %s" % (filename, str(i-a), r.status_code, r.encoding)
                source_txt = r.text.encode('utf-8')
    
                # Endbedingung letzte Seite
                if not source_txt.count(dividing_tag): break
                
                # Aufteilung des Quellcodes
                reviews = source_txt.split(dividing_tag)[1:]
    
                x = 1
                for review in reviews:
                
                    # get text
                    review_text = (review.split(div_tag_text_start)[1].split(div_tag_text_end)[0]).decode('utf-8')
                    
                    # get stars
                    stars = (review.split(div_tag_stars_start)[1].split(div_tag_stars_end)[0]).decode('utf-8')
    
                    # get topic
                    topic = (review.split(div_tag_topic_1)[1].split(div_tag_topic_2)[0].rpartition(div_tag_topic_3)[2]).decode('utf-8')
    
                    # get username
                    username = (review.split(div_tag_username_1)[1].split(div_tag_username_2)[0].rpartition(div_tag_username_3)[2]).decode('utf-8')
                    
                    # get date
                    date = ((review.split(div_tag_date_start)[1].split(div_tag_date_end)[0]).replace('am ','')).decode('utf-8')
    
                    # language detection - skip non-German reviews
                    if not detect(review_text) == "de": continue
                    
                    # replace 3 or more characters in a row by max 2 characters in a row
                    review_text = re.sub(r'(\w)\1{2,}',r'\1\1',review_text)
                    
                    # length detection - skip reviews shorter than 10 characters
                    if len(review_text) < 10: continue
    
                    f.write('%s%s%s%s%s%s%s%s%s%s%s\n' % (str((i-a-1)*10+x), delim, stars, delim, topic, delim, username, delim, date, delim, review_text))
                    x = x + 1
    
    
            f.close()