
import time
from token import OP
from unittest.mock import call
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import pandas as pd
from urllib.parse import urlparse

import re

df = pd.read_excel(r'C:\Users\HP\Dropbox\PC\Desktop\domains_scrapy\Neutronian Test Crawl 100 Domains Sept2022.xlsx')
urls= df['website'].values

def domain_names(urls):
    Links=[]
    for url in urls:
        domains=re.search('https?://([A-Za-z_0-9.-]+).*', url).group(1)
        Links.append(domains)
    return Links
def condition(text,words):
    
    return set(words).issubset(text.split('/'))

class ExampleSpider(CrawlSpider):
    name = 'example'
    
    custom_settings = {
    'DEPTH_LIMIT': 2,
    'SCHEDULER ORDER':'BFO'
}
    
    start_urls= ['https://www.kohls.com/','https://www.tollbrothers.com/']
    # for url in urls:
    #     start_urls.append(url)
    # for url in urls[0:20]:
    #     start_urls.append(url)
    
    allow_domain=[]
    allowed_domains = domain_names(start_urls)
    for value in start_urls:
        domain=urlparse(str(value)).netloc
        #print(domain)
        #start_urls.append(value)
        allow_domain.append(domain)
    print(allow_domain)
    
    
    #rules=[Rule(LinkExtractor(), callback='parse_item', follow=True)]
    rules=(
        Rule(LinkExtractor(allow_domains=allow_domain),callback='parse_item', follow=True),)
    
    
    #print(len(urls))
    
    
    def parse_item(self, response):
        privacy= []
        ToS=[]
        OptOut=[]
        DoNotSell=[]
        CaliforniaNotice=[]
        cookiePolicy=[]
        subjectAccessRequest=[]
        PrivacyCenter=[]
        About=[]
        Leadership=[]
        Investors=[]
        BoardDirectors=[]
        SensitiveData=[]
        Subprocessors=[]
        contact=[]
        ThirdParties=[]
        Locations=[]
        ChildrenPrivacy=[]
        AdChoices=[]
        
        Links=[]
        Links.append(response.url)
        

        
        for link in Links:
            print(link)
            #time.sleep(4)
            if condition(link,words=('privacy',)):
            #if all(map(lambda w: w in link, ('privacy'))):
                privacy.append(link)
            if condition(link,words=('privacy-policy',)):
            #if all(map(lambda w: w in link, ('privacy'))):
                privacy.append(link)
            
            if condition(link,words=('terms',)):
                ToS.append(link)
            if condition(link,words=('about',)):
                About.append(link)
            if condition(link,words=('subject-access-request',)):
                subjectAccessRequest.append(link)
            if condition(link,words=('privacy-center',)):
                PrivacyCenter.append(link)
            if condition(link,words=('leadership',)):
                Leadership.append(link)
            
            if condition(link,words=('investors',)):
                Investors.append(link)
            if condition(link,words=('board-of-directors',)):
                BoardDirectors.append(link)
            if condition(link,words=('directors',)):
                BoardDirectors.append(link)
            if condition(link,words=('board-of-directors',)):
                BoardDirectors.append(link)
            if condition(link,words=('sensitive',)):
                SensitiveData.append(link)
            if condition(link,words=('sensitive-data',)):
                SensitiveData.append(link)
            if condition(link,words=('subprocessors',)):
                Subprocessors.append(link)
            if condition(link,words=('contact',)):
                contact.append(link)
            if condition(link,words=('third-parties',)):
                ThirdParties.append(link)
            if condition(link,words=('locations',)):
                Locations.append(link)
            if condition(link,words=('children',)):
                ChildrenPrivacy.append(link)
            if condition(link,words=('ad-choices',)):
                AdChoices.append(link)
            
            if condition(link,words=('opt',)):
                OptOut.append(link)
            
            if condition(link,words=('do-not-sell',)):
                DoNotSell.append(link)
            
            if condition(link,words=('california',)):
                CaliforniaNotice.append(link)
            if condition(link,words=('calirights',)):
                CaliforniaNotice.append(link)
            
            if condition(link,words=('ccpa',)):
                CaliforniaNotice.append(link)
            
            if condition(link,words=('cookie',)):
                cookiePolicy.append(link)
                
            
        items={
    'privacy':privacy,
    'terms': ToS,
    'opt':OptOut,
    'DoNotSell':DoNotSell,
    'Calif':CaliforniaNotice,
    'cookie':cookiePolicy,
        }
        
        if not(all(len(value)== 0 for value in items.values())):
            yield items

            
        
            
            
          

                    
                
           
        
 
 
            
 
