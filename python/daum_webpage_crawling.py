#!/usr/bin/env python
# coding: utf-8

import requests
import json
import urllib
import pandas as pd
from pandas import DataFrame

api_key = <<api_key>>


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"

session = requests.Session()
session.headers.update( {'User-agent': user_agent, 'referer': None, 'Authorization': 'KakaoAK ' + api_key} )

url_tpl = "https://dapi.kakao.com/v2/search/web"
wanted_word = "covid"

page = 1
size = 50

content_list = []
    
for i in range(0,6):
    page = i + 1      # 1~6까지가 된다.
    
    params = {"page": page, "query": wanted_word, "size": size}
    query = urllib.parse.urlencode(params)
    
    api_url = url_tpl + "?" + query
    api_url
    
    r = session.get(api_url)

    if r.status_code != 200:
        print("[%d Error] %s" % (r.status_code, r.reason))
        continue
        
    # 가져온 결과를 딕셔너리로 변환
    r.encoding = "utf-8"
    blog_dict = json.loads(r.text)

    # DataFrame 생성
    blog_df = DataFrame(blog_dict['documents'])
    
    # 내용에 해당하는 컬럼만 리스트로 추출하여 미리 준비한 리스트에 병합
    content_list += list(blog_df['contents'])
    
content_list

text = " ".join(content_list)
text


# other jupyter file
from konlpy.tag import Okt
from collections import Counter


nlp = Okt()

nouns = nlp.nouns(text)

words = []

for n in nouns:
    if len(n) > 1:
        words.append(n)
        
words

count = Counter(words)
most = count.most_common(100)
most
